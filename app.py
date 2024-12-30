from flask import Flask, render_template
import pyautogui
import threading
import time

app = Flask(__name__)

mouse_active = False

def move_mouse():
    global mouse_active
    while mouse_active:
        pyautogui.moveRel(10, 0, duration=0.5)
        pyautogui.moveRel(-10, 0, duration=0.5)
        time.sleep(30)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start_mouse():
    global mouse_active
    if not mouse_active:
        mouse_active = True
        threading.Thread(target=move_mouse).start()
    return {"status": "Mouse Mover Started"}

@app.route("/stop")
def stop_mouse():
    global mouse_active
    mouse_active = False
    return {"status": "Mouse Mover Stopped"}

if __name__ == "__main__":
    app.run(debug=True)
