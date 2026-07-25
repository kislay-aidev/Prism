from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
def export(title,lines,path):
    doc=SimpleDocTemplate(path);styles=getSampleStyleSheet()
    elems=[Paragraph(f'<b>{title}</b>',styles['Heading1'])]
    elems.extend(Paragraph(str(x),styles['BodyText']) for x in lines)
    doc.build(elems)
    return path
