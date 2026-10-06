from openpyxl import Workbook
def export(df,path):
    wb=Workbook();ws=wb.active
    ws.append(list(df.columns))
    for row in df.itertuples(index=False):
        ws.append(list(row))
    wb.save(path)
    return path
