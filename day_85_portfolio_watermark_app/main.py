'''A simple GUI app for watermarking images.'''
from tkinter import Tk
from tkinter import ttk, filedialog
import PIL

def upload_photo():
    file_path = filedialog.askopenfilename(
        title='Select an Image',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'))
    )

    if file_path:
        # update image window label to display this photo
        pass

def display_photo():
    pass

app = Tk()
app.title('WaterMarkIt')

# top frame for upload-images buttons and labels
upload_frame = ttk.Frame(app, width=200, height=100)
upload_frame.grid(row=0, column=1, columnspan=3, pady=10)

# bottom frame for displaying image
photo_frame = ttk.Frame(app, width=400, height=200, padding=20, borderwidth=5, relief='sunken')
photo_frame.grid(row=1, column=1, columnspan=3)

# photo label and button
photo_label = ttk.Label(upload_frame, text='Upload Photo:')
photo_label.grid(row=0, column=0)

photo_button = ttk.Button(upload_frame, text='Browse', command=upload_photo)
photo_button.grid(row=0, column=1)

# watermark label and button
wm_label = ttk.Label(upload_frame, text='Upload Watermark:')
wm_label.grid(row=1, column=0, padx=10)

wm_button = ttk.Button(upload_frame, text='Browse')
wm_button.grid(row=1, column=1)



app.mainloop()