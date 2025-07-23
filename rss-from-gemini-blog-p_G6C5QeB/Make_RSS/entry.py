from feedgen.feed import FeedGenerator
from datetime import datetime 
from pytz import timezone as pytz_timezone

def handler(pd: "pipedream"):

  URL = "https://developers.googleblog.com/en/search/?product_categories=Gemini"

  fg = FeedGenerator()
  fg.title(pd.steps["Define_Constants"]["$return_value"]["title"])
  fg.description(pd.steps["Define_Constants"]["$return_value"]["description"])
  fg.link(href=pd.steps["Define_Constants"]["$return_value"]["blogUrl"])

  timezone = pytz_timezone(pd.steps["Define_Constants"]["$return_value"]["blogTZ"])

  for entry in pd.steps["Get_Entries"]["$return_value"]:
      fe = fg.add_entry()
      fe.id(entry["url"])
      fe.title(entry["title"])
      fe.link(href=entry["url"])
      date = datetime.fromtimestamp(entry["date"])
      localized_dt = date.astimezone(timezone)
      fe.published(localized_dt)

  # not sure why they return a byte string
  tempStr = fg.rss_str()
  string_data = tempStr.decode("utf-8")
  #json_output = json.dumps({"message": string_data})
  return string_data
  