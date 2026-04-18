from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
topics = pd.read_csv("./src/topics.csv")

for index, row in topics.iterrows():

    pdf.add_page()
    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=10, h=12, txt=row['Topic'], align='L', ln=1, border=0)

    
    for i in range(20, 298, 10):
        pdf.line(10, i, 298, i)
    
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R', ln=1, border=0)


    for page in range(row['Pages']-1):
        pdf.add_page()
        
        pdf.ln(275)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
        

        for j in range(10, 285, 10):
            pdf.line(10, j, 298, j)
        
pdf.output("prueba.pdf")
