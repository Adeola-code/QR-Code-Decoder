from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import shutil
import os


def open_image():
    file_path=filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        #This was added to check if it is an image
        allowed_extensions=('.png','.jpg','.jpeg','.gif','.bmp')
        if not file_path.lower().endswith(allowed_extensions):
            print('Error: Selected file is mot an image.')
            return
              
        
        image = Image.open(file_path)
        image.thumbnail((300, 300)) #RESIZE THE IMAGE FOR DISPLAY
        
    
        img_label = tk.Label(root, image=ImageTk.PhotoImage(image))
        img_label.pack()
        

        decoded_result = decode(image)
        if not decoded_result:
            print("No QR Code detected in this image. ")
        else:
            extracted_data= [result.data.decode('utf-8') for result in decoded_result]
            print("QR code(s) detected:", extracted_data)


root= tk.Tk()
root.title("Image Upload")

button = tk.Button(root, text="Open Image", command=open_image)
button.pack()

root.mainloop()
