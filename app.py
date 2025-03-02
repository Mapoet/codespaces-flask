import os
from flask import Flask, render_template, request, jsonify
from pathlib import Path
import requests

app = Flask(__name__)

# 存储当前打开的文件夹路径
current_folder = None

def get_file_tree(directory):
    tree = []
    for path in Path(directory).rglob('*'):
        if path.is_file() and not path.name.startswith('.'):
            tree.append(str(path.relative_to(directory)))
    return tree

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/data")
def data_page():
    return "你已经打开了一个新的数据页"

@app.route("/optimize-page")
def optimize_page():
    return render_template("optimize.html")

@app.route("/update-file-tree", methods=['POST'])
def update_file_tree():
    global current_folder
    data = request.json
    files = data.get('files', [])
    if files:
        # 从第一个文件路径中提取文件夹路径
        first_file = files[0]
        current_folder = os.path.dirname(os.path.abspath(first_file))
    return jsonify({"status": "success"})

@app.route("/file-tree")
def file_tree():
    if current_folder:
        tree = []
        for path in Path(current_folder).rglob('*'):
            if path.is_file() and not path.name.startswith('.'):
                tree.append(str(path.relative_to(current_folder)))
        return jsonify({"files": tree})
    return jsonify({"files": []})

@app.route("/read-file")
def read_file():
    global current_folder
    path = request.args.get('path')
    if current_folder and path:
        full_path = os.path.join(current_folder, path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            return str(e), 500
    return "File not found", 404

@app.route("/save-file", methods=['POST'])
def save_file():
    global current_folder
    data = request.json
    path = data.get('path')
    content = data.get('content')
    if current_folder and path:
        full_path = os.path.join(current_folder, path)
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Invalid path"}), 400

@app.route("/optimize", methods=["POST"])
def optimize_code():
    data = request.json
    prompt = data.get('prompt')
    api_key = data.get('api_key')
    code = data.get('code')
    
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": prompt},
                    {"role": "user", "content": code}
                ]
            }
        )
        response.raise_for_status()
        optimized_code = response.json().get("choices")[0].get("message").get("content")
        return jsonify({"optimized_code": optimized_code})
    except Exception as err:
        return jsonify({"error": str(err)}), 500

if __name__ == "__main__":
    app.run(debug=True)
