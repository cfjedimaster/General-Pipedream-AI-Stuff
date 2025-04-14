import os 
import requests 
import json 
from datetime import datetime, timedelta
import urllib.parse

def handler(pd: "pipedream"):

  data_store = pd.inputs["data_store"]

  if "cachedResult" in data_store:
    print("Returning from cache")
    return data_store["cachedResult"]

  token = os.environ.get("db_token")
  
  today = datetime.now()
  startDate = today + timedelta(days=-30)
  fStartDate = startDate.strftime("%Y-%m-%d")

  query = f'type:Event locations.region.name:"Louisiana" locations.city.name:"New Orleans" startDateTime>{fStartDate} sortBy:startDateTime'
  apiCall = f"https://kg.diffbot.com/kg/v3/dql?type=query&token={token}&query={urllib.parse.quote(query)}&size=250"
  
  req = requests.get(apiCall)
  # cache is 12 hours
  data_store.set("cachedResult", req.json(), ttl=43200)

  return json.loads(req.content)
