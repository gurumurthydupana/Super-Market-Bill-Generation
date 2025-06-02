from datetime import datetime
import re
from fpdf import FPDF

def main():
    name = input("Enter your name: ")

    list_items = '''
Rice       = 50 Rs/kg
Sugar      = 20 Rs/kg
Salt       = 10 Rs/kg
Chilli     = 45 Rs/kg
Onions     = 25 Rs/kg
Garlic     = 30 Rs/kg
Tamarind   = 50 Rs/kg
Colgate    = 70 Rs/pack
Soaps      = 15 Rs/pack
Shampoo    = 5 Rs/pack
Biscuits   = 15 Rs/pack
Boost      = 150 Rs/pack
Oil        = 250 Rs/ltr
Tea Powder = 70 Rs/pack
Dal        = 100 Rs/kg
'''

    # Prices dictionary (keys are title cased)
    items = {
        'Rice': 50,
        'Sugar': 20,
        'Salt': 10,
        'Chilli': 45,
        'Onions': 25,
        'Garlic': 30,
        'Tamarind': 50,
        'Colgate': 70,
        'Soaps': 15,
        'Shampoo': 5,
        'Biscuits': 15,
        'Boost': 150,
        'Oil': 250,
        'Tea Powder': 70,
        'Dal': 100
    }

    unit_types = {
        'kg': 1, 'g': 0.001, 'ltr': 1, 'pack': 1, 'pcs': 1,
        'pack': 1, 'piece': 1, 'each': 1
    }

    if input("For list of items, press 1: ").strip() == '1':
        print(list_items)

    pricelist = []
    totalprice = 0

    while True:
        item = input("Enter your item: ").strip().title()
        if item not in items:
            print("❌ The item you entered is not available. Please try again.")
            continue

        while True:
            quantity_input = input("Enter the quantity (e.g., 2 kg, 500 g, 3 pack): ").lower().strip()
            match = re.match(r'(\d+(?:\.\d+)?)\s*([a-zA-Z]+)', quantity_input)
            if match:
                qty_val = float(match.group(1))
                unit = match.group(2)
                if unit in unit_types:
                    qty_converted = qty_val * unit_types[unit]
                    break
                else:
                    print("❌ Unknown unit. Please use kg, g, ltr, pack, pcs, etc.")
            else:
                print("❌ Invalid format. Please enter quantity followed by unit (e.g., 2 kg)")

        price = qty_converted * items[item]
        pricelist.append((item, f"{qty_val} {unit}", items[item], price))
        totalprice += price

        choice = input("Add more items? (yes/no): ").strip().lower()
        if choice == "no":
            break

    if input("Can I bill the items? (yes/no): ").strip().lower() == "yes":
        if totalprice > 0:
            GST = totalprice * 0.05  # 5% GST as per your original code
            final_price = totalprice + GST
            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            # Print receipt to console
            print("\n" + "="*25, "SM Super Market", "="*25)
            print(" "*28 + "SRICITY")
            print(f"Name: {name:<30} Date: {now}")
            print("-"*80)
            print(f"{'S.No':<6} {'Item':<20} {'Quantity':<15} {'Unit Price':<12} {'Price'}")
            print("-"*80)
            for i, (item, qty, unit_price, cost) in enumerate(pricelist, 1):
                print(f"{i:<6} {item:<20} {qty:<15} Rs {unit_price:<10} Rs {cost:.2f}")
            print("-"*80)
            print(f"{'Subtotal':<55} Rs {totalprice:.2f}")
            print(f"{'GST (5%)':<55} Rs {GST:.2f}")
            print(f"{'Total Amount':<55} Rs {final_price:.2f}")
            print("-"*80)
            print(" " * 20 + "Thanks for visiting <----> Visit Again!")
            print("-"*80)

            # Create PDF receipt
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "SM Super Market", ln=True, align='C')
            pdf.set_font("Arial", '', 12)
            pdf.cell(0, 8, "SRICITY", ln=True, align='C')
            pdf.cell(0, 8, "-"*60, ln=True)
            pdf.cell(0, 8, f"Customer Name : {name}", ln=True)
            pdf.cell(0, 8, f"Date & Time   : {now}", ln=True)
            pdf.cell(0, 8, "-"*60, ln=True)

            pdf.set_font("Arial", 'B', 12)
            pdf.cell(10, 10, "S.No", 1)
            pdf.cell(50, 10, "Item", 1)
            pdf.cell(40, 10, "Quantity", 1)
            pdf.cell(40, 10, "Unit Price", 1)
            pdf.cell(40, 10, "Price", 1, ln=True)

            pdf.set_font("Arial", '', 12)
            for i, (item, qty, unit_price, cost) in enumerate(pricelist, 1):
                pdf.cell(10, 10, str(i), 1)
                pdf.cell(50, 10, item, 1)
                pdf.cell(40, 10, qty, 1)
                pdf.cell(40, 10, f"Rs {unit_price}", 1)
                pdf.cell(40, 10, f"Rs {cost:.2f}", 1, ln=True)

            pdf.cell(0, 8, "-"*60, ln=True)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(140, 10, "Subtotal", 0)
            pdf.cell(0, 10, f"Rs {totalprice:.2f}", ln=True)
            pdf.cell(140, 10, "GST (5%)", 0)
            pdf.cell(0, 10, f"Rs {GST:.2f}", ln=True)
            pdf.cell(140, 10, "Total Amount", 0)
            pdf.cell(0, 10, f"Rs {final_price:.2f}", ln=True)
            pdf.cell(0, 10, "-"*60, ln=True)
            pdf.set_font("Arial", 'I', 12)
            pdf.cell(0, 10, "Thank you for visiting! Please come again!", ln=True, align='C')

            pdf.output("receipt.pdf")
            print("📄 Receipt saved as 'receipt.pdf'")

if __name__ == "__main__":
    main()
