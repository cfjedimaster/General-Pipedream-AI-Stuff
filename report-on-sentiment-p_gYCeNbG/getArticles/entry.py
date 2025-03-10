import os 
import requests 
import json 
from datetime import datetime, timedelta
import urllib.parse

def handler(pd: "pipedream"):

  token = os.environ.get("db_token")
  
  today = datetime.now()
  lastWeek = today + timedelta(days=-7)
  fLastWeek = lastWeek.strftime("%Y-%m-%d")

  query = f'type:Article tags.label:"Xbox" language:"en" sentiment<=0 date>{fLastWeek} sortBy:date'
  
  apiCall = f"https://kg.diffbot.com/kg/v3/dql?type=query&token={token}&query={urllib.parse.quote(query)}&size=25"
  
  req = requests.get(apiCall)
  return json.loads(req.content)
  
