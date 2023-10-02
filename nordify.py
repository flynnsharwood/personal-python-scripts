import argparse
import os
from image_go_nord import convert_to_nord

def main():
    parser = argparse.ArgumentParser(description="Convert image palettes using image-go-nord.")
    
    parser.add_argument("input_path", help="Path to the input image file or directory.")
    parser.add_argument("output_path", help="Path to the output image file or directory.")
    parser.add_argument("--avg_algorithm", action="store_true", help="Toggle averaging algorithm.")
    parser.add_argument("--palette", choices=["nord", "solarized", "gruvbox", "one_dark", "dracula"], default="nord", help="Choose a palette.")
    
    args = parser.parse_args()
    
    if os.path.isdir(args.input_path):
        convert_images_in_directory(args.input_path, args.output_path, args.avg_algorithm, args.palette)
    else:
        convert_image(args.input_path, args.output_path, args.avg_algorithm, args.palette)

def convert_images_in_directory(input_dir, output_dir, avg_algorithm, palette):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            convert_image(input_path, output_path, avg_algorithm, palette)
        else:
            print(f"Skipping {filename} (unsupported file format).")

def convert_image(input_image, output_image, avg_algorithm, palette):
    try:
        convert_to_nord(input_image, output_image, avg_algorithm, palette)
        print(f"Image converted using the '{palette}' palette: {input_image} -> {output_image}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
