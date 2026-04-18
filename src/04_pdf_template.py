from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
topics = pd.read_csv("topics.csv")

for index, row in topics.iterrows():

    pdf.add_page()
    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, txt=row['topic'], align='l', ln=1, border=1)
    pdf.line(10, 21, 200, 21)


pdf.output("prueba.pdf")
