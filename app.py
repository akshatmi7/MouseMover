from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Check if running in Render (headless)
if os.environ.get('RENDER') == 'true':
    pyautogui = None
else:
    import pyautogui


@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML file


@app.route('/start')
def start_mouse_mover():
    if pyautogui:
        pyautogui.moveTo(500, 500, duration=1)
        return jsonify({"status": "Mouse mover started!"})
    return jsonify({"status": "Running in headless mode. Mouse mover not available."})


@app.route('/stop')
def stop_mouse_mover():
    return jsonify({"status": "Mouse mover stopped!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
