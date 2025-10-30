import os
import csv
from openpyxl import Workbook
from openpyxl.drawing.image import Image as pyxlImage
from tqdm import tqdm
from PIL import Image, ImageOps

from utils import delete_directory, create_directory


class Pohon:
    def __init__(self, settings):
        self.wb = Workbook()
        self.ws = self.wb.active

        self.folder_path = settings["FOLDER_PATH"]
        self.export_path = settings["EXPORT_PATH"]
        self.image_dimension = settings["IMAGE_DIMENSION"]

    def only_images(self):
        # Loop through all files in folder
        row = 1
        temp_folder_name = os.path.join(self.folder_path, "temp")
        create_directory(temp_folder_name)
            
        for file_name in tqdm(sorted(os.listdir(self.folder_path))):
            if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                img_path = os.path.join(self.folder_path, file_name)
                temp_img_path = os.path.join(temp_folder_name, file_name)   # Temporary path to store fixed images
                with Image.open(img_path) as img:
                    img_fixed = ImageOps.exif_transpose(img)    # Fix image orientation and save to temporary path
                    img_fixed.save(temp_img_path)

                # Open temporary image
                img_pyxl = pyxlImage(temp_img_path)

                # Resize image (width x height in pixels)
                img_pyxl.height = self.image_dimension["height"]
                img_pyxl.width = self.image_dimension["width"]
                
                # Add image and filename to worksheet
                self.ws.add_image(img_pyxl, f"A{row}")
                self.ws[f"B{row}"] = file_name

                # Move to next row (e.g., one row down per image)
                row += 1   # adjust spacing (1 row(s) per picture)

        # Save the workbook
        self.wb.save(self.export_path)
        print(f"Workbook {self.export_path} is created successfully.")

        # Delete temporary folder
        delete_directory(temp_folder_name)

    def images_with_coordinates(self):
        if os.path.exists("output.csv"):
            row = 1
            temp_folder_name = os.path.join(self.folder_path, "temp")
            create_directory(temp_folder_name)
            # Open the CSV file
            with open('output.csv', 'r', newline='') as csvfile:
                # Create a CSV reader object
                reader = csv.reader(csvfile)

                # Iterate over each row in the CSV file
                for csv_row in tqdm(reader):
                    file_name = csv_row[0]
                    latitude = csv_row[1]
                    longitude = csv_row[2]

                    img_path = os.path.join(self.folder_path, file_name)
                    temp_img_path = os.path.join(temp_folder_name, file_name)   # Temporary path to store fixed images
                    with Image.open(img_path) as img:
                        img_fixed = ImageOps.exif_transpose(img)    # Fix image orientation and save to temporary path
                        img_fixed.save(temp_img_path)

                    # Open temporary image
                    img_pyxl = pyxlImage(temp_img_path)

                    # Resize image (width x height in pixels)
                    img_pyxl.height = self.image_dimension["height"]
                    img_pyxl.width = self.image_dimension["width"]
                    
                    # Add image, filename, and coordinates to worksheet
                    self.ws.add_image(img_pyxl, f"A{row}")
                    self.ws[f"B{row}"] = file_name
                    self.ws[f"C{row}"] = latitude
                    self.ws[f"D{row}"] = longitude

                    # Move to next row (e.g., one row down per image)
                    row += 1   # adjust spacing (1 row(s) per picture)

            # Save the workbook
            self.wb.save(self.export_path)
            print(f"Workbook {self.export_path} is created successfully.")

            # Delete temporary folder
            delete_directory(temp_folder_name)
                    
                    
        else:
            print("output.csv not found!, please generate first.")