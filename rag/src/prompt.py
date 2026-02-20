def summary_prompt(text, length):
    return f"""
Summarize the following content.
Desired length: {length}

query : {text}
"""
