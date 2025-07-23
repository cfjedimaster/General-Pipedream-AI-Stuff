def handler(pd: "pipedream"):
    # I'm just used to set some values used a few times in the later steps
    # blogUrl is the url to hit obviously, 
    # title and desc are used in the RSS generation area. blogTZ adds a tz to dates
    return {
      "blogUrl": "https://developers.googleblog.com/en/search/?product_categories=Gemini",
      "title": "Google Gemini Blog Enties",
      "description": "AI Generated RSS Feed for Google Gemini Blog",
      "blogTZ":"America/Los_Angeles"
    }
