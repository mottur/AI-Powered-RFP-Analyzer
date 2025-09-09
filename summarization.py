import requests
from shared import LABELS

api_key = "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"

headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "AI-Powered-RFP-Analyzer",  # Can be your email or app URL
    "Content-Type": "application/json",
}

system_msg = "You are a helpful assistant for summarizing Request for Proposal (RFP) documents. Given a category of text from an RFP, " \
"provide a concise summary and suggest actionable insights or next steps for responding to the RFP. " \

data = {
    "model": "meta-llama/llama-3.3-70b-instruct:free",
    "messages": [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": ""}
    ]
}


def validate_extraction(categories: dict) -> dict:
    """
    Validates the chunking and classification of sections.
    """
    msg = "You are a helpful assistant for validating text extraction from Request for Proposal (RFP) documents. " \
          "Given a section of text from an RFP, determine if it best fits the specified category from the following categories:\n" \
          "\n".join([f"- {key}: {value}" for key, value in LABELS.items()])
    data_ext = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "system", "content": msg},
            {"role": "user", "content": ""}
        ]
    }
    for cat in categories.keys():
        for sec in categories[cat]["sections"]:
            sec_text = sec["title"] + "\n" + sec["body"]
            data_ext["messages"][1]["content"] = f"""
            This is a section from an RFP. Does it describe {cat}?
            --- START OF SECTION ---
            {sec_text[:4000]}  # Truncate to first 4000 chars to fit token limits
            --- END OF SECTION ---
            Answer: Yes or No. If yes, explain why.
            """
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data_ext)
            sec["validation"] = response.json()["choices"][0]["message"]["content"]
    return categories

def summarize(categories: dict) -> dict:
    """
    Using an LLM model (https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1), this function:
    - Summarizes the categories.
    - Suggests actionable insights or next steps.
    - Validates extraction logic through prompt engineering.
    """
    labels = "\n".join(f"{key}: {value}" for key, value in LABELS.items())
    text = {key: None for key in LABELS.keys()}
    for key in text.keys():
        text[key] = [sec["title"] + "\n" + sec["body"] for sec in categories[key]["sections"]]
    data["messages"][1]["content"] = f"The following json provides chunks of text are from an RFP document." \
                                      f"The keys are the categories, which are defined:\n{labels}\n" \
                                      f"Consider the following json:\n{str(text)}\n" \
                                      f"Provide a concise summary of the chunks in each category based on the descriptions provided above, " \
                                      f"keeping in mind that the chunks may correspond to more than one category. " \
                                      f"After that, suggest actionable insights or next steps. " \
                                      f"Return a json string with the defined categories as keys, " \
                                      f"the generated summaries for each category as values, " \
                                      f"and an additional key 'Insights', which should include the generated insights as the value."
    # print(data["messages"][1]["content"])
    # return [data["messages"][1]["content"]]
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]