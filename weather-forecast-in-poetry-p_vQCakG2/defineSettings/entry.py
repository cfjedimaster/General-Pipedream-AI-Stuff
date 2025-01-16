import os

def handler(pd: "pipedream"):
  return {
    "apikey": os.environ["PIRATE_WEATHER"],
    "latitude": 30.216667,
    "longitude": -92.033333 
  }