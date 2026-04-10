\# ☁️ CloudContact



A serverless contact form built on AWS. Users can submit their name, email, and message through a web form. The submission is saved to a database and an email notification is sent instantly.



\## 🏗️ Architecture



User → CloudFront → S3 (HTML Form)

↓

API Gateway

↓

Lambda

↙        ↘

DynamoDB        SES

(saves submission) (sends email)



\## 🛠️ AWS Services Used



\- S3 — Hosts the static HTML contact form

\- CloudFront — CDN for fast global delivery and HTTPS

\- API Gateway — Public HTTP endpoint for the form submission

\- Lambda — Serverless function that processes submissions (Python)

\- DynamoDB — NoSQL database that stores all form submissions

\- SES — Sends email notification on every new submission

\- IAM — Roles and policies for secure service communication

\- CloudWatch — Logs and monitoring for Lambda



\## 💡 How It Works



1\. User visits the CloudFront URL and fills in the contact form

2\. JavaScript sends a POST request to API Gateway

3\. API Gateway triggers the Lambda function

4\. Lambda saves the submission to DynamoDB

5\. Lambda sends an email notification via SES

6\. User sees a success message on the form



\## 🚀 What I Learned



\- Serverless architecture patterns on AWS

\- How API Gateway connects frontend to backend

\- IAM roles and least privilege security

\- NoSQL data storage with DynamoDB

\- Email delivery with SES in sandbox mode

\- Static website hosting with S3 and CloudFront

\- Debugging with CloudWatch logs

\- Git version control workflow



\## 📸 Screenshot



<img width="1896" height="905" alt="Screenshot 2026-04-10 152155" src="https://github.com/user-attachments/assets/700ab8f0-449d-452f-a8db-36bf529f8892" />




\## ⚙️ Tech Stack



\- Frontend: HTML, CSS, JavaScript

\- Backend: Python (AWS Lambda)

\- Database: AWS DynamoDB

\- Cloud: Amazon Web Services

