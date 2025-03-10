from datetime import datetime

def handler(pd: "pipedream"):

  email = f"""
Negative Article Results:

Our search found {pd.steps["getArticles"]["$return_value"]["hits"]} results. Here are the top 25:
  """  

  for result in pd.steps["getArticles"]["$return_value"]["data"]:
    date = datetime.fromtimestamp(result["entity"]["date"]["timestamp"] / 1000)
    date_f = date.strftime("%Y-%m-%d")
    
    email += f"""
{result["entity"]["title"]}
Sentiment:  {result["entity"]["sentiment"]}
Published:  {date_f}
Link:       {result["entity"]["pageUrl"]}
    """

  return email