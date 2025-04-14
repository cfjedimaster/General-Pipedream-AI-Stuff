import os 
import requests 
import json 
from datetime import datetime, timedelta
import urllib.parse

def simplifyEvent(e): 

	event = {}

	if "description" in e["entity"]:
		event["description"] = e["entity"]["description"]
	if "startDateTime" in e["entity"]:
		date = datetime.fromtimestamp(e["entity"]["startDateTime"]["timestamp"] / 1000)
		event["startDateTime"] = date.strftime("%Y-%m-%d")

	event["name"] = e["entity"]["name"]
	event["url"] = f"https://{e['entity']['origin']}"
	
	return event
  
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
  apiCall = f"https://kg.diffbot.com/kg/v3/dql?type=query&token={token}&query={urllib.parse.quote(query)}&size=100"
  
  req = requests.get(apiCall)
  result = req.json()
  events = list(map(simplifyEvent, result["data"]))
  
  # cache is 12 hours
  data_store.set("cachedResult", events, ttl=43200)

  return events
