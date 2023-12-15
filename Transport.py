# Create the destination folder if it doesn't exist
import os
import shutil
# Your list of existing paths
def transf(destination_path,file_paths):
    os.makedirs(destination_path, exist_ok=True)
    # file_paths = ["/path/to/file1.pdf", "/path/to/file2.docx", "/path/to/subfolder/file3.txt"]
    for file_path in file_paths:
        # Check if the file exists in the source path
        if os.path.exists(file_path):
            # source_file = os.path.join(source_path, file_path)
            destination_file = os.path.join(destination_path, os.path.basename(file_path))
            shutil.copy(file_path, destination_file)
        else:
            print(f"File not found: {file_path}")

    print(f"Files copied to: {destination_path}")

if __name__ == '__main__':
    li = [r'C:\Users\vedant\OneDrive\Desktop\PDFS\Va.pdf',r'C:\Users\vedant\OneDrive\Desktop\PDFS\Ta.pdf']
    # m_li = []
    # for i in li:
    #     s = i.replace('\\','/')
    #     m_li.append(s)
    # print(m_li)
    destination = 'C:\\Users\\vedant\\OneDrive\\Desktop\\P'
    transf(destination,li)