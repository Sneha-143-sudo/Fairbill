from PIL import Image, ImageDraw, ImageFont

# Create a blank white canvas simulating an A4 sheet (800x1000)
img = Image.new('RGB', (800, 1000), color='white')
d = ImageDraw.Draw(img)

# Use basic system fonts (fallback to default if not found)
try:
    font_title = ImageFont.truetype("arial.ttf", 26)
    font_header = ImageFont.truetype("arial.ttf", 14)
    font_body = ImageFont.truetype("arial.ttf", 12)
    font_bold = ImageFont.truetype("arialbold.ttf", 12)
except IOError:
    font_title = font_header = font_body = font_bold = ImageFont.load_default()

# --- DRAW HEADER ---
d.text((50, 50), "APEX SUPER SPECIALITY HOSPITAL", fill="darkgreen", font=font_title)
d.text((50, 85), "Plot 12, Sector 4, HSR Layout, Bengaluru, Karnataka 560102", fill="gray", font=font_body)
d.text((50, 100), "GSTIN: 29AAAAA1111A1Z1 | Contact: +91 80 5555 0144", fill="gray", font=font_body)

# --- INVOICE INFO ---
d.text((550, 50), "TAX INVOICE / SUMMARY", fill="black", font=font_header)
d.text((550, 75), "Patient: Rajesh Kumar", fill="black", font=font_body)
d.text((550, 90), "UHID / Bill No: #2026-9941", fill="black", font=font_body)
d.text((550, 105), "Date: Oct 09, 2026", fill="black", font=font_body)

# Draw decorative divider line
d.line([(50, 135), (750, 135)], fill="darkgreen", width=2)

# --- TABLE HEADERS ---
d.text((50, 155), "SAC/HSN", fill="black", font=font_bold)
d.text((150, 155), "Description of Medical Services", fill="black", font=font_bold)
d.text((650, 155), "Amount (₹)", fill="black", font=font_bold)

d.line([(50, 175), (750, 175)], fill="black", width=1)

# --- BILLING LINE ITEMS (With hidden traps for the AI to catch!) ---
items = [
    ("9985", "General Ward Room Rent (Per Day)", "4,500.00"),
    ("9993", "Doctor Consultation & Round Charges", "1,200.00"),
    ("9993", "Essential Surgical Gloves & Consumables", "850.00"),    # Highly Inflated price!
    ("9985", "Hospital Hygiene & Maintenance Surcharge", "1,500.00"), # JUNK FEE!
    ("9993", "Nursing Care Attendant Charges", "2,000.00"),
    ("9993", "Doctor Consultation & Round Charges", "1,200.00"),      # DUPLICATE CHARGE!
]

y_pos = 195
for sac, desc, price in items:
    d.text((50, y_pos), sac, fill="black", font=font_body)
    d.text((150, y_pos), desc, fill="black", font=font_body)
    d.text((650, y_pos), price, fill="black", font=font_body)
    y_pos += 30

d.line([(50, y_pos + 10), (750, y_pos + 10)], fill="black", width=1)

# --- ILLEGAL TAX TRAP FOR HACKATHON WOW FACTOR ---
# Note: Room rents under ₹5000 and general medical procedures are exempt from GST in India.
# This hospital is illegally charging 18% GST on the total to scam the consumer.
d.text((450, y_pos + 30), "Subtotal:", fill="black", font=font_body)
d.text((650, y_pos + 30), "11,250.00", fill="black", font=font_body)

d.text((450, y_pos + 50), "CGST (9%) + SGST (9%):", fill="darkred", font=font_body)
d.text((650, y_pos + 50), "2,025.00", fill="darkred", font=font_body)

d.line([(500, y_pos + 75), (750, y_pos + 75)], fill="gray", width=1)

d.text((450, y_pos + 90), "GRAND TOTAL DUE:", fill="black", font=font_bold)
d.text((650, y_pos + 90), "₹13,275.00", fill="black", font=font_bold)

# Save the image locally
img.save("indian_bill.png")
print("✅ Success! 'indian_bill.png' generated safely.")