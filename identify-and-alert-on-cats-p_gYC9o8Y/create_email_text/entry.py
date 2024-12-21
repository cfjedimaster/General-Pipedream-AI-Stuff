def handler(pd: "pipedream"):

  email = f"""
<p>
Matches were found against your image. Matches were found on these targets:<br>
<strong>{', '.join(pd.steps["check_for_targets"]["$return_value"]["matches"])}</strong>
</p>

<h2>Image</h2>
<img src="{pd.steps["trigger"]["event"]["body"]["raw_body_url"]}" width="400">
  """
    
  return {"email": email}
