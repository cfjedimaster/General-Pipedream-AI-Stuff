# pipedream add-package google-generativeai
import google.generativeai as genai

def handler(pd: "pipedream"):

  print(pd.steps["get_image"]["$return_value"]["path"])
  # Couldn't return the object directly, not serializable
  file = genai.upload_file(pd.steps["get_image"]["$return_value"]["path"])
  # workaround - return the name, refetch the file ob in the next step
  return file.name
