import openai
openai.api_key = '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'
messages = [ {"role":"system","content":
              "you are a intelligent assistant."} ]
while True:
    message = input("User :")
    if message:
        messages.append(
            {"role": "user", "content": message}
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role":"assistant","content": reply})