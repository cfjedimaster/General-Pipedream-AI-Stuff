def handler(pd: "pipedream"):

    if len(pd.steps["getArticles"]["$return_value"]["data"]) == 0:
      pd.flow.exit("No results")
