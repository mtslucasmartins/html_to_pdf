from io import BytesIO
from xhtml2pdf import pisa

def convert_html_to_pdf(html, output_path, encoding='utf-8'):
    output_file = open(output_path, "w+b")

    data = BytesIO(html.encode(encoding))

    status = pisa.CreatePDF(data, dest=output_file, encoding=encoding)           

    output_file.close()

    return status.err

def convert_html_template_to_pdf(source_path, output_path):
    with open(source_path, 'r', encoding='utf-8') as f: 
        return convert_html_to_pdf(f.read(), output_path)

if __name__ == "__main__":
    pisa.showLogging()

    source_file = 'template.html'
    convert_html_template_to_pdf(source_file, 'from_template.pdf')
    # source_text = html
    # convert_html_to_pdf(source_text, 'from_string.pdf') 