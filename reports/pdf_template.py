def generate(report: dict, output_path: str):
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
        from reportlab.lib.styles import getSampleStyleSheet
    except ImportError:
        raise RuntimeError("reportlab is required for PDF generation. Install: pip install reportlab")

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Executive Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    for section, data in report.items():
        elements.append(Paragraph(f"<b>{section.title()}</b>", styles["Heading2"]))
        if isinstance(data, dict):
            rows = [[k, str(v)] for k, v in data.items()]
            if rows:
                elements.append(Table([["Metric", "Value"]] + rows))
        elements.append(Spacer(1, 12))

    doc.build(elements)
    return output_path
