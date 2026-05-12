from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    HRFlowable
)
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from datetime import datetime
import uuid
import os

ACCENT = colors.HexColor("#4338ca")
DARK = colors.HexColor("#1e1b4b")
GRAY = colors.HexColor("#6b7280")
LIGHT = colors.HexColor("#f8fafc")
SOFT = colors.HexColor("#eef2ff")
WHITE = colors.white


def style(name, **kwargs):
    return ParagraphStyle(name, **kwargs)


def money(x):
    return f"Rs. {x:,.2f}"


def generate_invoice(data, output_dir):

    invoice_id = f"INV-{datetime.now().strftime('%Y%m')}-{str(uuid.uuid4())[:6].upper()}"

    filename = f"{invoice_id}.pdf"
    filepath = os.path.join(output_dir, filename)

    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm
    )

    story = []

    # ───────────────── HEADER ─────────────────

    header = [
        [
            Paragraph(
                "FF-01-S5",
                style(
                    "logo",
                    fontSize=24,
                    fontName="Helvetica-Bold",
                    textColor=ACCENT,
                    leading=28
                )
            ),

            Paragraph(
                "INVOICE",
                style(
                    "invoice",
                    fontSize=24,
                    fontName="Helvetica-Bold",
                    textColor=DARK,
                    alignment=TA_RIGHT,
                    leading=28
                )
            )
        ],

        [
            Paragraph(
                "Smart Invoice Generator",
                style(
                    "tagline",
                    fontSize=9,
                    fontName="Helvetica",
                    textColor=GRAY
                )
            ),

            Paragraph(
                invoice_id,
                style(
                    "invoiceid",
                    fontSize=9,
                    textColor=GRAY,
                    alignment=TA_RIGHT
                )
            )
        ]
    ]

    header_table = Table(header, colWidths=[9 * cm, 7 * cm])

    header_table.setStyle(TableStyle([
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    story.append(header_table)

    story.append(
        HRFlowable(
            width="100%",
            thickness=1.2,
            color=ACCENT,
            spaceBefore=10,
            spaceAfter=18
        )
    )

    # ───────────────── CLIENT INFO ─────────────────

    date = datetime.now().strftime("%B %d, %Y")

    info = [
        [
            Paragraph(
                "<b>Bill To</b>",
                style(
                    "bill",
                    fontSize=11,
                    textColor=DARK
                )
            ),

            Paragraph(
                "<b>Invoice Details</b>",
                style(
                    "details",
                    fontSize=11,
                    textColor=DARK,
                    alignment=TA_RIGHT
                )
            )
        ],

        [
            Paragraph(
                data["client_name"],
                style(
                    "client",
                    fontSize=14,
                    fontName="Helvetica-Bold",
                    textColor=DARK,
                    leading=18
                )
            ),

            Paragraph(
                f"""
                <b>Date:</b> {date}<br/>
                <b>Status:</b> Generated
                """,
                style(
                    "meta",
                    fontSize=9,
                    textColor=GRAY,
                    alignment=TA_RIGHT,
                    leading=16
                )
            )
        ],

        [
            Paragraph(
                data.get("client_email", ""),
                style(
                    "email",
                    fontSize=10,
                    textColor=GRAY
                )
            ),
            ""
        ],

        [
            Paragraph(
                data.get("client_address", ""),
                style(
                    "address",
                    fontSize=10,
                    textColor=GRAY
                )
            ),
            ""
        ]
    ]

    info_table = Table(info, colWidths=[10 * cm, 6 * cm])

    info_table.setStyle(TableStyle([
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    story.append(info_table)
    story.append(Spacer(1, 0.7 * cm))

    # ───────────────── ITEMS TABLE ─────────────────

    rows = [["#", "Description", "Qty", "Price", "Amount"]]

    subtotal = 0

    for i, item in enumerate(data["items"], start=1):

        line_total = item["qty"] * item["price"]
        subtotal += line_total

        rows.append([
            str(i),
            item["name"],
            str(item["qty"]),
            money(item["price"]),
            money(line_total)
        ])

    tax_rate = data.get("tax_rate", 0)
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    rows.append(["", "", "", "Subtotal", money(subtotal)])

    if tax_rate > 0:
        rows.append([
            "",
            "",
            "",
            f"Tax ({int(tax_rate * 100)}%)",
            money(tax_amount)
        ])

    rows.append(["", "", "", "TOTAL", money(total)])

    total_row = len(rows) - 1

    table = Table(
        rows,
        colWidths=[1 * cm, 7.5 * cm, 2 * cm, 2.8 * cm, 3 * cm],
        repeatRows=1
    )

    table.setStyle(TableStyle([

        # Header
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),

        ("TOPPADDING", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        # Body
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 9),

        ("ROWBACKGROUNDS", (0, 1), (-1, -4), [WHITE, SOFT]),

        ("TOPPADDING", (0, 1), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 8),

        ("LINEBELOW", (0, 1), (-1, -4), 0.3, colors.HexColor("#e5e7eb")),

        # Alignment
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (2, 0), (-1, -1), "RIGHT"),

        # Totals
        ("FONTNAME", (3, -3), (-1, -1), "Helvetica-Bold"),

        ("BACKGROUND", (3, total_row), (-1, total_row), ACCENT),
        ("TEXTCOLOR", (3, total_row), (-1, total_row), WHITE),

        ("TOPPADDING", (3, total_row), (-1, total_row), 10),
        ("BOTTOMPADDING", (3, total_row), (-1, total_row), 10),

        ("FONTSIZE", (3, total_row), (-1, total_row), 11),

    ]))

    story.append(table)

    # ───────────────── NOTES ─────────────────

    if data.get("notes"):

        story.append(Spacer(1, 0.8 * cm))

        story.append(
            Paragraph(
                "Notes",
                style(
                    "notehead",
                    fontSize=11,
                    fontName="Helvetica-Bold",
                    textColor=DARK
                )
            )
        )

        story.append(Spacer(1, 0.12 * cm))

        story.append(
            Paragraph(
                data["notes"],
                style(
                    "notebody",
                    fontSize=9,
                    textColor=GRAY,
                    leading=16
                )
            )
        )

    # ───────────────── FOOTER ─────────────────

    story.append(Spacer(1, 1.3 * cm))

    story.append(
        HRFlowable(
            width="100%",
            thickness=0.5,
            color=colors.HexColor("#d1d5db"),
            spaceAfter=8
        )
    )

    story.append(
        Paragraph(
            "Generated using FF-01-S5 • Smart Invoice Generator",
            style(
                "footer",
                fontSize=8,
                textColor=GRAY,
                alignment=TA_CENTER
            )
        )
    )

    doc.build(story)

    return invoice_id, filename, total