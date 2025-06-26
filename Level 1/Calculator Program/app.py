from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify
import math

app = Flask(__name__)
app.secret_key = 'your-secret-key'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Scientific Calculator</title>
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
    .calculator {
      background-color: var(--card-color);
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      width: 350px;
    }
    .calculator h2 {
      text-align: center;
      margin-bottom: 1rem;
    }
    .calculator input, .calculator select, .calculator button {
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
    .input-group {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .input-group input {
      flex: 1;
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
      updateInputs();
    }

    function updateInputs() {
      const operator = document.querySelector('select[name="operator"]').value;
      const num1Input = document.querySelector('input[name="num1"]');
      const num2Input = document.querySelector('input[name="num2"]');
      const num2Div = num2Input.parentElement;

      if (['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln', 'sqrt', 'exp', 'fact', 'abs', 'square', 'pi', 'e'].includes(operator)) {
        num2Div.style.display = 'none';
        num1Input.placeholder = 'Enter number';
      } else {
        num2Div.style.display = 'block';
        num1Input.placeholder = 'Enter first number';
        num2Input.placeholder = 'Enter second number';
      }
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
<body id="page-body">
  <div class="calculator">
    <h2>Scientific Calculator</h2>
    <form method="POST" action="/">
      <div class="input-group">
        <input type="number" name="num1" step="any" placeholder="Enter first number" required />
      </div>
      <select name="operator" onchange="updateInputs()">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">×</option>
        <option value="/">/</option>
        <option value="%">%</option>
        <option value="power">x^y</option>
        <option value="sin">sin</option>
        <option value="cos">cos</option>
        <option value="tan">tan</option>
        <option value="asin">arcsin</option>
        <option value="acos">arccos</option>
        <option value="atan">arctan</option>
        <option value="log">log</option>
        <option value="ln">ln</option>
        <option value="sqrt">√</option>
        <option value="exp">e^x</option>
        <option value="fact">n!</option>
        <option value="abs">|x|</option>
        <option value="square">x²</option>
        <option value="pi">π</option>
        <option value="e">e</option>
      </select>
      <div class="input-group">
        <input type="number" name="num2" step="any" placeholder="Enter second number" />
      </div>
      <div class="buttons">
        <button type="submit">Calculate</button>
      </div>
    </form>
    <div class="buttons" style="margin-top: 0.5rem;">
      <button type="button" onclick="clearHistory()">Clear History</button>
    </div>

    {% if result is not none %}
      <div class="result">{{ expression }} = {{ result }}</div>
    {% endif %}

    <div class="history" id="history-container">
      <h4>Calculation History:</h4>
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
            document.getElementById('history-container').innerHTML = '<h4>Calculation History:</h4><ul></ul>';
          }
        });
    }
  </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = ""
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            operator = request.form['operator']
            num2 = request.form.get('num2')
            if num2 is not None:
                num2 = float(num2)

            # Binary operations
            if operator == '+':
                result = num1 + num2
                expression = f"{num1} + {num2}"
            elif operator == '-':
                result = num1 - num2
                expression = f"{num1} - {num2}"
            elif operator == '*':
                result = num1 * num2
                expression = f"{num1} × {num2}"
            elif operator == '/':
                result = 'Cannot divide by zero' if num2 == 0 else num1 / num2
                expression = f"{num1} / {num2}"
            elif operator == '%':
                result = num1 % num2
                expression = f"{num1} % {num2}"
            elif operator == 'power':
                result = math.pow(num1, num2)
                expression = f"{num1}^{num2}"

            # Unary operations
            elif operator == 'sin':
                result = math.sin(math.radians(num1)) if session.get('angle_mode', 'DEG') == 'DEG' else math.sin(num1)
                expression = f"sin({num1})"
            elif operator == 'cos':
                result = math.cos(math.radians(num1)) if session.get('angle_mode', 'DEG') == 'DEG' else math.cos(num1)
                expression = f"cos({num1})"
            elif operator == 'tan':
                result = math.tan(math.radians(num1)) if session.get('angle_mode', 'DEG') == 'DEG' else math.tan(num1)
                expression = f"tan({num1})"
            elif operator == 'asin':
                result = math.degrees(math.asin(num1)) if session.get('angle_mode', 'DEG') == 'DEG' else math.asin(num1)
                expression = f"arcsin({num1})"
            elif operator == 'acos':
                result = math.degrees(math.acos(num1)) if session.get('angle_mode', 'DEG') == 'DEG' else math.acos(num1)
                expression = f"arccos({num1})"
            elif operator == 'atan':
                result = math.degrees(math.atan(num1)) if session.get('angle_mode', 'DEG') == 'DEG' else math.atan(num1)
                expression = f"arctan({num1})"
            elif operator == 'log':
                result = math.log10(num1) if num1 > 0 else 'Invalid input'
                expression = f"log({num1})"
            elif operator == 'ln':
                result = math.log(num1) if num1 > 0 else 'Invalid input'
                expression = f"ln({num1})"
            elif operator == 'sqrt':
                result = math.sqrt(num1) if num1 >= 0 else 'Invalid input'
                expression = f"√({num1})"
            elif operator == 'exp':
                result = math.exp(num1)
                expression = f"e^{num1}"
            elif operator == 'fact':
                result = math.factorial(int(num1)) if num1 >= 0 and num1.is_integer() else 'Invalid input'
                expression = f"{int(num1)}!"
            elif operator == 'abs':
                result = abs(num1)
                expression = f"|{num1}|"
            elif operator == 'square':
                result = num1 ** 2
                expression = f"{num1}²"
            elif operator == 'pi':
                result = math.pi
                expression = "π"
            elif operator == 'e':
                result = math.e
                expression = "e"
            else:
                result = 'Invalid operator'

            if isinstance(result, (int, float)):
                result = round(result, 6)
                session['history'].append(f"{expression} = {result}")
            else:
                session['history'].append(f"{expression} = Error: {result}")

        except ValueError as e:
            result = 'Invalid input. Please enter numeric values.'
            session['history'].append(f"{expression} = Error: {result}")
        except Exception as e:
            result = f"Error: {str(e)}"
            session['history'].append(f"{expression} = Error: {result}")

    return render_template_string(HTML_TEMPLATE, result=result, expression=expression, history=session['history'])

@app.route('/clear', methods=['POST'])
def clear():
    session['history'] = []
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)