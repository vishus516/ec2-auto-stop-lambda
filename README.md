# ec2-auto-stop-lambda
Automatically stops EC2 using Lambda, Boto3, and EventBridge

# 🛑 EC2 Auto-Stop Lambda (Cost Saver)

Automatically stops non-production EC2 instances outside working hours using AWS Lambda, EventBridge, and Terraform.

---

## ✅ Features

- 🏷️ Tag-based EC2 selection (`AutoStop=True`)
- ⏰ Time-based trigger via EventBridge (e.g. 7:30 PM IST)
- 🐍 Lambda in Python using Boto3
- 💸 Reduces AWS cost by shutting down unused EC2
- 🧩 Fully automated via Terraform

---

## 🔧 Technologies Used

- **Terraform**
- **AWS Lambda (Python 3.13)**
- **Amazon EventBridge**
- **Boto3**
- *(Optional)* Slack or SNS Notification

---

## 🚀 How It Works

1. **Terraform** launches EC2 with `AutoStop=True` tag
2. **Lambda** checks EC2 instances daily at off-hours
3. If tag matches and instance is running → it is stopped
4. *(Optional)* Notification sent via Slack/SNS

---

## 🏗️ Project Structure

ec2-autostop/
│
├── main.tf # Terraform config to launch EC2
├── lambda_function.py # Python code for Lambda function
├── README.md # You're here


---

## 🛠️ Setup Instructions

### 1. Install Required Tools

- Terraform
- AWS CLI
- Python 3.x (for local testing, optional)

### 2. Configure AWS CLI

```bash
aws configure


### 3. Deploy with Terraform
'''bash
 terraform init
 terraform apply

### 4. Create Lambda Function
Runtime: Python 3.13

Paste code from lambda_function.py

Attach IAM role with ec2:DescribeInstances and ec2:StopInstances

### 5. Schedule via EventBridge
Use cron: cron(0 14 * * ? *) (7:30 PM IST)

Trigger your Lambda daily
