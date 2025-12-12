from fpdf import FPDF

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!")
pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output("tuto1.pdf")