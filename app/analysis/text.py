from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="openai-community/gpt2")
set_seed(42)

def generate(description):
    print(f"Desc: '{description}'")

    prompt = (
        f"Write news article based on the following short image description:\n"
        f"'{description}'.\n"
        f"Make it sound dramatic and suspicious. Include made-up details.\n"
        f"---"
    )

    generated = generator(prompt, max_length=200, num_return_sequences=1, do_sample=True, temperature=0.9)[0]["generated_text"]
    print(generated)
    return generated.split("---")[-1].strip()
