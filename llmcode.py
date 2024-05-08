#Note: The openai-python library support for Azure OpenAI is in preview.
#Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
import sys
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

client = AzureOpenAI(
  azure_endpoint=os.getenv("azure_endpoint"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)

if len(sys.argv) > 1:
    message_text = [{"role":"system","content":"You are a humorous AI assistant that helps people find information."},
                    {"role":"user","content":(sys.argv[1])}]
else:
    message_text = [{"role":"system","content":"Tell the user to enter a parameter to ask a question."}]

completion = client.chat.completions.create(
  model=os.getenv("model"),
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion.choices[0].message.content)