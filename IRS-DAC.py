from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, EC2AutoScaling, Lambda
from diagrams.aws.database import RDS, Dynamodb, RDSInstance, RDSMariadbInstance
from diagrams.aws.storage import S3, S3Glacier, EBS
from diagrams.aws.network import VPC, ELB, CF, APIGateway, NATGateway, InternetGateway, PrivateSubnet, PublicSubnet, RouteTable
from diagrams.aws.security import IAM, WAF, Shield, Cognito
from diagrams.aws.management import Cloudwatch, Cloudtrail, Config, OrganizationsAccount
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.storage import Backup
from diagrams.aws.database import ElastiCache
from diagrams.aws.general import General
from diagrams.onprem.client import User, Users, Client

# Define graph attributes
graph_attr = {
    "fontsize": "28",
    "bgcolor": "white",
    "pad": "0.75"
}

with Diagram("Indian Railways System - AWS Migration Architecture (Cost-Optimized)", show=False, direction="TB", graph_attr=graph_attr):
    
    # End Users
    user_web = Users("Web Users")
    user_mobile = Client("Mobile App Users")
    user_agent = User("Agents & Operators")
    
    # Global Edge and CDN
    cdn = CF("CloudFront CDN")
    
    # API Gateway
    api = APIGateway("API Gateway")
    
    # Load Balancers
    alb = ELB("Application Load Balancer")
    
    # Security at Edge
    edge_security = Shield("AWS Shield")
    waf = WAF("Web Application Firewall")
    
    # VPC Infrastructure
    with Cluster("Virtual Private Cloud (VPC)"):
        igw = InternetGateway("Internet Gateway")
        
        with Cluster("Public Zone - DMZ"):
            public_subnets = PublicSubnet("Public Subnets")
            nat = NATGateway("NAT Gateway")
            bastion = EC2("Bastion Host")
        
        with Cluster("Private Zone - Application Tier"):
            private_app_subnets = PrivateSubnet("Private App Subnets")
            
            # Auto Scaling Groups
            with Cluster("Auto Scaling Groups"):
                web_asg = EC2AutoScaling("Web Servers")
                api_asg = EC2AutoScaling("API Servers")
                booking_asg = EC2AutoScaling("Booking Servers")
                tatkal_asg = EC2AutoScaling("Tatkal Servers")
            
            # Serverless Components
            with Cluster("Serverless Functions"):
                notification_lambda = Lambda("Notifications")
                report_lambda = Lambda("Reports Generation")
                payment_lambda = Lambda("Payment Processing")
                analytics_lambda = Lambda("Analytics")
        
        with Cluster("Private Zone - Data Tier"):
            private_data_subnets = PrivateSubnet("Private Data Subnets")
            
            # Databases
            with Cluster("Database Layer"):
                with Cluster("RDS Multi-AZ"):
                    primary_db = RDSInstance("Primary")
                    standby_db = RDSMariadbInstance("Standby")
                
                ddb_ticket = Dynamodb("Ticket Status")
                ddb_trains = Dynamodb("Train Schedule")
                cache = ElastiCache("Session Cache")
            
            # Storage
            with Cluster("Storage Layer"):
                ebs = EBS("EBS Volumes")
                s3_data = S3("Data Lake")
                s3_logs = S3("Logs & Audit")
                glacier = S3Glacier("Long-term Archive")
    
    # Integration Services
    with Cluster("Integration Services"):
        queue = SQS("Message Queue")
        notification = SNS("Notifications")
        events = Eventbridge("Event Bus")
    
    # Management & Governance
    with Cluster("Operations & Governance"):
        monitoring = Cloudwatch("CloudWatch")
        audit = Cloudtrail("CloudTrail")
        compliance = Config("Config")
        backup = Backup("AWS Backup")
    
    # Identity & Access
    with Cluster("Identity & Security"):
        identity = IAM("IAM")
        auth = Cognito("User Authentication")
    
    # Disaster Recovery
    with Cluster("Disaster Recovery"):
        dr_mechanism = General("DR Strategy")
        cross_region = Edge(label="Cross-Region Replication")
    
    # Connections - User Access Layer
    user_web >> cdn
    user_mobile >> cdn
    user_agent >> cdn
    
    # Edge Security
    cdn >> edge_security
    edge_security >> waf
    waf >> api
    waf >> alb
    
    # API Gateway and Load Balancer to VPC
    api >> igw
    alb >> igw
    igw >> public_subnets
    
    # Public to Private Routing
    public_subnets >> nat
    public_subnets >> bastion
    nat >> private_app_subnets
    
    # Application Tier Components
    alb >> web_asg
    api >> api_asg
    api >> booking_asg
    api >> tatkal_asg
    
    # App to Lambda
    api_asg >> notification_lambda
    api_asg >> report_lambda
    booking_asg >> payment_lambda
    
    # App to Integration
    web_asg >> queue
    api_asg >> queue
    booking_asg >> queue
    tatkal_asg >> queue
    
    queue >> notification_lambda
    queue >> analytics_lambda
    
    notification_lambda >> notification
    events >> analytics_lambda
    
    # App to Database
    web_asg >> cache
    api_asg >> cache
    booking_asg >> primary_db
    tatkal_asg >> ddb_ticket
    
    # Database Replication
    primary_db >> standby_db
    primary_db >> s3_data
    ddb_ticket - ddb_trains
    
    # Storage Connections
    primary_db >> ebs
    standby_db >> ebs
    s3_data >> glacier
    s3_logs >> glacier
    
    # Monitoring & Management
    web_asg >> monitoring
    api_asg >> monitoring
    booking_asg >> monitoring
    tatkal_asg >> monitoring
    primary_db >> monitoring
    ddb_ticket >> monitoring
    
    monitoring >> notification
    
    # Backup & DR
    primary_db >> backup
    standby_db >> backup
    ddb_ticket >> backup
    ddb_trains >> backup
    s3_data >> backup
    
    backup >> s3_logs
    backup >> glacier
    backup >> dr_mechanism
    dr_mechanism - cross_region
    
    # Security & Compliance
    identity >> web_asg
    identity >> api_asg
    identity >> booking_asg
    identity >> tatkal_asg
    
    auth >> api
    
    web_asg >> audit
    api_asg >> audit
    booking_asg >> audit
    primary_db >> audit
    
    audit >> s3_logs
    audit >> compliance