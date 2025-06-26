from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Fibonacci Sequence Generator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-color);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      transition: background-color 0.3s, color 0.3s;
    }
    .generator {
      background-color: var(--card-color);
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      width: 350px;
    }
    .generator h2 {
      text-align: center;
      margin-bottom: 1rem;
    }
    .generator input, .generator button {
      width: 100%;
      padding: 0.6rem;
      margin: 0.5rem 0;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 1rem;
    }
    .result {
      margin-top: 1rem;
      text-align: center;
      font-weight: bold;
      font-size: 1.2rem;
      color: var(--accent-color);
    }
    .history {
      margin-top: 1rem;
      font-size: 0.95rem;
      background-color: var(--history-bg);
      border: 1px solid var(--history-border);
      padding: 0.5rem;
      border-radius: 5px;
    }
    .history h4 {
      margin: 0 0 0.5rem;
      font-size: 1rem;
    }
    .history ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .history li {
      padding: 2px 0;
      border-bottom: 1px solid var(--history-border);
    }
    .buttons {
      display: flex;
      justify-content: space-between;
    }
    .buttons button {
      width: 48%;
    }
    .theme-toggle {
      text-align: center;
      margin-top: 1rem;
    }
  </style>
  <script>
    function toggleTheme() {
      const current = localStorage.getItem('theme') || 'light';
      const next = current === 'light' ? 'dark' : 'light';
      localStorage.setItem('theme', next);
      setTheme(next);
    }

    function setTheme(mode) {
      const root = document.documentElement;
      if (mode === 'dark') {
        root.style.setProperty('--bg-color', '#1f2937');
        root.style.setProperty('--text-color', '#f9fafb');
        root.style.setProperty('--card-color', '#374151');
        root.style.setProperty('--accent-color', '#10b981');
        root.style.setProperty('--history-bg', '#4b5563');
        root.style.setProperty('--history-border', '#6b7280');
      } else {
        root.style.setProperty('--bg-color', 'white');
        root.style.setProperty('--text-color', 'black');
        root.style.setProperty('--card-color', '#ffffff');
        root.style.setProperty('--accent-color', '#1f2937');
        root.style.setProperty('--history-bg', '#f9fafb');
        root.style.setProperty('--history-border', '#d1d5db');
      }
    }

    window.onload = () => {
      const savedTheme = localStorage.getItem('theme') || 'light';
      setTheme(savedTheme);
    }
  </script>
  <style>
    :root {
      --bg-color: white;
      --text-color: black;
      --card-color: #ffffff;
      --accent-color: #1f2937;
      --history-bg: #f9fafb;
      --history-border: #d1d5db;
    }
  </style>
</head>
<body>
  <div class="generator">
    <h2>Fibonacci Sequence Generator</h2>
    <p>Enter the number of terms:</p>
    <form method="POST" action="/">
      <input type="number" name="terms" min="1" placeholder="Enter number of terms" required />
      <div class="buttons">
        <button type="submit">Generate Sequence</button>
      </div>
    </form>
    <div class="buttons" style="margin-top: 0.5rem;">
      <button type="button" onclick="clearHistory()">Clear History</button>
    </div>

    {% if sequence is not none %}
      <div class="result">Fibonacci Sequence: {{ sequence }}</div>
    {% endif %}
    {% if error is not none %}
      <div class="result" style="color: red;">{{ error }}</div>
    {% endif %}

    <div class="history" id="history-container">
      <h4>History:</h4>
      <ul>
        {% for item in history %}
          <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>

    <div class="theme-toggle">
      <button onclick="toggleTheme()">Toggle Theme</button>
    </div>
  </div>

  <script>
    function clearHistory() {
      fetch('/clear', { method: 'POST' })
        .then(response => {
          if (response.ok) {
            document.getElementById('history-container').innerHTML = '<h4>History:</h4><ul></ul>';
          }
        });
    }
  </script>
</body>
</html>
'''

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

@app.route('/', methods=['GET', 'POST'])
def fibonacci_generator():
    # Initialize session variables if not present
    if 'history' not in session:
        session['history'] = []

    sequence = None
    error = None

    if request.method == 'POST':
        try:
            terms = int(request.form['terms'])
            if terms <= 0:
                error = "Please enter a positive number of terms."
                session['history'].append(f"Error: {error}")
            else:
                sequence = generate_fibonacci(terms)
                session['history'].append(f"Terms: {terms} - Sequence: {sequence}")
        except ValueError:
            error = "Please enter a valid integer."
            session['history'].append(f"Error: {error}")

        session.modified = True

    return render_template_string(
        HTML_TEMPLATE,
        sequence=sequence,
        error=error,
        history=session['history']
    )

@app.route('/clear', methods=['POST'])
def clear():
    session['history'] = []
    session.modified = True
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)