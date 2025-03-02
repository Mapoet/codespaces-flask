# Flask Code Optimization Project

## 项目目的

本项目旨在通过 Flask 框架构建一个简单的 Web 应用，用户可以上传多个代码文件，并使用 DeepSeek API 对代码进行优化。该项目展示了如何集成第三方 API 以增强代码质量和性能。

## 功能

- 首页展示项目介绍和优化代码按钮
- 代码优化页面，支持上传多个文件
- 使用 DeepSeek API 对上传的代码进行优化
- 显示优化后的代码或错误信息

## 依赖

- Flask==2.3.2
- requests==2.28.1
- openai==0.27.0

## 使用方式

1. 克隆本项目到本地：
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

3. 运行 Flask 应用：
    ```sh
    flask --debug run
    ```

4. 打开浏览器访问 `http://127.0.0.1:5000`，进入首页。

5. 点击“优化代码”按钮，进入代码优化页面。

6. 在代码优化页面：
    - 输入 Deekseek API Key
    - 输入提示信息
    - 上传需要优化的代码文件
    - 点击“优化代码”按钮，查看优化后的代码或错误信息

## 注意事项

- 确保已安装 Python 3.7 及以上版本
- 确保网络连接正常，以便调用 DeepSeek API
- 上传的文件应为文本文件，且总大小不应超过 API 限制

## 作者

本项目由 `MapoetNiphy` 开发。

## 致谢

特别感谢 GitHub 和 Codespaces 提供的开发平台和工具支持。