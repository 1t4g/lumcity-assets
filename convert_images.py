import os
from Pillow import Image

def convert_images(png_folder, webp_folder):
    sizes = [(100, 100), (512, 512)]
    
    # Create target directories if they don't exist
    for size in sizes:
        size_folder = os.path.join(webp_folder, f"{size[0]}px")
        if not os.path.exists(size_folder):
            os.makedirs(size_folder)
    
    # Process each PNG file
    for filename in os.listdir(png_folder):
        if filename.endswith(".png"):
            png_path = os.path.join(png_folder, filename)
            base_name = os.path.splitext(filename)[0]
            
            with Image.open(png_path) as img:
                for size in sizes:
                    img_resized = img.resize(size, Image.ANTIALIAS)
                    output_folder = os.path.join(webp_folder, f"{size[0]}px")
                    output_path = os.path.join(output_folder, f"{base_name}{size[0]}px.webp")
                    img_resized.save(output_path, "WEBP")
                    print(f"Saved {output_path}")

if __name__ == "__main__":
    png_folder = "png"
    webp_folder = "webp"
    convert_images(png_folder, webp_folder)
