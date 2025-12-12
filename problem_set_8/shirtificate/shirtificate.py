from fpdf import FPDF


class PDF(FPDF):
    pass

# Create PDF
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# title for shirtficate
pdf.set_font("helvetica", style="B",size=50)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")

# shirt and text
pdf.image("shirtificate.png", 35, 50, 140)
pdf.set_font("helvetica", style="", size=20)
pdf.set_text_color(255,255,255)
user_name = input("Name: ")
pdf.set_xy(0, 100) 
pdf.cell(0, 10, f"{user_name} took CS50", align="C")

pdf.output("shirtificate.pdf")