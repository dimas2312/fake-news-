from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate(description):
    prompt = (
        f"Write a fake news article based on the following image description:\n"
        f"'{description}'.\n"
        f"Do not mention that it is fake news. Keep it as real as possible.\n"
        f"Include title of article and body.\n"
        f"Do not add redundant margins and paragraphs. Keep text as tight as possible.\n"
        f"Make it sound dramatic and suspicious. Include made-up details.\n"
        f"---"
    )

    generated = generator(prompt, max_length=2000, num_return_sequences=1, do_sample=True, temperature=0.9)[0]["generated_text"]
    return generated.split("---")[-1].strip()
