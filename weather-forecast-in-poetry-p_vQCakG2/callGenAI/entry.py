# pipedream add-package google-generativeai
import google.generativeai as genai

import os 

def handler(pd: "pipedream"):

  genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

  model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Given a forecast, rewrite it in poetry. Return just the poem and nothing more."
  )
  
  response = model.generate_content(pd.steps["writeSummary"]["$return_value"])

  return response.text

