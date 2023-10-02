import os
from bs4 import BeautifulSoup

def scrape_media_links(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    image_links = []
    video_links = []

    # Find all <img> tags
    img_tags = soup.find_all('img')
    # Find all <video> tags
    vid_tags = soup.find_all('video')

    # Extract the 'src' attribute from each <img> tag
    for img_tag in img_tags:
        src = img_tag.get('src')
        if src:
            image_links.append(src)

    # Extract the 'src' attribute from each <video> tag
    for vid_tag in vid_tags:
        src = vid_tag.get('src')
        if src:
            video_links.append(src)

    # Combine image and video links
    media_links = image_links + video_links

    return media_links

# Usage example
html_file = r"index (9).html"

# Extract the base name of the HTML file (without the extension)
base_name = os.path.splitext(os.path.basename(html_file))[0]

links = scrape_media_links(html_file)

# Create an output file name based on the HTML file name
output_file = f'{base_name}_media_links.txt'
with open(output_file, 'w') as f:
    for link in links:
        f.write(link + '\n')

print(f"Media links saved to '{output_file}'")

