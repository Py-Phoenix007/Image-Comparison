from PIL import Image
import hashlib

# Author: Jeba Seelan
# Topic: Image Comparison Tool
# Created on: 2024-10-23
# Description: A script to compare two images to determine if they are the same, regardless of format.

def CheckImgPix(ImgPath1: str, ImgPath2: str) -> str:
    """
    Compare two images to determine if they are the same, regardless of format.

    Parameters:
    ImgPath1 (str): File path to the first image.
    ImgPath2 (str): File path to the second image.

    Returns:
    str: Message indicating whether the images are the same or not.
    """
    try:
        with Image.open(ImgPath1) as img1, Image.open(ImgPath2) as img2:
            # Convert images to a consistent mode (RGB or RGBA)
            img1 = img1.convert('RGBA')
            img2 = img2.convert('RGBA')

            # Check if both images have the same size
            if img1.size != img2.size:
                return "Two Images Are Not Same"

            # Create a hash for each image to compare their content
            hash1 = hashlib.sha256(img1.tobytes()).hexdigest()
            hash2 = hashlib.sha256(img2.tobytes()).hexdigest()

            # Compare the hashes
            return "Two Images Are Same" if hash1 == hash2 else "Two Images Are Not Same"
    
    except FileNotFoundError as e:
        return f"Error: {e.filename} not found."
    except IOError as e:
        return f"Error opening image file: {e}."
    except Exception as e:
        return f"An unexpected error occurred: {e}."
#Example Usage
if __name__ == "__main__":
    # Example image paths
    img_path1 = "path/to/image1.png"
    img_path2 = "path/to/image2.png"

    # Call the function and print the result
    result = CheckImgPix(img_path1, img_path2)
    print(result)