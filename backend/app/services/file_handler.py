from PyPDF2 import PdfReader

def extract_pdf_text(file):
    file.seek(0)
    reader = PdfReader(file)
    return "".join(page.extract_text() or "" for page in reader.pages)[:3000]

def extract_code_text(file):
    file.seek(0)
    return file.read().decode("utf-8", errors="ignore")[:3000]