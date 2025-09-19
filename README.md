# README.md

# 📊 Loan Approval Predictor

A Machine Learning + Flask web application to predict whether a loan application will be **Approved** or **Rejected** based on applicant details such as income, credit history, dependents, and property area.

---

## 🚀 Features

* Simple and responsive frontend form.
* Prediction API built with Flask.
* Pre-trained ML model (`loan_model.pkl`).
* Clean UI with HTML, CSS, and JavaScript.

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **ML Model:** Scikit-learn (Joblib for model persistence)
* **Other:** Pandas, Flask-CORS

---

## 📂 Project Structure

```
Loan-approval-UI/
│
├── app.py                # Flask backend
├── loan_model.pkl        # Trained ML model (keep tracked if small)
├── requirements.txt      # Dependencies
├── .gitignore            # Ignored files
├── README.md             # Project description (this file)
├── LICENSE               # MIT license
├── templates/
│   └── index.html        # Frontend form (Flask requires this location)
└── static/               # (optional) CSS, JS, images
```

> ⚠️ Make sure `index.html` is inside `templates/` (Flask looks for templates there).

---

## ⚡ Setup Instructions (Local)

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/Loan-approval-UI.git
   cd Loan-approval-UI
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

   Visit: `http://127.0.0.1:5000/`

---

## 📌 API Endpoint

### `POST /predict`

* **Request Body (JSON)**

  ```json
  {
    "Gender": "Male",
    "Married": "Yes",
  ```

"Dependents": "1",
"Education": "Graduate",
"Self\_Employed": "No",
"ApplicantIncome": 6000,
"CoapplicantIncome": 2000,
"LoanAmount": 150,
"Loan\_Amount\_Term": 360,
"Credit\_History": 1,
"Property\_Area": "Urban"
}

````

- **Response**
```json
{
  "loan_status": "Approved"
}
````

---

## 📜 Notes

* If your `loan_model.pkl` is large, consider using Git LFS or storing it in a cloud bucket and loading it at runtime.
* Add `requirements.txt` and `.gitignore` before the first commit to avoid committing unwanted files.

---

## 📦 requirements.txt

```
Flask
flask-cors
pandas
joblib
scikit-learn
```

---

## 🚫 .gitignore

```
# Python
__pycache__/
*.pyc
*.pyo
*.pkl

# Virtual environments
.env
venv/
.venv/

# OS / IDE
.DS_Store
*.log
.idea/
.vscode/

# Secrets
.env
```

---

## 🔁 Git commands (create repo & push)

1. Create a GitHub repository at: `https://github.com/ishwarya-18/Loan-approval-UI` (or use your account)

2. Run these commands locally in the project root:

```bash
git init
git add .
git commit -m "Initial commit - Loan Approval Predictor"
git branch -M main
git remote add origin https://github.com/<your-username>/Loan-approval-UI.git
git push -u origin main
```

(Replace `<your-username>` with your GitHub username.)

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Developed by **Aishwarya**
