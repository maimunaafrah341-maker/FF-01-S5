from flask import Flask, render_template, request, send_file, redirect, url_for
from generator import generate_invoice
from database import init_db, save_invoice, get_all_invoices
import os

app = Flask(__name__)
INVOICES_DIR = "invoices"
os.makedirs(INVOICES_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    client_name  = request.form.get("client_name")
    client_email = request.form.get("client_email")
    client_addr  = request.form.get("client_address")

    item_names  = request.form.getlist("item_name[]")
    item_qtys   = request.form.getlist("item_qty[]")
    item_prices = request.form.getlist("item_price[]")

    items = []
    for name, qty, price in zip(item_names, item_qtys, item_prices):
        if name.strip() and qty.strip() and price.strip():
            items.append({
                "name":  name,
                "qty":   int(qty),
                "price": float(price)
            })

    tax_rate = float(request.form.get("tax_rate", 0)) / 100
    notes    = request.form.get("notes", "")

    invoice_data = {
        "client_name":    client_name,
        "client_email":   client_email,
        "client_address": client_addr,
        "items":          items,
        "tax_rate":       tax_rate,
        "notes":          notes
    }

    invoice_id, filename, total = generate_invoice(invoice_data, INVOICES_DIR)
    save_invoice(invoice_id, client_name, total, filename)

    return redirect(url_for("success",
                            invoice_id=invoice_id,
                            filename=filename,
                            total=f"{total:.2f}"))

@app.route("/success")
def success():
    return render_template("success.html",
        invoice_id=request.args.get("invoice_id"),
        filename=request.args.get("filename"),
        total=request.args.get("total"))

@app.route("/download/<filename>")
def download(filename):
    path = os.path.join(INVOICES_DIR, filename)
    return send_file(path, as_attachment=True)

@app.route("/history")
def history():
    invoices = get_all_invoices()
    return render_template("history.html", invoices=invoices)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
