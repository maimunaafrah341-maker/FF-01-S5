# FF-01-S5 — Automated Invoice Generator for Small Businesses

<div align="center">

![Build Season](https://img.shields.io/badge/Build%20Season-2026-1a1a6e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ecc71?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-1a1a6e?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-2ecc71?style=for-the-badge&logo=flask&logoColor=white)
![SDG](https://img.shields.io/badge/UN%20SDG-Goal%208%20%26%209-1a1a6e?style=for-the-badge)

**"Professional invoices in seconds — built for the micro-businesses that keep our cities running."**

Team Fast & Curious · Stanley College of Engineering, Hyderabad · First-Year AIML

</div>

---

## 👥 Team

| Name | Role |
|------|------|
| **Yusra Fatima** | Team Lead |
| **Maimuna Afrah** | Full-Stack Developer |
| **Samreen Fatima** | Research & Documentation |

---

## 🎯 Product Overview

**FF-01-S5** is a lightweight, offline-first web application engineered for small businesses, freelancers, home bakeries, and independent vendors who require professional billing infrastructure without the financial burden or complexity of enterprise software.

Users input client metrics, append transactional line items dynamically, and receive a beautifully formatted, print-ready PDF invoice instantly. 

### ⚠️ The Problem
Millions of grassroots micro-enterprises manage their accounts using handwritten paper logs or fragmented WhatsApp messages. Standard corporate billing platforms are either cost-prohibitive, structurally complex, or entirely dependent on cloud connectivity. This friction introduces critical vulnerabilities:
* **Operational Inefficiency:** Hours lost to manual document generation.
* **Financial Risk:** Human mathematical slip-ups that leak revenue.
* **Poor Record-Keeping:** Decentralized files lead to lost payment and tax histories.
* **Credibility Loss:** Hand-drafted receipts undermine professional client trust.

### 💡 Real-World Inspiration
This system wasn't built in a vacuum. It was explicitly inspired by **Noor & Nosh**, a local home bakery closely connected to our team. Watching them grapple with chaotic paper invoice trails and manually calculated totals drove us to engineer a clean digital ecosystem to optimize their daily workflows.

---

## 🌿 UN SDG Alignment

* **Goal 8: Decent Work & Economic Growth** FF-01-S5 formalizes and digitalizes backend logistics for micro-enterprises. By eliminating structural invoicing bottlenecks, it scales productivity and safeguards transaction integrity at the community level.
* **Goal 9: Industry, Innovation & Infrastructure** Leveraging lightweight, open-source tech stacks, this project models how local industries can implement resilient digital tools without heavy capital investments or enterprise cloud dependence.

---

## ⚡ Key Features

| Feature | Technical Implementation |
|:---|:---|
| **Dynamic Invoice Staging** | Add, configure, or eliminate transaction items instantly with zero page reloads. |
| **Live Ledger Engines** | Algorithmic tracking of subtotal, custom tax scaling, and grand totals updates natively as you type. |
| **Programmatic PDF Compositor** | Custom drawing layout calculations generated cleanly via ReportLab backend. |
| **Zero-Click Delivery** | Integrated JS countdown mechanism pushes an instantaneous document stream download upon validation. |
| **Hardware Print Utility** | Dedicated direct-to-print engine handling on the success portal to streamline physical routing. |
| **Local Storage Architecture** | Continuous transaction logging via localized relational SQLite data tables. |
| **3-Layer Secure Guard** | Cascade form checking applied seamlessly at client view, routing controller, and schema level. |

---

## 🛠️ Tech Stack

| Layer | Component | Functional Domain |
|:---|:---|:---|
| **Backend** | Python 3 / Flask | Application architecture routing, payload checking, and core processing |
| **Frontend** | HTML5 / CSS3 / Vanilla JS | Responsive UI presentation layer and dynamic client calculations |
| **PDF Engine** | ReportLab Compositor | Dynamic structural design mapping and document compiling |
| **Database** | SQLite Relational Data | Persistent local session history logs |
| **Source Control** | Git / GitHub | Codebase management and release versioning |

---

## 📐 System Architecture

An overview of data transformation across the application layers:

<div align="center">

<img src="architecture.png" alt="System Architecture" width="500">

</div>

---

## 📱 Application Journey

### 1. Invoice Form — State Presentation
A balanced two-column user interface engineered with a fixed dynamic live calculating preview card positioned on the right panel.

![Invoice Form Empty](screenshots/form-empty.png)

### 2. Live Data Validation & State Execution
Real-time pricing models adjusting dynamically to input changes. Featured below executing an order tracking payload for the **Noor & Nosh** bakery workflow.

![Invoice Form Filled](screenshots/form-filled.png)

### 3. Automated Document Generation Success
Following validation, the receipt engine passes transactional metrics to database storage, rendering unique identifiers along with automated client document downloads.

![Success Page](screenshots/success.png)

---

## ⚙️ Installation & Deployment

### Prerequisites
* Python 3.8+ installed local environment
* `pip` packaging manager tool
* Git engine configuration

### Step 1: Clone the Working Core
```bash
git clone [https://github.com/maimunaafrah341-maker/FF-01-S5.git](https://github.com/maimunaafrah341-maker/FF-01-S5.git)
cd FF-01-S5