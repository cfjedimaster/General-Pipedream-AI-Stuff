def handler(pd: "pipedream"):

  email = f"""
Matches were found against your image. Matches were found on these targets:

{pd.steps["check_for_targets"]["$return_value"]["matches"]}
  """
    
  return {"email": email}
