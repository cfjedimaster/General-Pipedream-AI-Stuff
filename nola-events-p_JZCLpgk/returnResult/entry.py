def handler(pd: "pipedream"):

  pd.respond({
    "status": 200,
    "body": pd.steps["getEvents"]["$return_value"]
  })
