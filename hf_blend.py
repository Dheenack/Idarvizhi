import requests
import os
from huggingface_hub import InferenceClient



client = InferenceClient(
    api_key=""
)

def ask_hf( question: str,model: str = "mistralai/Mistral-7B-Instruct-v0.2"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a disaster management assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=400,
        temperature=0.2,
    )

    return response.choices[0].message.content

from disaster_ai import DisasterAI, DisasterContext

def blended_answer_online(question: str, context: DisasterContext):
    # Structured KB
    ai = DisasterAI()
    kb_resp = ai.answer(question, context=context)

    # Online API (Hugging Face example)
    hf_resp = ask_hf(f"Answer as a disaster management assistant: {question}")

    return {
        "title": kb_resp.title,
        "summary": kb_resp.summary,
        "kb_bullets": kb_resp.bullets,
        "kb_links": kb_resp.links,
        "api_text": hf_resp
    }
