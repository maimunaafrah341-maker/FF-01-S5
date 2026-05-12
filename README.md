# FF-01-S5 — Smart Invoice Generator for Small Businesses

> Build Season 2026  
> Team: Fast & Curious

---

## 👥 Team Members

- Yusra Fatima — Team Lead
- Samreen Fatima
- Maimuna Afrah

---

## 🧾 Problem Statement

Many small businesses, freelancers, home bakeries, and local vendors still manage invoices manually using notebooks or spreadsheets. Existing invoicing platforms are often expensive, complicated, or overloaded with features unnecessary for small-scale businesses.

This creates problems like:
- Time-consuming invoice creation
- Manual calculation errors
- Poor record keeping
- Unprofessional billing formats

---

## 💡 Our Solution

FF-01-S5 is a lightweight web-based invoice generator designed specifically for small businesses and independent creators.

Users can:
- Enter client details
- Add multiple line items dynamically
- Automatically calculate totals and tax
- Generate professional PDF invoices instantly
- Store invoice history locally using SQLite

The platform focuses on simplicity, speed, and accessibility.

---

## ✨ Key Features

✅ Dynamic invoice form with live total calculation  
✅ Add/remove multiple line items instantly  
✅ Automatic tax computation  
✅ Professional PDF invoice generation using ReportLab  
✅ Invoice download support  
✅ Invoice history tracking with SQLite database  
✅ Clean responsive UI for desktop and mobile  
✅ Built using beginner-friendly open technologies

---

## 🛠 Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| Backend      | Python, Flask            |
| Frontend     | HTML, CSS, Vanilla JS    |
| PDF Engine   | ReportLab                |
| Database     | SQLite                   |
| Version Control | Git & GitHub         |

---

## 🚀 Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/maimunaafrah341-maker/FF-01-S5.git
cd FF-01-S5
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Flask Server

```bash
python app.py
```

### 4. Open in Browser

```text
http://localhost:5000
```

---

## 📁 Project Structure

```text
FF-01-S5/
│
├── app.py
├── generator.py
├── database.py
├── requirements.txt
├── README.md
├── invoices.db
│
├── invoices/
│
└── templates/
    ├── index.html
    ├── success.html
    └── history.html
```

---

## 🧠 Inspiration

This project was inspired by a real-world issue faced by *Noor & Nosh*, a home bakery connected to our team, where invoices were being tracked manually in notebooks.

We wanted to build a solution that feels:
- simple,
- affordable,
- beginner-friendly,
- and genuinely useful for small business owners.

---

## 🔮 Future Improvements

- GST-ready invoice formatting
- Email invoice directly to clients
- Cloud database integration
- Dashboard analytics
- Authentication system
- Razorpay / UPI payment integration
- Multi-theme invoice templates

---

## 🌟 Why This Project Matters

FF-01-S5 demonstrates how simple technology can solve real operational problems for small businesses.

Instead of building a complex enterprise platform, we focused on:
- usability,
- speed,
- accessibility,
- and practical impact.

---