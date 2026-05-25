# FF-01-S5 — Automated Invoice Generator for Small Businesses

<div align="center">

![Build Season](https://img.shields.io/badge/Build%20Season-2026-1a1a6e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ecc71?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-1a1a6e?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-2ecc71?style=for-the-badge&logo=flask&logoColor=white)
![SDG](https://img.shields.io/badge/UN%20SDG-Goal%208%20%26%209-1a1a6e?style=for-the-badge)

**"Professional invoices in seconds — built for the businesses that keep cities running."**

Team Fast & Curious · Stanley College of Engineering, Hyderabad · First-Year AIML

</div>

---

## Team

| Name | Role |
|------|------|
| Yusra Fatima | Team Lead |
| Maimuna Afrah | Full-Stack Developer |
| Samreen Fatima | Research & Documentation |

---

## Product Overview

FF-01-S5 is a lightweight, web-based invoice generator built for small businesses, freelancers, home bakeries, and independent vendors who need professional billing without the cost or complexity of enterprise software.

Users fill in client details, add line items dynamically, and receive a professionally formatted PDF invoice within seconds. All invoice records are stored locally using SQLite for future reference.

### The Problem

Millions of small business owners — from local tailors to home bakers — still track invoices in notebooks or WhatsApp messages. Existing invoicing tools are either expensive, overly complex, or require constant internet connectivity. This results in:

- Time-consuming manual billing
- Calculation errors that cost money
- Poor record-keeping and lost payment history
- Unprofessional documents that undermine credibility

### Real-World Inspiration

This project was directly inspired by **Noor & Nosh**, a home bakery connected to our team, where all orders and billing were managed through handwritten notes. FF-01-S5 was built to solve exactly that problem.

---

## UN SDG Alignment

**Goal 8 — Decent Work & Economic Growth**
FF-01-S5 empowers micro and small enterprises to operate more efficiently. Automating the billing process saves time, reduces errors, and helps small business owners present a more professional image — directly supporting productivity and income growth at the grassroots level.

**Goal 9 — Industry, Innovation & Infrastructure**
Built entirely using open-source, beginner-accessible technologies, FF-01-S5 demonstrates how lightweight digital infrastructure can modernise small-scale industry without requiring expensive tools or cloud services.

---

## Key Features

| Feature | Description |
|---------|-------------|
| Dynamic Invoice Form | Add and remove line items in real time |
| Live Total Calculation | Subtotal, tax, and grand total update as you type |
| PDF Generation | Professional invoices generated via ReportLab |
| Auto-Download | Invoice downloads automatically on generation |
| Print Support | Direct Print / Open PDF button on the success page |
| Countdown Timer | Visual feedback with auto-redirect after generation |
| Invoice History | All records stored and viewable via SQLite |
| Input Validation | Three-layer validation — frontend, backend, database |
| Responsive UI | Two-column layout works across desktop and mobile |

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend | Python 3, Flask | Server logic, routing, PDF trigger |
| Frontend | HTML5, CSS3, Vanilla JS | UI, live calculations, form validation |
| PDF Engine | ReportLab | Programmatic PDF invoice generation |
| Database | SQLite | Local invoice history storage |
| Version Control | Git & GitHub | Collaboration and source management |

---

## System Architecture

```
+------------------------------------------------------------------+
|                         CLIENT BROWSER                          |
|                                                                  |
|   index.html — Two-Column Invoice Form                          |
|   Left panel  : Client info, line items, tax, notes             |
|   Right panel : Live sidebar — real-time total preview          |
|   JavaScript  : Dynamic row add/remove + live calculation       |
+----------------------------+-------------------------------------+
                             |
                        HTTP POST /generate
                             |
+----------------------------v-------------------------------------+
|                      FLASK SERVER  (app.py)                     |
|   - Receives and validates form data                            |
|   - try/except around PDF generation and database save          |
+----------------+----------------------------+-------------------+
                 |                            |
                 v                            v
+----------------+----------+   +------------+--------------------+
|   generator.py            |   |   database.py                   |
|   ReportLab PDF Engine    |   |   SQLite Interface              |
|                           |   |                                 |
|   _build_header()         |   |   init_db()       try/finally   |
|   _build_client_info()    |   |   save_invoice()  try/finally   |
|   _build_items_table()    |   |   fetch_invoices() try/finally  |
|   _build_notes()          |   +------------+--------------------+
|   _build_footer()         |                |
+----------+----------------+                v
           |                        +--------+--------+
           v                        |   invoices.db   |
   +-------+--------+               |   (SQLite DB)   |
   |   /invoices/   |               +-----------------+
   |   *.pdf files  |
   +-------+--------+
           |
           v
+------------------------------------------------------------------+
|   success.html                                                   |
|   - Countdown timer → auto-download PDF                         |
|   - Print / Open PDF button  (addressed judge feedback)         |
|   - Link to invoice history                                      |
+------------------------------------------------------------------+
```

---

## Application Screenshots

### Invoice Form — Empty State
The two-column layout with the live invoice summary sidebar on the right.

![Invoice Form Empty](screenshots/form-empty.png)

---

### Invoice Form — Filled with Live Preview
Live sidebar updates in real time as items and quantities are entered. Shown here with a Noor & Nosh order.

![Invoice Form Filled](screenshots/form-filled.png)

---

### Success Page — Invoice Generated
After submission, the success page displays the Invoice ID, total amount, and a Download PDF button. The PDF also auto-downloads via a countdown timer.

![Success Page](screenshots/success.png)

---

## Installation Guide

### Prerequisites

- Python 3.8 or higher
- pip
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

`requirements.txt` includes:
```
flask
reportlab
```

### Step 3 — Run the Application

```bash
python app.py
```

Expected output:
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
2. Add line items — description, quantity, unit price
3. Set the tax percentage
4. Click **Generate Invoice**
5. PDF auto-downloads to your device

---

## Project Structure

```
FF-01-S5/
|
+-- app.py              Flask routes, input validation, error handling
+-- generator.py        ReportLab PDF engine — 5 modular functions
+-- database.py         SQLite init, save, fetch with try/except/finally
+-- requirements.txt    Python dependencies
+-- README.md
|
+-- templates/
|   +-- index.html      Two-column invoice form with live sidebar
|   +-- success.html    Countdown timer, auto-download, print button
|   +-- history.html    Invoice history view
|
+-- invoices/           Generated PDF invoices stored here
```

---

## Code Architecture

### Modular PDF Generation

The PDF engine was refactored in Week 3 from a single 150+ line monolithic function into five focused helper functions, each responsible for one section of the invoice:

```python
def _build_header(canvas, doc, data)        # Business name, invoice number, date
def _build_client_info(canvas, doc, data)   # Bill-to section
def _build_items_table(canvas, doc, items)  # Line items with qty, rate, amount
def _build_notes(canvas, doc, notes)        # Optional notes and terms
def _build_footer(canvas, doc, totals)      # Subtotal, tax, grand total
```

Styles are defined once at the module level and shared across all functions.

### Three-Layer Error Handling

```
Layer 1 — Frontend (index.html)
  required, min, step HTML attributes block invalid input before submission

Layer 2 — Backend (app.py)
  try/except around PDF generation and database save

Layer 3 — Database (database.py)
  try/except/finally on all three functions — connection always closes cleanly
```

---

## Testing & Edge Cases

| Scenario | How It Is Handled |
|----------|------------------|
| Empty required fields | Frontend `required` attribute blocks submission |
| Negative quantity or price | `min="0"` and `step` attributes enforce valid input |
| PDF generation failure | `try/except` in `app.py` catches ReportLab errors |
| Database write failure | `try/except/finally` ensures connection closes cleanly |
| Missing line items | Backend validates at least one item is present |

---

## Build Journey

| Week | Deliverables |
|------|-------------|
| Week 1 | Problem statement, tech stack justification, architecture diagram |
| Week 2 | GitHub setup, two-column UI with live sidebar, ReportLab PDF generation, demo video |
| Week 3 | Three-layer error handling, generator refactored into 5 modules, auto-download and print button added |
| Week 4 | Repository cleaned, full documentation, README completed |

---

## Future Improvements

- GST-ready invoice formatting with CGST/SGST breakdown
- Email invoice directly to client via SMTP
- Cloud database integration
- Dashboard analytics — revenue tracking and client insights
- User authentication
- Razorpay and UPI payment link integration
- Multi-theme invoice templates

---

## Why This Project Matters

FF-01-S5 is not just a student project — it is a working solution to a real problem faced by real businesses in our community. The goal was never complexity. It was impact.

> Simple technology. Real problems. Genuine solutions.

---

<div align="center">

**Fast & Curious** · Build Season 2026 · Stanley College of Engineering, Hyderabad

</div>
