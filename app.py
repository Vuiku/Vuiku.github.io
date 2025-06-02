from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# Маршрут для статических файлов (CSS, JS, изображения)
@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('js', path)

@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('images', path)

# Маршрут для HTML страниц
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/pages/<path:path>')
def serve_pages(path):
    return send_from_directory('pages', path)

# Обработчик 404 ошибки
@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory('.', '404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 