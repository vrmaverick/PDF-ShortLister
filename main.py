import os
import fitz  # PyMuPDF for PDF files
from docx import Document  # python-docx for Word files
import Transport 


def search_pdf(file_path, keyword):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return keyword in text

def search_word(file_path, keyword):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return keyword in text

def search_files_in_folder(folder_path, keyword):
    matching_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith('.pdf'):
            if search_pdf(file_path, keyword):
                matching_files.append(fr"{file_path}")
                
                print(f"Found keyword '{keyword_to_search}' in: {file_path}")
        elif filename.endswith('.docx'):
            if search_word(file_path, keyword):
                matching_files.append(fr"{file_path}")
                print(f"Found keyword '{keyword_to_search}' in: {file_path}")

    return matching_files

if __name__=="__main__":
    # Specify the folder containing your PDF and Word files
    folder_path = 'C:\\Users\\vedant\\OneDrive\\Desktop\\PDFS' #source folder
    keyword_to_search = 'is'

    matching_files = search_files_in_folder(folder_path, keyword_to_search)

    if len(matching_files) > 0:
        print(f"These files contain the keyword '{keyword_to_search}':")
        for file_path in matching_files:
            print(file_path)
            print(type(matching_files))
        destination_path = 'C:\\Users\\vedant\\OneDrive\\Desktop\\destination' #destination folder
        Transport.transf(destination_path,matching_files)
    else:
        print(f"No files found containing the keyword '{keyword_to_search}'.")


