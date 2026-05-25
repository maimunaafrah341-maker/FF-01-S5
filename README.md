# FF-01-S5 — Automated Invoice Generator for Small Businesses

<div align="center">

![Build Season](https://img.shields.io/badge/Build%20Season-2026-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![SDG](https://img.shields.io/badge/UN%20SDG-Goal%208%20%26%209-orange?style=for-the-badge)

> **"Professional invoices in seconds — built for the businesses that keep cities running."**

**Team Fast & Curious** · Stanley College of Engineering, Hyderabad · First-Year AIML

</div>

---

## 👥 Team

| Name | Role |
|------|------|
| Yusra Fatima | Team Lead |
| Maimuna Afrah | Full-Stack Developer |
| Samreen Fatima | Research & Documentation |

---

## 📌 Product Overview

### What is FF-01-S5?

FF-01-S5 is a **lightweight, web-based invoice generator** built specifically for small businesses, freelancers, home bakeries, and independent vendors who need professional billing without the cost or complexity of enterprise software.

Users can fill in client details, add line items dynamically, and receive a professionally formatted PDF invoice — all within seconds. Invoice records are stored locally using SQLite for future reference.

### The Problem We're Solving

Millions of small business owners — from local tailors to home bakers — still track invoices in notebooks or informal WhatsApp messages. Existing invoicing tools are either expensive subscriptions, overly complex, or require internet connectivity. This leads to:

- ⏱ Time-consuming manual billing
- 🧮 Calculation errors that cost money
- 📂 Poor record-keeping and lost payment history
- 📄 Unprofessional documents that undermine credibility

### Real-World Inspiration

This project was directly inspired by **Noor & Nosh**, a home bakery connected to our team, where orders and billing were managed entirely through handwritten notes. FF-01-S5 was built to solve exactly that.

---

## 🌍 UN SDG Global Impact Alignment

This project contributes to two United Nations Sustainable Development Goals:

### 🏭 SDG Goal 8 — Decent Work & Economic Growth
FF-01-S5 empowers micro and small enterprises to operate more efficiently. By automating the billing process, business owners save time, reduce errors, and present a more professional image — directly supporting economic productivity and income growth at the grassroots level.

### ⚙️ SDG Goal 9 — Industry, Innovation & Infrastructure
Built entirely using open-source, beginner-accessible technologies (Python, Flask, ReportLab, SQLite), FF-01-S5 demonstrates how lightweight digital infrastructure can modernize small-scale industry without requiring expensive tools or cloud services.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🧾 Dynamic Invoice Form | Add/remove multiple line items in real time |
| 🔢 Live Total Calculation | Subtotal, tax, and grand total update as you type |
| 📄 PDF Generation | Professional invoices via ReportLab |
| ⬇️ Auto-Download | Invoice downloads automatically on generation |
| 🖨️ Print Support | Direct Print/Open PDF button on success page |
| 🕒 Countdown Timer | Visual feedback with auto-redirect after generation |
| 📚 Invoice History | All records stored and viewable via SQLite |
| ✅ Input Validation | Frontend + backend validation prevents bad data |
| 📱 Responsive UI | Two-column layout works on desktop and mobile |

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python 3, Flask | Server logic, routing, PDF trigger |
| **Frontend** | HTML5, CSS3, Vanilla JS | UI, live calculations, form validation |
| **PDF Engine** | ReportLab | Programmatic PDF invoice generation |
| **Database** | SQLite | Local invoice history storage |
| **Version Control** | Git & GitHub | Collaboration and code management |

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT BROWSER                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  index.html — Two-Column Invoice Form                    │   │
│  │  • Left: Input fields (client info, line items)          │   │
│  │  • Right: Live sidebar (real-time total preview)         │   │
│  │  • JS: Dynamic row add/remove + live tax calculation     │   │
│  └───────────────────────┬──────────────────────────────────┘   │
└──────────────────────────┼──────────────────────────────────────┘
                           │  HTTP POST /generate
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        FLASK SERVER (app.py)                    │
│  • Receives form data                                            │
│  • Input validation (required fields, numeric checks)           │
│  • try/except around PDF generation + DB save                   │
└────────────────┬────────────────────┬───────────────────────────┘
                 │                    │
                 ▼                    ▼
┌───────────────────────┐  ┌─────────────────────────────────────┐
│   generator.py        │  │   database.py                       │
│   PDF Engine          │  │   SQLite Interface                  │
│                       │  │                                     │
│  _build_header()      │  │  init_db()      — try/except/finally│
│  _build_client_info() │  │  save_invoice() — try/except/finally│
│  _build_items_table() │  │  fetch_invoices()— try/except/finally│
│  _build_notes()       │  └────────────────────┬────────────────┘
│  _build_footer()      │                       │
└──────────┬────────────┘                       ▼
           │                         ┌─────────────────┐
           ▼                         │   invoices.db   │
   ┌───────────────┐                 │   (SQLite DB)   │
   │  /invoices/   │                 └─────────────────┘
   │  *.pdf files  │
   └───────┬───────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────────┐
│  success.html                                                   │
│  • Countdown timer → auto-download PDF                          │
│  • Print / Open PDF button (addresses judge feedback)           │
│  • View Invoice History link                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation Guide

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/maimunaafrah341-maker/FF-01-S5.git
cd FF-01-S5
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
```
flask
reportlab
```

### Step 3 — Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 4 — Open in Browser

```
http://localhost:5000
```

### Step 5 — Generate Your First Invoice

1. Fill in your business name and client details
2. Add line items (description, quantity, unit price)
3. Set tax percentage
4. Click **Generate Invoice**
5. PDF auto-downloads to your device ✅

---

## 📁 Project Structure

```
FF-01-S5/
│
├── app.py              ← Flask routes, input validation, error handling
├── generator.py        ← ReportLab PDF engine (5 modular functions)
├── database.py         ← SQLite init, save, fetch with try/except/finally
├── requirements.txt    ← Python dependencies
├── README.md           ← You are here
│
├── templates/
│   ├── index.html      ← Two-column invoice form + live sidebar
│   ├── success.html    ← Countdown timer + auto-download + print button
│   └── history.html    ← Invoice history view
│
└── invoices/           ← Generated PDF invoices stored here
```

---

## 🧱 Code Architecture — Key Design Decisions

### Modular PDF Generation (`generator.py`)

The PDF engine was refactored from a single 150+ line monolithic function into **5 focused helper functions**, each responsible for one section of the invoice:

```python
# Week 3 refactor — modular generator
def _build_header(canvas, doc, data):
    """Renders business name, logo area, invoice number, date"""

def _build_client_info(canvas, doc, data):
    """Renders bill-to section with client name and address"""

def _build_items_table(canvas, doc, items):
    """Renders the line items table with qty, rate, amount columns"""

def _build_notes(canvas, doc, notes):
    """Renders optional notes/terms section"""

def _build_footer(canvas, doc, totals):
    """Renders subtotal, tax, and grand total"""
```

Styles are defined once at the module level and reused across all functions — no repetition.

### Three-Layer Error Handling

```
Frontend (index.html)     →  required / min / step HTML attributes
Backend (app.py)          →  try/except around generate + DB save
Database (database.py)    →  try/except/finally on all 3 DB functions
```

This ensures the app never crashes on unexpected input and always cleans up database connections.

---

## 🧪 Testing & Edge Cases Handled

| Scenario | How It's Handled |
|----------|-----------------|
| Empty required fields | Frontend `required` attribute blocks submission |
| Negative quantity/price | `min="0"` and `step` attributes enforce valid numbers |
| PDF generation failure | `try/except` in `app.py` catches ReportLab errors |
| Database write failure | `try/except/finally` ensures connection closes cleanly |
| Missing line items | Backend validates at least one item exists |

---

## 🔄 Build Journey — Week by Week

| Week | Milestones |
|------|-----------|
| **Week 1** | Problem statement defined, tech stack justified, architecture diagram created |
| **Week 2** | GitHub live, two-column UI with live sidebar built, ReportLab PDF generation working |
| **Week 3** | Full error handling (3 layers), generator refactored into 5 modules, auto-download + print button added |
| **Week 4** | Repository cleaned, documentation completed, README finalized |

---

## 🔮 Future Improvements

- 🇮🇳 GST-ready invoice formatting (CGST/SGST breakdown)
- 📧 Email invoice directly to client via SMTP
- ☁️ Cloud database (PostgreSQL / Firebase)
- 📊 Dashboard analytics — revenue tracking, top clients
- 🔐 User authentication system
- 💳 Razorpay / UPI payment link integration
- 🎨 Multi-theme invoice templates

---

## 🌟 Why This Project Matters

FF-01-S5 is not just a student project — it's a working solution to a real problem faced by real businesses in our community. We didn't build for complexity; we built for impact.

> **Simple technology. Real problems. Genuine solutions.**

---

<div align="center">

**Fast & Curious** · Build Season 2026 · Stanley College of Engineering, Hyderabad

*First-Year AIML · FF-01-S5*

</div>
