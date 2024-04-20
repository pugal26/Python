import os
from pdf2image import convert_from_path

#Input path
pdf_folder = "D:/Python/input/"

#Output Path
output_folder = "D:/Python/output/"

#Ensure the output folder exists
os.makedirs(output_folder,exist_ok=True)

#get a lst of all pdf files in the folder
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

for pdf_file in pdf_files:
    #convert each PDF file to images
    images = convert_from_path(os.path.join(pdf_folder, pdf_file), poppler_path=r"D:/Python/Release-24.02.0-0/poppler-24.02.0/Library/bin/")

    #save each images wit the same name as the input PDF file
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder,f"{os.path.splitext(pdf_file)[0]}_{i+1}.jpg"),"JPEG")