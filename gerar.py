from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        pass  

for i in range(1, 31):
    pdf = PDF()  # Cria uma nova instância do PDF para cada iteração
    pdf.add_page()

    # Adiciona uma imagem no corpo do documento
    pdf.image('./logo.png', x=15, y=20, w=180)

    pdf.set_font("Arial", "B", 25)
    pdf.set_y(150)  # Ajusta a posição vertical para abaixo da imagem
    pdf.cell(0, 10, "Para acessar documento", ln=True, align="C")

    pdf.set_font("Arial", size=25)
    pdf.set_text_color(0, 0, 255)

    # Adiciona o texto do link centralizado horizontalmente
    pdf.set_y(170)  # Ajusta a posição vertical para onde o link será inserido
    link = f'https://www.in.gov.br/leiturajornal?data={i:02d}-mm-aaaa'
    pdf.cell(0, 10, 'Clique aqui', ln=True, align='C', link=link)
    nome_pdf = f"do-{i:02d}-mm-aaaa"
    pdf.output(f"./mes-ano/{nome_pdf}.pdf")
    print(f"PDF gerado: {nome_pdf}.pdf")
