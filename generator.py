from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                 Paragraph, Spacer, HRFlowable)
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from datetime import datetime
import uuid, os

ACCENT    = colors.HexColor("#3c3879")
DARK      = colors.HexColor("#1e1b4b")
LIGHT_BG  = colors.HexColor("#f5f3ff")
GRAY      = colors.HexColor("#6b7280")
WHITE     = colors.white

def _style(name, **kw):
    return ParagraphStyle(name, **kw)

def generate_invoice(data, output_dir):
    invoice_id = f"INV-{datetime.now().strftime('%Y%m')}-{str(uuid.uuid4())[:6].upper()}"
    filename   = f"{invoice_id}.pdf"
    filepath   = os.path.join(output_dir, filename)

    doc = SimpleDocTemplate(filepath, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm,  bottomMargin=2*cm)
    story = []

    # ── Header ────────────────────────────────────────────────
    hdr = [
        [Paragraph("FF-01-S5",
                   _style("h1", fontSize=26, fontName="Helvetica-Bold",
                          textColor=ACCENT)),
         Paragraph("INVOICE",
                   _style("inv", fontSize=22, fontName="Helvetica-Bold",
                          textColor=DARK, alignment=TA_RIGHT))],
        [Paragraph("Automated Invoice Generator",
                   _style("sub", fontSize=9, fontName="Helvetica",
                          textColor=GRAY)),
         Paragraph(invoice_id,
                   _style("iid", fontSize=9, fontName="Helvetica",
                          textColor=GRAY, alignment=TA_RIGHT))]
    ]
    t = Table(hdr, colWidths=[9*cm, 8*cm])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    story += [t, HRFlowable(width="100%", thickness=2,
                             color=ACCENT, spaceAfter=10)]

    # ── Bill-to + Date ─────────────────────────────────────────
    date_str = datetime.now().strftime("%B %d, %Y")
    bill = [
        [Paragraph("Bill To:",
                   _style("bt", fontSize=10, fontName="Helvetica-Bold",
                          textColor=DARK)),
         Paragraph("Invoice Date:",
                   _style("id_", fontSize=10, fontName="Helvetica-Bold",
                          textColor=DARK, alignment=TA_RIGHT))],
        [Paragraph(data["client_name"],
                   _style("cn", fontSize=11, fontName="Helvetica",
                          textColor=DARK)),
         Paragraph(date_str,
                   _style("ds", fontSize=10, fontName="Helvetica",
                          textColor=GRAY, alignment=TA_RIGHT))],
        [Paragraph(data.get("client_email", ""),
                   _style("ce", fontSize=9, fontName="Helvetica",
                          textColor=GRAY)), ""],
        [Paragraph(data.get("client_address", ""),
                   _style("ca", fontSize=9, fontName="Helvetica",
                          textColor=GRAY)), ""],
    ]
    bt = Table(bill, colWidths=[9*cm, 8*cm])
    bt.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                            ("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    story += [bt, Spacer(1, 0.4*cm)]

    # ── Items table ────────────────────────────────────────────
    rows = [["#", "Description", "Qty", "Unit Price", "Amount"]]
    subtotal = 0.0
    for i, item in enumerate(data["items"], 1):
        line = item["qty"] * item["price"]
        subtotal += line
        rows.append([str(i), item["name"], str(item["qty"]),
                     f"Rs.{item['price']:.2f}", f"Rs.{line:.2f}"])

    tax_amt = subtotal * data.get("tax_rate", 0.0)
    total   = subtotal + tax_amt
    n       = len(data["items"])

    rows.append(["", "", "", "Subtotal",  f"Rs.{subtotal:.2f}"])
    if data.get("tax_rate", 0):
        rows.append(["", "", "", f"Tax ({data['tax_rate']*100:.0f}%)",
                     f"Rs.{tax_amt:.2f}"])
    rows.append(["", "", "", "TOTAL", f"Rs.{total:.2f}"])
    tr = len(rows)

    tbl = Table(rows, colWidths=[1*cm, 8*cm, 1.8*cm, 3*cm, 3.2*cm],
                repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,0),   ACCENT),
        ("TEXTCOLOR",    (0,0),(-1,0),   WHITE),
        ("FONTNAME",     (0,0),(-1,0),   "Helvetica-Bold"),
        ("FONTSIZE",     (0,0),(-1,0),   10),
        ("TOPPADDING",   (0,0),(-1,0),   8),
        ("BOTTOMPADDING",(0,0),(-1,0),   8),
        ("FONTNAME",     (0,1),(-1,n),   "Helvetica"),
        ("FONTSIZE",     (0,1),(-1,n),   9),
        ("ROWBACKGROUNDS",(0,1),(-1,n),  [WHITE, LIGHT_BG]),
        ("TOPPADDING",   (0,1),(-1,n),   6),
        ("BOTTOMPADDING",(0,1),(-1,n),   6),
        ("ALIGN",        (2,0),(-1,-1),  "RIGHT"),
        ("ALIGN",        (0,0),(0,-1),   "CENTER"),
        ("LINEBELOW",    (0,1),(-1,n),   0.5, colors.HexColor("#e5e7eb")),
        ("LINEABOVE",    (3,n+1),(-1,n+1), 1.5, ACCENT),
        ("FONTNAME",     (3,n+1),(-1,-1),"Helvetica-Bold"),
        ("FONTSIZE",     (3,n+1),(-1,-1), 10),
        ("TOPPADDING",   (3,n+1),(-1,-1), 7),
        ("BACKGROUND",   (3,tr-1),(-1,tr-1), ACCENT),
        ("TEXTCOLOR",    (3,tr-1),(-1,tr-1), WHITE),
        ("TOPPADDING",   (3,tr-1),(-1,tr-1), 8),
        ("BOTTOMPADDING",(3,tr-1),(-1,tr-1), 8),
    ]))
    story.append(tbl)

    # ── Notes ──────────────────────────────────────────────────
    if data.get("notes"):
        story += [Spacer(1, 0.4*cm),
                  Paragraph("Notes:",
                            _style("nh", fontSize=10, fontName="Helvetica-Bold",
                                   textColor=DARK)),
                  Paragraph(data["notes"],
                            _style("nb", fontSize=9, fontName="Helvetica",
                                   textColor=GRAY))]

    # ── Footer ─────────────────────────────────────────────────
    story += [Spacer(1, 1*cm),
              HRFlowable(width="100%", thickness=0.5,
                         color=GRAY, spaceAfter=6),
              Paragraph("Thank you for your business!",
                        _style("ty", fontSize=9, fontName="Helvetica",
                               textColor=GRAY, alignment=TA_CENTER))]

    doc.build(story)
    return invoice_id, filename, total
