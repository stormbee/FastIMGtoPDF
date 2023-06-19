import tkinter as tk
from PIL import Image, UnidentifiedImageError
from tkdnd import TkinterDnD, DND_FILES
import os
import shutil
import sys


def convert_to_pdf(image_path):
    try:
        image = Image.open(image_path)
        pdf_path = image_path.replace(image_path.split('.')[-1], "pdf")
        image.save(pdf_path, "PDF", resolution=100.0)
        return pdf_path
    except UnidentifiedImageError:
        return None

 
def drop_inside_window(event):
    file_pathes = [file_path.strip('{').strip('}') for file_path in event.data.split('} {')]
    process_files(file_pathes)
 

def process_files(file_pathes):
    
    for file_path in file_pathes:
        if file_path.endswith(tuple(listOfExtensions)):
            pdf_path = convert_to_pdf(file_path)
            if pdf_path:
                desktop_path = os.path.expanduser("~/Desktop")
                dest_path = os.path.join(desktop_path, os.path.basename(pdf_path))
                shutil.move(pdf_path, dest_path)
    root.destroy()

listOfExtensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif"]
root = TkinterDnD.Tk()
# root.geometry("300x300")
root.withdraw() # hide the root window

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop_inside_window)
if len(sys.argv) > 1:
    file_paths = sys.argv[1:]
    process_files(file_paths)
    root.quit()  # Exit the main event loop
if len(sys.argv) <= 1:
    root.destroy() # show the root window
root.mainloop()
