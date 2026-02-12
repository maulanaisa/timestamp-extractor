import pymupdf
import os
from tqdm import tqdm
from settings import SETTINGS

from utils import create_directory

base_path = SETTINGS["PDF_FOLDER_PATH"]
documents = [filename for filename in os.listdir(base_path) if filename.endswith(".pdf")]
export_path = os.path.join(base_path, "images")
create_directory(export_path)

for document in documents:
    print(document)
    doc = pymupdf.open(os.path.join(base_path, document))
    for page_index in tqdm(range(len(doc))):
        page = doc[page_index]
        image_list = page.get_images()

        for image_index, img in enumerate(image_list, start=1):
            xref = img[0] # get the XREF of the image
            pix = pymupdf.Pixmap(doc, xref)

            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

            if pix.height >= 100 and pix.width >= 100:
                pix.save(os.path.join(export_path,f"{document}-page_{page_index}-image_{image_index}.jpg"))
            pix = None