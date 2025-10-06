import requests
import json
from shared import LABELS
from apikey import api_key

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


def validate_extraction(chunks: list[dict]) -> dict:
    """
    Validates the chunking and classification of sections.
    """
    msg = "You are a helpful assistant for classifying chunks from Request for Proposal (RFP) documents. " \
          "Given a section of text from an RFP, determine which category it best fits from the following categories:\n" \
          "\n".join([f"- {key}: {value}" for key, value in LABELS.items()])
    data_ext = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "system", "content": msg},
            {"role": "user", "content": ""}
        ]
    }
    labels = "\n".join(f"{key}: {value}" for key, value in LABELS.items())
    first_half = chunks[:len(chunks) // 2]
    second_half = chunks[len(chunks) // 2:]
    segments = [first_half, second_half]
    results = []
    try:
        # for sec in chunks:
        #     sec_text = sec["title"] + "\n" + sec["body"]
        #     data_ext["messages"][1]["content"] = f"""
        #     This is a section from an RFP.
        #     --- START OF SECTION ---
        #     {sec_text[:4000]}
        #     --- END OF SECTION ---
        #     Return ONLY one of the labels, which are defined:\n{labels}\nIf none of the labels fit, return N/A. No explanation is required.
        #     """
        #     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data_ext)
        #     result = response.json()["choices"][0]["message"]["content"]
        #     lower_keys = [key.lower() for key in LABELS.keys()]
        #     lower_keys.append("N/A")
        #     sec["true_label"] = find_pattern(result.lower(), lower_keys)
        for sec in segments:
            data_ext["messages"][1]["content"] = f"""
                Here is a json of all the chunks of text to classify.
                --- START OF JSON ---
                {json.dumps(sec)}
                --- END OF JSON ---
                For each chunk, decide on ONLY one of the labels, which are defined:\n{labels}\nIf none of the labels fit, return N/A. No explanation is required.
                Return the same json with the key 'true_label' appended to each chunk, with the value being the chosen label.
            """
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data_ext)
            result = response.json()["choices"][0]["message"]["content"]
            print(result)
            results.extend(json.loads(result))
    except Exception as e:
        print("Issue during LLM labeling: ", e, "\n", response.json())
    return results

def find_pattern(text, patterns):
    """
    Finds the first instance of one of the patterns in a string.
    """
    first_match = None
    first_index = len(text) + 1

    for pattern in patterns:
        idx = text.find(pattern)
        if idx != -1 and idx < first_index:
            first_index = idx
            first_match = pattern

    return first_match.capitalize()

def summarize(categories: dict) -> dict:
    """
    Using an LLM model (https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1), this function:
    - Summarizes the categories.
    - Suggests actionable insights or next steps.
    """
    labels = "\n".join(f"{key}: {value}" for key, value in LABELS.items())
    text = {key: None for key in LABELS.keys()}
    for key in text.keys():
        text[key] = [sec["title"] + "\n" + sec["body"] for sec in categories[key]["sections"]]
    data["messages"][1]["content"] = f"The following json provides chunks of text are from an RFP document." \
                                      f"The keys are the categories, which are defined:\n{labels}\n" \
                                      f"Consider the following json:\n{str(text)}\n" \
                                      f"Provide a detailed summary of the chunks in each category based on the descriptions provided above, " \
                                      f"keeping in mind that the chunks may correspond to more than one category. " \
                                      f"After that, suggest actionable insights or next steps. " \
                                      f"Return ONLY a json string with the defined categories as keys, " \
                                      f"the generated summaries for each category as values, " \
                                      f"and an additional key 'Insights', which should include the generated insights and/or actionable steps as the value."
    # print(data["messages"][1]["content"])
    # return [data["messages"][1]["content"]]
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]