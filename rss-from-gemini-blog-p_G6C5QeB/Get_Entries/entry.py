import os 
import requests 
def handler(pd: "pipedream"):

  # do we have a good cache?
  cache = pd.inputs["data_store"]
  cachedData = cache.get("entries")
  if cachedData:
    print("cache used")
    return cachedData

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

  entries = res.json()["data"]["blogposts"]
  cache.set("entries", entries, ttl=3600)
  return entries
