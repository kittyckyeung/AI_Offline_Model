from gpt4all import GPT4All
print("Testing GPT4All installation...")

try:
    models = GPT4All.list_models()
    print(f"GPT4All working! Found {len(models)} available models:")
    print("First few models:")

    for i, model in enumerate(models[:5]):
        name = model.get("name", "unknown")
        size = model.get("filesize", "unknown size")
        print(f"{i+1}. {name} ({size})")
except Exception as e:
    print(f"Error: {e}")
