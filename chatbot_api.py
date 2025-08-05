import os
import openai
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Set up the OpenAI client
client = OpenAI(api_key="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")


@app.route('/chat/', methods=['POST'])
def chat():
    data = request.get_json()
    user_prompt = data.get("prompt", "")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Or "gpt-4"
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )
        message = response.choices[0].message.content.strip()
        return jsonify({"response": message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
