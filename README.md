# **AI internal Chatbot powered by AWS Bedrock Knowledge Base RAG Workflow and trigger.dev**

- You can submit files to AWS S3 Bucket for which the LLM chosed using AWS Bedrock will refere to for private/specific information when asked questions about them
- You can test the already deployed/created trigger.dev workflow using the `test.py` in which you need to replace the `AUTH_TOKEN` with the one provided by trigger.dev
- To start the trigger.dev locally you need first to create a S3 bucket with files in it, a Bedrock Knowledge Base and a User with all the permisions needed. After that download the API keys and set them as env variables. 
- Choosed AWS for flexibility, experience working with and costs.
- Chatgpt is not trained with the current API/SDK for the AWS Bedrock, neither with trigger.dev. So, a deep dive into the documentation was needed.
- There could be a frontend too and the posibility of easy uploading of documents to the S3 (without the API or the AWS Console)