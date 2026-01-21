from fpdf import FPDF

def save_pdf(
    state,
    district,
    year,
    disaster,
    overall_risk,
    env
):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "IDARVIZHI DISASTER INTELLIGENCE REPORT", ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", "", 11)

    pdf.multi_cell(0, 8, f"""
STATE           : {state}
DISTRICT        : {district}
YEAR            : {year}
DISASTER TYPE   : {disaster}

OVERALL RISK SCORE : {overall_risk}
SEVERITY INDEX     : {env["disaster_index"]}
""")

    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "1. Environmental Observations", ln=True)

    pdf.set_font("Arial", "", 11)
    for k, v in env.items():
        pdf.cell(0, 8, f"{k.replace('_',' ').title()} : {v}", ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "2. Risk Interpretation", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, """
-> Elevated environmental stress indicators detected.
-> Weather parameters exceed historical seasonal averages.
-> Population exposure increases vulnerability.
-> Infrastructure readiness is moderate.
-> Immediate preparedness actions are recommended.
""")

    pdf.ln(3)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "3. Advisory & Preparedness Measures", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, """
-> Activate district emergency operations center.
-> Issue public early warning advisories.
-> Deploy disaster response teams.
-> Prepare evacuation shelters.
-> Monitor updates every 3 hours.
""")

    file_path = "IDARVIZHI_Disaster_Report.pdf"
    pdf.output(file_path)

    return file_path
