from pdf2image import convert_from_path

images=convert_from_path("431426_Novel combinations of aplitabart_ a DR5 agonist IgM antibody_ with ADCs or chemotherapeutic agents lead to robust anti_tumor responses in solid tumor models.pdf",poppler_path=r"D:/Python/Release-24.02.0-0/poppler-24.02.0/Library/bin/")
x=1
for image in images:
    image.save('output'+str(x)+".jpg","JPEG")
    x=x+1