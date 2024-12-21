def handler(pd: "pipedream"):

  email = f"""
<p>
Matches were found against your image. Matches were found on these targets:<br>
<strong>{', '.join(pd.steps["check_for_targets"]["$return_value"]["matches"])}</strong>
</p>
  """
    
  return {"email": email}
