import os
from PIL import Image

def convert_images(png_folder, webp_folder):
    sizes = [(100, 100), (512, 512)]
    
    for size in sizes:
        size_folder = os.path.join(webp_folder, f"{size[0]}px")
        os.makedirs(size_folder, exist_ok=True)  # Create size-specific folder if it doesn't exist
    
    for filename in os.listdir(png_folder):
        if filename.endswith(".png"):
            png_path = os.path.join(png_folder, filename)
            base_name = os.path.splitext(filename)[0]
            
            with Image.open(png_path) as img:
                for size in sizes:
                    width, height = size
                    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
                    aspect_ratio = img.width / img.height
                    
                    if img.width > img.height:
                        new_height = int(width / aspect_ratio)
                        resized_img = img.resize((width, new_height), Image.LANCZOS)
                        offset = (0, (height - new_height) // 2)
                    else:
                        new_width = int(height * aspect_ratio)
                        resized_img = img.resize((new_width, height), Image.LANCZOS)
                        offset = ((width - new_width) // 2, 0)
                    
                    new_img.paste(resized_img, offset)
                    size_folder = os.path.join(webp_folder, f"{size[0]}px")
                    os.makedirs(size_folder, exist_ok=True)  # Ensure size-specific folder exists
                    output_path = os.path.join(size_folder, f"{base_name}_{size[0]}px.webp")
                    new_img.save(output_path, "WEBP")
                    print(f"Saved {output_path}")

if __name__ == "__main__":
    png_folder = "png"
    webp_folder = "webp"
    convert_images(png_folder, webp_folder)
