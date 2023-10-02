import os

def merge_binary_files(input_dir_odd, input_dir_even, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through files in the odd input directory
    for root, _, files in os.walk(input_dir_odd):
        for file in files:
            input_file_odd = os.path.join(root, file)

            # Construct the corresponding even file path
            input_file_even = os.path.join(input_dir_even, file)

            # Construct the output file path
            output_file_path = os.path.join(output_directory, file)

            # Read odd and even parts as binary data
            with open(input_file_odd, 'rb') as infile_odd, open(input_file_even, 'rb') as infile_even:
                odd_bytes = infile_odd.read()
                even_bytes = infile_even.read()

                # Combine odd and even parts
                merged_data = bytearray()
                max_length = max(len(odd_bytes), len(even_bytes))

                for i in range(max_length):
                    if i < len(odd_bytes):
                        merged_data.append(odd_bytes[i])
                    if i < len(even_bytes):
                        merged_data.append(even_bytes[i])

                # Write the merged data to the output file
                with open(output_file_path, 'wb') as outfile:
                    outfile.write(merged_data)

# Usage example
input_directory_odd = '/mnt/c/Users/Study/Pictures/odd'
input_directory_even = '/mnt/c/Users/Study/Pictures/even'
output_directory = '/mnt/c/Users/Study/Pictures/output'

merge_binary_files(input_directory_odd, input_directory_even, output_directory)
