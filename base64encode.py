import base64
import os
import glob
import csv

# Function to check if a file has an image extension
def is_image_file(file_name):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webm', '.mp4', '.avi', '.mkv', '.3gp', '.mov', '.mpg', '.wmv',]
    return any(file_name.lower().endswith(ext) for ext in image_extensions)

new_data = []
main_directory = r"/mnt/c/Users/Study/Pictures/pizza/"

# Traverse through the directory and its subdirectories
for root, dirs, files in os.walk(main_directory):
    for file in files:
        if is_image_file(file):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as image_file:
                result = base64.b64encode(image_file.read()).decode('utf-8')
                new_data.append([file_path, result])

# Save the base64 strings as CSV
csv_file = r"pizza.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["File Name", "Base64 String"])
    writer.writerows(new_data)

print("Base64 strings saved to CSV successfully!")
