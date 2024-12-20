import requests 

def handler(pd: "pipedream"):

  #first, did we have an image?
  if "raw_body_url" not in pd.steps["trigger"]["event"]["body"]:
    pd.flow.exit("No media uploaded to event")

  # what type was it?
  mediaType = pd.steps["trigger"]["event"]["headers"]["content-type"]

  if mediaType.endswith("png"):
    tmpFile = "/tmp/file.png"
  elif mediaType.endswith("jpg"):
    tmpFile = "/tmp/file.jpg"
  else:
    pd.flow.exit(f"Invalid content type passed, {mediaType}")
  
  with requests.get(pd.steps["trigger"]["event"]["body"]["raw_body_url"], stream=True) as response:
    # Check if the request was successful
    response.raise_for_status()
 
    # Open the new file /tmp/file.html in binary write mode
    with open(tmpFile, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
          
    return { "path": tmpFile}  
