
from fpdf import FPDF
import datetime

def get_input(prompt):
    return input(f"{prompt}: ").strip()

def create_pdf(data, filename="vault_lifeplan.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="VAULTGUARDIAN™ – DIGITAL LIVSPLAN", ln=True, align='C')
    pdf.ln(10)

    for key, value in data.items():
        pdf.multi_cell(0, 10, txt=f"{key}: {value}")
        pdf.ln(2)

    pdf.ln(10)
    pdf.cell(0, 10, txt=f"Skapat: {datetime.date.today()}   |   Signerat: ___________________", ln=True)

    pdf.output(filename)
    print(f"✅ PDF genererad: {filename}")

def main():
    print("🧠 VAULTPDF GENERATOR – Svara på frågorna nedan")
    questions = {
        "Namn": get_input("Vad heter du?"),
        "Kontaktperson": get_input("Vem ska kontaktas om något händer dig?"),
        "Viktigaste filer att säkra": get_input("Vilka filer/mappar är viktigast?"),
        "Lösenordshantering": get_input("Var finns dina lösenord? (t.ex. i lösenordsapp, på papper...)"),
        "Sociala medier": get_input("Vad ska göras med dina sociala medier vid bortgång?"),
        "Instruktioner": get_input("Finns andra instruktioner till familj, vänner, affärspartners?"),
    }
    create_pdf(questions)

if __name__ == "__main__":
    main()
