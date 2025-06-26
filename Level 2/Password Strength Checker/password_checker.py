from flask import Flask, render_template_string, request, session
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Password Strength Checker</title>
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
    .checker {
      background-color: var(--card-color);
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      width: 350px;
    }
    .checker h2 {
      text-align: center;
      margin-bottom: 1rem;
    }
    .checker input, .checker button {
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
    .details {
      margin-top: 0.5rem;
      font-size: 0.9rem;
      color: var(--text-color);
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
  <div class="checker">
    <h2>Password Strength Checker</h2>
    <p>Enter a password to check its strength:</p>
    <form method="POST" action="/">
      <input type="text" name="password" placeholder="Enter your password" required />
      <div class="buttons">
        <button type="submit">Check Strength</button>
      </div>
    </form>
    <div class="buttons" style="margin-top: 0.5rem;">
      <button type="button" onclick="clearHistory()">Clear History</button>
    </div>

    {% if result is not none %}
      <div class="result">Strength: {{ result }}</div>
      <div class="details">{{ details }}</div>
    {% endif %}

    <div class="history" id="history-container">
      <h4>Password History:</h4>
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
            document.getElementById('history-container').innerHTML = '<h4>Password History:</h4><ul></ul>';
          }
        });
    }
  </script>
</body>
</html>
'''

def check_password_strength(password):
    # Initialize checks
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Count the number of criteria met
    criteria_met = sum([length >= 8, has_upper, has_lower, has_digit, has_special])
    details = []

    # Add details about each criterion
    details.append(f"Length: {length} (Minimum 8 required)")
    details.append(f"Uppercase letters: {'Yes' if has_upper else 'No'}")
    details.append(f"Lowercase letters: {'Yes' if has_lower else 'No'}")
    details.append(f"Digits: {'Yes' if has_digit else 'No'}")
    details.append(f"Special characters: {'Yes' if has_special else 'No'}")

    # Determine strength
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif criteria_met >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, "; ".join(details)

@app.route('/', methods=['GET', 'POST'])
def password_checker():
    # Initialize session variables if not present
    if 'history' not in session:
        session['history'] = []

    result = None
    details = None

    if request.method == 'POST':
        password = request.form['password']
        strength, details = check_password_strength(password)
        result = strength

        # Mask the password for display in history (show only first and last character)
        if len(password) > 2:
            masked_password = f"{password[0]}{'*' * (len(password) - 2)}{password[-1]}"
        else:
            masked_password = password

        session['history'].append(f"Password: {masked_password} - Strength: {strength}")
        session.modified = True

    return render_template_string(
        HTML_TEMPLATE,
        result=result,
        details=details,
        history=session['history']
    )

@app.route('/clear', methods=['POST'])
def clear():
    session['history'] = []
    session.modified = True
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)