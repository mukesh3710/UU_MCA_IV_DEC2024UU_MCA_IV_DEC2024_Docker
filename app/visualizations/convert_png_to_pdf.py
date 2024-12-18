# visualizations/convert_png_to_pdf.py

from PIL import Image

def convert_png_to_pdf(png_files, output_pdf):
    """
    Converts a list of PNG files to a single PDF file.

    Args:
        png_files (list): List of paths to the PNG files.
        output_pdf (str): Path to save the generated PDF.
    """
    images = []
    for png_file in png_files:
        img = Image.open(png_file)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        images.append(img)
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
