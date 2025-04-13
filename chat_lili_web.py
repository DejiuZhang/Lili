import os
import openai
import gradio as gr

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_ID = os.getenv("MODEL_ID")

def chat_with_lili(message, history):
    messages = [{"role": "system", "content": "You are Lili, a 13-year-old girl in a single-parent household...（你的完整系统 prompt 可以粘贴在这里）"}]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=messages
    )
    return response.choices[0].message["content"]

gr.ChatInterface(
    fn=chat_with_lili,
    title="Chat with Lili 👧",
    description="Lili is your virtual child, a 13-year-old girl facing school bullying. Talk with her.",
    theme="soft"
).demo.launch(
    server_name="0.0.0.0",
    server_port=10000,
    share=True
)
