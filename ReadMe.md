# IRS Migration to AWS Cloud

## Project Overview

This project explores the migration of the **Indian Railways System (IRS)** from a legacy, on-premises infrastructure to a **cloud-native architecture on AWS**. The goal was to address challenges like high latency, poor scalability, rising operational costs, and security concerns by leveraging AWS services for a modern, resilient, and cost-optimized IT environment.

> This was a **group project** completed as part of an **AWS Cloud internship** during my time at **F13 Technologies**, carried out under the guidance of a mentor, with collaborative contributions across architecture design, research, cost analysis, and presentation.

---

## Key Functionalities of IRS Platform

- **Real-Time Ticketing** with secure transactions  
- **AI-Powered Train Scheduling** using real-time and predictive data  
- **Freight & Logistics** optimization through forecasting and tracking  
- **Live GPS Tracking** and Delay Predictions  
- **Predictive Analytics** for maintenance and capacity planning  
- **Secure Cloud-Based Data Management**  

---

## System Architecture

### Pre-Migration (On-Premises)

- Data centers in Secunderabad and Gurugram (managed by RailTel)  
- Centralized compute with high latency and limited scalability  
- Manual infrastructure scaling and high CapEx  

### Post-Migration (AWS Cloud)

| Layer | AWS Services |
|-------|---------------|
| **Compute** | Amazon EC2, AWS Lambda, Auto Scaling |
| **Databases** | Amazon RDS, DynamoDB |
| **Storage** | Amazon S3, Glacier |
| **Networking** | Amazon VPC, CloudFront |
| **Security** | IAM, AWS WAF, AWS Shield |
| **Monitoring** | CloudWatch, CloudTrail |
| **Migration** | AWS DMS, SMS, Snowball, Migration Hub |

> Architecture design and cost comparison were documented and modeled using cloud best practices, with cloud-native alternatives considered at each layer.

---

## Migration Process

Follows the **AWS 6 Rs Strategy**:
- **Rehost** – Lift and shift legacy apps  
- **Replatform** – Slight modifications for scalability  
- **Refactor** – Redesign where needed for cloud-native deployment

### Migration Phases

1. Discovery & Inventory  
2. Assessment & Planning  
3. AWS Environment Setup  
4. Data & Application Migration  
5. Testing, Optimization, and Security Setup  
6. Go-Live and Knowledge Transfer

---

## Cost Analysis

| Phase | Details |
|-------|---------|
| **Before Migration** | High CapEx for servers, cooling, security, and IT staff |
| **During Migration** | Dual operations, training, and migration tooling |
| **After Migration** | Pay-as-you-go model, auto-scaling, lifecycle storage |

Implemented cost optimization strategies:  
- Reserved Instances  
- S3 tiering to Glacier  
- Serverless adoption for non-critical workloads  
- CloudWatch-based cost tracking

---

## Security & Compliance

- Defense-in-depth using IAM, Shield, WAF, and VPC isolation  
- Encryption (at rest and in transit) using KMS  
- Backup & DR with Multi-AZ and Cross-Region Replication  
- Regulatory compliance tracking via CloudTrail and AWS Config

---

## Acknowledgment

This project was developed as part of a **group internship project/assignment** under the mentorship of experienced AWS professionals. Team contributions included architecture analysis, migration strategy, cost modeling, and documentation.

---

## License

This repository is intended for educational, professional portfolio, and demonstration purposes only.
