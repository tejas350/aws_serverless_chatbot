⚡ AWS Serverless Chatbot (Python)

The AWS Serverless Chatbot is a fully serverless, event-driven conversational bot built using AWS Lambda, API Gateway, and DynamoDB.
It processes user messages, generates intelligent responses using Python logic, and stores chat history without requiring any servers or manual scaling.

This project demonstrates skills in cloud architecture, Python backend development, event-driven workflows, and serverless design patterns.

🚀 Features
✅ Fully Serverless Architecture

Built using AWS services with zero infrastructure management:

AWS Lambda for processing user messages

API Gateway for HTTPS access

DynamoDB for storing chat history

IAM Roles & Policies for secure access

✅ Python-Based Chat Engine

Handles:

Input parsing

Response generation

Validation

DynamoDB operations

✅ REST API Endpoint

Users can send messages to a single API endpoint such as:

POST /chatbot
{
    "message": "Hello"
}

✅ Scalable and Cost-Efficient

Auto-scales based on number of requests

Pay-per-use pricing

No servers or VMs required

✅ Cloud-Ready and Extensible

You can integrate this chatbot with:

Mobile apps

Web front-end

WhatsApp or Telegram API

ChatGPT/OpenAI API

SNS, SQS, EventBridge

🧩 Architecture Overview
Client -> API Gateway -> Lambda (Python) -> DynamoDB -> Response back to client

Components:

API Gateway – Receives user request

Lambda Function (Python) – Contains chatbot logic

DynamoDB – Stores chat conversation history

CloudWatch Logs – Logs and debugging

IAM Roles – Secure resource access

📁 Project Structure
aws-serverless-chatbot/
│
├── lambda_function.py        # Main chatbot logic
├── requirements.txt          # Python dependencies
├── deploy/                   # Infrastructure or packaging scripts
└── README.md                 # Project documentation

🛠️ Setup Instructions
1️⃣ Install Dependencies Locally
pip install -r requirements.txt -t .

2️⃣ Zip the Lambda Package
zip -r chatbot.zip .

3️⃣ Create AWS Lambda Function

Runtime: Python 3.10

Handler: lambda_function.lambda_handler

Upload the ZIP file

4️⃣ Create API Gateway (REST API)

Method: POST

Integration: Lambda Proxy

5️⃣ Create DynamoDB Table

Example:

Table Name: ChatHistory

Partition Key: session_id

▶️ Example Request
POST https://your-api-id.execute-api.region.amazonaws.com/chatbot

{
    "session_id": "user1",
    "message": "Hi"
}

Example Response
{
    "reply": "Hello! How may I assist you today?"
}

🧠 How It Works

User sends a message

API Gateway forwards it to Lambda

Lambda processes message using Python logic

DynamoDB stores message and reply

Lambda returns response back to the user

🧪 Testing

Run locally:

python lambda_function.py


Test via cURL:

curl -X POST https://your-api/chatbot \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'

🌱 Future Improvements

Integrate OpenAI for AI-generated responses

Add sentiment analysis

Add authentication (Cognito)

Build a frontend UI

Add WhatsApp/Twilio integration
