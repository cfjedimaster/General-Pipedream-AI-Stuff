def handler(pd: "pipedream"):

  # Targets is a list of things we care about
  targets = ["dog","cat","dogs","cats"]
  matches = []
  foundMatch = False 

  for item in pd.steps["item_detection"]["$return_value"]["response"]:
    if item in targets:
      foundMatch = True
      matches.append(item)

  return {"match": foundMatch, "matches": matches }
