import base64
import csv
import os

MAX_FIELD_SIZE = 1024 * 1024 * 1024  # Set the field size limit to 1024 MB

def save_image_from_base64(file_path, base64_string):
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)

    with open(file_path, "wb") as image_file:
        image_file.write(base64.b64decode(base64_string))

def convert_csv_to_images(csv_file):
    csv.field_size_limit(MAX_FIELD_SIZE)  # Set the field size limit
    
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            file_path = row[0]
            base64_string = row[1]
            save_image_from_base64(file_path, base64_string)
            print("Converted:", file_path)

    print("Images saved successfully!")

# Specify the path to the CSV file containing file paths and base64 strings
csv_file = r"pizza"

# Convert the CSV to images
convert_csv_to_images(csv_file)
