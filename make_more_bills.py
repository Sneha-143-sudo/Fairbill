from PIL import Image, ImageDraw, ImageFont

def generate_bill(filename, title, subtitle, items, totals_text, totals_val, color="black"):
    img = Image.new('RGB', (800, 950), color='white')
    d = ImageDraw.Draw(img)
    try:
        f_title, f_body, f_bold = ImageFont.truetype("arial.ttf", 26), ImageFont.truetype("arial.ttf", 12), ImageFont.truetype("arialbold.ttf", 12)
    except IOError:
        f_title = f_body = f_bold = ImageFont.load_default()

    d.text((50, 50), title, fill=color, font=f_title)
    d.text((50, 85), subtitle, fill="gray", font=f_body)
    d.line([(50, 130), (750, 130)], fill=color, width=2)
    
    d.text((50, 150), "Description", fill="black", font=f_bold)
    d.text((650, 150), "Amount (₹)", fill="black", font=f_bold)
    d.line([(50, 170), (750, 170)], fill="black", width=1)
    
    y = 190
    for desc, price in items:
        d.text((50, y), desc, fill="black", font=f_body)
        d.text((650, y), price, fill="black", font=f_body)
        y += 30
        
    d.line([(50, y + 10), (750, y + 10)], fill="black", width=1)
    d.text((450, y + 30), totals_text, fill="darkred" if "GST" in totals_text or "Service" in totals_text else "black", font=f_body)
    d.text((650, y + 30), totals_val, fill="black", font=f_bold)
    img.save(filename)
    print(f"✅ Generated {filename}")

# 1. RESTAURANT BILL (The Forced Service Charge & Wrong GST Trap)
rest_items = [
    ("Paneer Butter Masala", "320.00"),
    ("Butter Naan (Quantity: 3)", "180.00"),
    ("Jeera Rice", "150.00"),
    ("Mineral Water Bottle (MRP ₹20)", "60.00"),            # Inflated pricing!
    ("Forced Restaurant Service Charge (10%)", "71.00"),   # ILLEGAL/VOLUNTARY FEE!
]
generate_bill("restaurant_bill.png", "SPICE KITCHEN RESTAURANT", "MG Road, Bengaluru | GSTIN: 29BBBCC1111A1Z2", rest_items, "Grand Total (Includes 18% GST instead of 5%):", "₹921.00", "darkred")

# 2. ELECTRICITY BILL (The Slab Calculation & Mystery Surcharge Trap)
elec_items = [
    ("Fixed Monthly Fixed Demand Charge", "150.00"),
    ("Energy Charges (Slab 1: 0-100 Units @ ₹4.50)", "450.00"),
    ("Energy Charges (Slab 2: 101-200 Units @ ₹7.00)", "700.00"),
    ("Unexplained Fuel Adjustment Surcharge", "340.00"),    # SUSPICIOUS MARKUP!
    ("Delayed Payment Penalty Interest (Paid on time!)", "180.00"), # ERROR!
]
generate_bill("electricity_bill.png", "STATE ELECTRICITY DISTRIBUTION CO.", "Nesco Zone 3 | Consumer ID: 02848194410", elec_items, "NET AMOUNT PAYABLE:", "₹1,820.00", "darkblue")

# 3. GROCERY RECEIPT (The Over-MRP Price Trap)
grocery_items = [
    ("Basmati Rice 5kg Pack", "650.00"),
    ("Refined Sunflower Oil 1L", "145.00"),
    ("Amul Butter 500g (Printed Max MRP ₹275)", "320.00"),   # OVER-MRP SCAM!
    ("Organic Whole Wheat Atta 5kg", "290.00"),
    ("Mandatory Carry Bag & Handling Surcharge", "45.00"),  # JUNK FEE!
]
generate_bill("grocery_bill.png", "MEGA MART SUPERMARKET", "HSR Layout Branch | Cashier: Lane 04", grocery_items, "TOTAL AMOUNT PAYABLE:", "₹1,450.00", "darkgreen")