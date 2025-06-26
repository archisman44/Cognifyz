# 📧 Email Validator - Cognifyz Level 1 Task 3

This project is a Python program developed as part of **Level 1 - Task 3** for the Cognifyz internship program. The task is to build an **Email Validator** that checks if a given string is a valid email address based on standard email format rules.

---

## 🔍 Task Objective

> **Develop a Python function that validates whether a given string is a valid email address.**  
> The function should:
> - Check for the presence of an "@" symbol  
> - Ensure a domain name exists  
> - Reject email addresses with invalid characters or formats (like double dots, missing domain, etc.)

---

## 📁 File Structure

```
Email Validator/
│
├── app.py         # Main application file
└── README.md      # Project documentation (this file)
```

---

## 🧠 Logic Used

- Validates email using Python's `re` (regular expressions) module  
- Includes an **additional check** to reject email addresses with `..` (double dots)  
- Uses a loop to allow multiple email inputs until the user types `exit`

---

## 💻 How to Run

1. Make sure you have Python installed.
2. Open the terminal in VS Code in the project directory.
3. Run the following command:

```bash
python app.py
```

4. You will be prompted to enter email addresses one by one.

---

## ✅ Sample Output

```
📧 Email Validator Program (type 'exit' to quit)

Enter an email address: archi@gmail.com
✅ 'archi@gmail.com' is a valid email address.

Enter an email address: archi@gmaill..com
❌ 'archi@gmaill..com' is NOT a valid email address.

Enter an email address: exit
👋 Exiting...
```

---

## 🧪 Tech Used

- Python 3
- Regular Expressions (`re` module)

---

## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 1  
- **Task:** 3 - Email Validator

---
