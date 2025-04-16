from fpdf import FPDF

def generate_report(data: dict, output_path="nawa_report.pdf"):
    """
    Generates a minimal PDF report using fpdf.
    pip install fpdf==1.7
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="NAWA Tracking Report", ln=True, align="C")

    for k, v in data.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)

    pdf.output(output_path)
    return output_path

