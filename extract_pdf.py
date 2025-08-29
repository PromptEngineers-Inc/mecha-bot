import PyPDF2

def extract_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    with open('data/output.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(text)
    

if __name__ == "__main__":
    extract_pdf('data/oding.pdf')
    