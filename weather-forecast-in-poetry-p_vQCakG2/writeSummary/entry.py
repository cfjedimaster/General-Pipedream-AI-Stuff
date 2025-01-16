def handler(pd: "pipedream"):
  summary = f"""
The forecast for today is {pd.steps['getForecast']['$return_value']['summary']}, with a {pd.steps['getForecast']['$return_value']['precipProbability']*100} percent chance of {pd.steps['getForecast']['$return_value']['precipType']}.
The high temperature will be {pd.steps['getForecast']['$return_value']['temperatureHigh']}F and a low of {pd.steps['getForecast']['$return_value']['temperatureLow']}F.
  """

  print(summary)
  return summary