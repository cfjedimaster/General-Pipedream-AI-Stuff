import requests

def handler(pd: "pipedream"):

  data = requests.get(f"https://api.pirateweather.net/forecast/{pd.steps['defineSettings']['$return_value']['apikey']}/{pd.steps['defineSettings']['$return_value']['latitude']},{pd.steps['defineSettings']['$return_value']['longitude']}?exclude=minutely,hourly,currently,alerts")
  return (data.json())["daily"]["data"][0]