from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodoro Timer</title>
    <style>
        body {
            background-color: #f7f1e3;
            text-align: center;
            font-family: "Courier New", monospace;
            padding-top: 50px;
        }
        h1 {
            color: #e74c3c;
            font-size: 40px;
        }
        #timer {
            font-size: 48px;
            color: #2c3e50;
            margin: 20px;
        }
        #tomato {
            width: 200px;
            margin: 20px auto;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            background-color: #e67e22;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #d35400;
        }
        #session {
            margin-top: 20px;
            font-size: 20px;
            color: #27ae60;
        }
    </style>
</head>
<body>
    <h1>Pomodoro</h1>
    <img id="tomato" src="/image/tomato.png" alt="Tomato">
    <div id="timer">25:00</div>
    <button onclick="startTimer()">Start</button>
    <button onclick="resetTimer()">Reset</button>
    <div id="session"></div>

    <script>
        let workTime = 25 * 60;
        let breakTime = 5 * 60;
        let longBreak = 20 * 60;
        let reps = 0;
        let timeLeft = workTime;
        let timerInterval = null;

        function updateDisplay() {
            let minutes = Math.floor(timeLeft / 60);
            let seconds = timeLeft % 60;
            document.getElementById("timer").textContent =
                String(minutes).padStart(2, '0') + ":" + String(seconds).padStart(2, '0');
        }

        function startTimer() {
            reps++;
            if (reps % 8 === 0) {
                timeLeft = longBreak;
                document.querySelector("h1").textContent = "Long Break";
            } else if (reps % 2 === 0) {
                timeLeft = breakTime;
                document.querySelector("h1").textContent = "Break";
            } else {
                timeLeft = workTime;
                document.querySelector("h1").textContent = "Work";
            }

            clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateDisplay();
                } else {
                    clearInterval(timerInterval);
                    if (reps % 2 !== 0) {
                        document.getElementById("session").textContent += "✔";
                    }
                    startTimer();
                }
            }, 1000);
        }

        function resetTimer() {
            clearInterval(timerInterval);
            timerInterval = null;
            reps = 0;
            timeLeft = workTime;
            document.querySelector("h1").textContent = "Pomodoro";
            document.getElementById("session").textContent = "";
            updateDisplay();
        }

        updateDisplay();
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/image/<path:filename>")
def serve_image(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == "__main__":
    app.run(debug=True)