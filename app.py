from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/data")
def data_page():
    return "你已经打开了一个新的数据页"

@app.route("/optimize-page")
def optimize_page():
    return render_template("optimize.html")

@app.route("/optimize", methods=["POST"])
def optimize_code():
    data = request.json
    code = data.get("code")
    api_key = data.get("api_key")
    prompt = data.get("prompt")
    try:
        # 调用 DeepSeek API 进行代码优化
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
                {"role": "user", "content": code}
            ],
            stream=False
        )
        optimized_code = response.choices[0].message.content
        return jsonify({"optimized_code": optimized_code})
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error occurred: {http_err}"}), 500
    except requests.exceptions.RequestException as req_err:
        return jsonify({"error": f"Request error occurred: {req_err}"}), 500
    except Exception as err:
        return jsonify({"error": f"An error occurred: {err}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
