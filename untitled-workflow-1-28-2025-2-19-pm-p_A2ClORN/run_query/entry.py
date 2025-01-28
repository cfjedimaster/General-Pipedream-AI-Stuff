# pipedream add-package pinecone
# pipedream add-package pinecone-plugin-assistant
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message
import os

def handler(pd: "pipedream"):

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
  assistant = pc.assistant.Assistant(assistant_name="dandd")

  print(pd.steps["trigger"]["event"]["body"]["text"])
  msg = Message(role="user",content=pd.steps["trigger"]["event"]["body"]["text"])
  resp = assistant.chat(messages=[msg])
  return resp.message.content
