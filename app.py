from flask import Flask, render_template, request, jsonify
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
        # 调用 deekseek-v1/-code API 进行代码优化
        response = requests.post("https://api.deekseek.com/v1/code", 
                                 headers={"Authorization": f"Bearer {api_key}"},
                                 json={"code": code, "prompt": prompt})
        response.raise_for_status()
        optimized_code = response.json().get("optimized_code")
        return jsonify({"optimized_code": optimized_code})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
