import os 
import requests 
def handler(pd: "pipedream"):

  AGENTQL_API_KEY = os.environ.get("AGENTQL_API_KEY")
  URL = "https://developers.googleblog.com/en/search/?product_categories=Gemini"
  
  query = """
  {
      blogposts[] {
          url
          title
          date(convert to time since epoch)
      }
  }
  """

  body = {
      "query":query,
      "url":URL
  }

  headers = {
      "X-API-Key":AGENTQL_API_KEY,
      "Content-Type":"application/json"
  }

  res = requests.post("https://api.agentql.com/v1/query-data", json=body, headers=headers)
  return res.json()["data"]["blogposts"]
