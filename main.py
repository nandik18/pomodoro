from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodoro Timer</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; background: #fdf6e3; }
        h1 { color: #d35400; }
        #timer { font-size: 48px; margin: 20px; }
        button { padding: 10px 20px; font-size: 16px; margin: 5px; }
    </style>
</head>
<body>
    <h1>Pomodoro Timer</h1>
    <div id="timer">25:00</div>
    <button onclick="startTimer()">Start</button>
    <button onclick="resetTimer()">Reset</button>

    <script>
        let workTime = 25 * 60;
        let timeLeft = workTime;
        let timerInterval = null;

        function updateDisplay() {
            let minutes = Math.floor(timeLeft / 60);
            let seconds = timeLeft % 60;
            document.getElementById("timer").textContent =
                String(minutes).padStart(2, '0') + ":" + String(seconds).padStart(2, '0');
        }

        function startTimer() {
            if (timerInterval) return;
            timerInterval = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateDisplay();
                } else {
                    clearInterval(timerInterval);
                    timerInterval = null;
                    alert("Time's up!");
                }
            }, 1000);
        }

        function resetTimer() {
            clearInterval(timerInterval);
            timerInterval = null;
            timeLeft = workTime;
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

if __name__ == "__main__":
    app.run(debug=True)