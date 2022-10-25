import openai

openai.api_key = "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"

def generate_script(prompt):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.7,
    max_tokens=4097-round(len(prompt)/2),
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response.choices[0]["text"]

print(generate_script("aniden sarki soylemekle ilgili bir yazi yaz"))