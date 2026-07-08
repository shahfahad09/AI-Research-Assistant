import fitz


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf, start=1):
        page_text = page.get_text()
        text += f"\n\n[Page {page_number}]\n{page_text}"

    pdf.close()

    return text