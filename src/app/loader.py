from io import BytesIO
from pdfplumber import open as pdf_open
from docx import Document

def load_document(filename, content, content_type):
    if content_type == 'text/plain' or filename.lower().endswith('.txt'):
        return content.decode('utf-8')
    if content_type == 'application/pdf':
        return extract_pdf_text(content)
    elif content_type in ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        return extract_docx_text(content)
    else:
        raise ValueError("Unsupported file type")

def extract_pdf_text(content):
    text = ""
    with pdf_open(BytesIO(content)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_docx_text(content):
    document = Document(BytesIO(content))
    return "\n".join([para.text for para in document.paragraphs])
