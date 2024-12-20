def handler(pd: "pipedream"):

  if pd.steps["check_for_targets"]["$return_value"]["match"] == False:
    return pd.flow.exit("Ended because no match.")    
