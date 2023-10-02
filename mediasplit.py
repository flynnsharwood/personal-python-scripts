import os
import struct

def split_binary_file(input_file, output_dir_odd, output_dir_even):
    with open(input_file, 'rb') as infile:
        data = infile.read()

    # Separate odd and even bytes
    odd_bytes = data[::2]
    even_bytes = data[1::2]

    # Create output directories if they don't exist
    os.makedirs(output_dir_odd, exist_ok=True)
    os.makedirs(output_dir_even, exist_ok=True)

    # Create output file paths
    output_file_odd = os.path.join(output_dir_odd, os.path.basename(input_file))
    output_file_even = os.path.join(output_dir_even, os.path.basename(input_file))

    # Write odd bytes to the odd output file
    with open(output_file_odd, 'wb') as outfile_odd:
        outfile_odd.write(odd_bytes)

    # Write even bytes to the even output file
    with open(output_file_even, 'wb') as outfile_even:
        outfile_even.write(even_bytes)

def split_media_files_in_directory(input_directory, output_directory_odd, output_directory_even):
    # List of media file extensions
    media_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webm', '.mp4', '.avi', '.mkv', '.3gp', '.mov', '.mpg', '.wmv']

    # Walk through the directory tree and process files
    for root, _, files in os.walk(input_directory):
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension.lower() in media_extensions:
                input_file_path = os.path.join(root, file)

                split_binary_file(input_file_path, output_directory_odd, output_directory_even)

# Usage example
input_directory = '/mnt/c/Users/Study/Pictures/input'
output_directory_odd = '/mnt/c/Users/Study/Pictures/odd'
output_directory_even = '/mnt/c/Users/Study/Pictures/even'

split_media_files_in_directory(input_directory, output_directory_odd, output_directory_even)
