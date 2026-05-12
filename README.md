# FF-01-S5 — Automated Invoice Generator for Small Businesses

> Build Season 2026 | Team: Fast and Curious

## 👥 Team Members
- Yusra Fatima (Team Lead)
- Samreen Fatima
- Maimuna Afrah

## 🧾 About
FF-01-S5 is a web-based invoice generator built for small business owners
(like home bakeries, freelancers, and local vendors) who need fast, clean,
professional PDFs without paying for software.

## ✨ Features
- Fill a simple form: client name, line items, tax rate
- Auto-generates a professional PDF invoice using ReportLab
- Saves invoice records to a local SQLite database
- Download PDF instantly after generation
- View invoice history

## 🛠 Tech Stack
| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Flask           |
| PDF Engine | ReportLab               |
| Database   | SQLite                  |
| Frontend   | HTML, CSS, Vanilla JS   |

## 🚀 Run Locally
```bash
pip install -r requirements.txt
python app.py
```
Then open http://localhost:5000

## 📁 Structure
```
FF-01-S5/
├── app.py
├── generator.py
├── database.py
├── templates/
│   ├── index.html
│   └── success.html
├── static/style.css
├── invoices/
└── requirements.txt
```

## 💡 Inspiration
Built from a real pain point — Noor & Nosh, our member's home bakery,
was tracking invoices manually in a notebook. No more.
