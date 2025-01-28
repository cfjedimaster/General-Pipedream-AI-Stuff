import markdown

def handler(pd: "pipedream"):

    html = f"""
<p>
Your support question has been received and will be answered as soon as possible. We took your
question and passed it to our expert AI system to see if we could quickly answer youir question:
</p>

<h2>AI Answer</h2>

{markdown.markdown(pd.steps["run_query"]["$return_value"])}

<p>
Please note we will still attempt to answer your question as soon as possible.
</p>
    """

    return html