# pipedream add-package google-generativeai
import google.generativeai as genai
# pipedream add-package pip install google-ai-generativelanguage
from google.ai.generativelanguage_v1beta.types import content

import os 
import json 

def handler(pd: "pipedream"):

  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_schema": content.Schema(
      type = content.Type.OBJECT,
      properties = {
        "response": content.Schema(
          type = content.Type.ARRAY,
          items = content.Schema(
            type = content.Type.STRING,
          ),
        ),
      },
    ),
    "response_mime_type": "application/json",
  }

  # Ok, technically not a new file, just a new file object :) 
  newFile = genai.get_file(pd.steps["upload_to_gemini"]["$return_value"])
  
  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Given an image, you return a list of items found in the image. You sort the results by the items you have the highest confidence in.",
  )

  result = model.generate_content([newFile,"what's in this photo"])
  print(result)
  return json.loads(result.text)

