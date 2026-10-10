from PIL import Image, ImageDraw, ImageFont

# Create a blank white canvas simulating an A4 sheet (800x1000)
img = Image.new('RGB', (800, 1000), color='white')
d = ImageDraw.Draw(img)

# Use basic system fonts (fallback to default if not found)
try:
    font_title = ImageFont.truetype("arial.ttf", 28)
    font_header = ImageFont.truetype("arial.ttf", 14)
    font_body = ImageFont.truetype("arial.ttf", 12)
    font_bold = ImageFont.truetype("arialbold.ttf", 12)
except IOError:
    font_title = font_header = font_body = font_bold = ImageFont.load_default()

# --- DRAW HEADER ---
d.text((50, 50), "METRO CARE REGIONAL HOSPITAL", fill="navy", font=font_title)
d.text((50, 90), "100 Medical Center Blvd, New York, NY 10001", fill="gray", font=font_body)
d.text((50, 105), "Customer Support: 1-800-555-0199", fill="gray", font=font_body)

# --- INVOICE INFO ---
d.text((550, 50), "INVOICE PRIOR NOTICE", fill="black", font=font_header)
d.text((550, 75), "Patient Name: Alex Mercer", fill="black", font=font_body)
d.text((550, 90), "Account Num: #9844-1102X", fill="black", font=font_body)
d.text((550, 105), "Statement Date: Oct 02, 2026", fill="black", font=font_body)

# Draw decorative divider line
d.line([(50, 140), (750, 140)], fill="navy", width=2)

# --- TABLE HEADERS ---
d.text((50, 160), "Date", fill="black", font=font_bold)
d.text((150, 160), "Description of Service / Line Item", fill="black", font=font_bold)
d.text((650, 160), "Amount ($)", fill="black", font=font_bold)

d.line([(50, 180), (750, 180)], fill="black", width=1)

# --- BILLING LINE ITEMS (Including sneaky hidden fees!) ---
items = [
    ("09/24/2026", "Emergency Room Triage Assessment", "450.00"),
    ("09/24/2026", "Sterile Gauze Bandage (Quantity: 2)", "120.00"),     # Overpriced!
    ("09/24/2026", "IV Administration Fluid (Saline 1L)", "310.00"),
    ("09/24/2026", "Acetaminophen 325mg (Single Oral Dose)", "45.00"),   # Tylenol markup!
    ("09/24/2026", "Facility Operational Readiness Fee", "150.00"),       # JUNK FEE!
    ("09/24/2026", "Biomedical Waste Disposal Surcharge", "85.00"),      # Double-dipped fee!
    ("09/24/2026", "Emergency Room Triage Assessment", "450.00"),        # DUPLICATE CHARGE!
]

y_pos = 200
for date, desc, price in items:
    # Highlight the scam/junk rows slightly so they look clear to us
    if "Fee" in desc or "Surcharge" in desc or "Duplicate" in desc or "Gauze" in desc:
        d.text((50, y_pos), date, fill="darkred", font=font_body)
        d.text((150, y_pos), desc, fill="darkred", font=font_body)
        d.text((650, y_pos), price, fill="darkred", font=font_body)
    else:
        d.text((50, y_pos), date, fill="black", font=font_body)
        d.text((150, y_pos), desc, fill="black", font=font_body)
        d.text((650, y_pos), price, fill="black", font=font_body)
    y_pos += 30

d.line([(50, y_pos + 10), (750, y_pos + 10)], fill="black", width=1)

# --- TOTAL DUE ---
d.text((500, y_pos + 30), "TOTAL AMOUNT DUE:", fill="black", font=font_bold)
d.text((650, y_pos + 30), "$1,610.00", fill="black", font=font_bold)

# Save the image locally
img.save("sample_bill.png")
print("✅ Success! 'sample_bill.png' generated. Drop this directly into your Streamlit app.")