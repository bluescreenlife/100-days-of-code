'''A simple GUI app for watermarking images.'''
from tkinter import PhotoImage, Tk
from tkinter import ttk, filedialog
import PIL

image_to_mark = None # to be assigned PhotoImage object
watermark = None # to be assigned PhotoImage object

def get_image():
    global image_to_mark
    file_path = filedialog.askopenfilename(
        title='Select an Image',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        print(f'Image path obtained: {file_path}')

        # update image window label to display this photo
        image_to_mark = PhotoImage(file=file_path)
        image_label.config(image=image_to_mark)
        image_label['image'] = image_to_mark

def get_watermark():
    global watermark
    file_path = filedialog.askopenfilename(
        title='Select a Watermark',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        print(f'Watermark path obtained: {file_path}')

        # update image window label to display this photo
        watermark = PhotoImage(file=file_path)
        wm_label.config(image=watermark)
        wm_label['image'] = watermark


app = Tk()
app.title('WaterMarkIt')

# top frame for upload-images buttons and labels
upload_frame = ttk.Frame(app, width=200, height=100)
upload_frame.grid(row=0, column=1, columnspan=3, pady=10)

# bottom frame for displaying image
preview_frame = ttk.Frame(app, width=400, height=200, padding=20, borderwidth=5, relief='sunken')
preview_frame.grid(row=1, column=1, columnspan=3)

# upload image label and button
ttk.Label(upload_frame, text='Upload Image:').grid(row=0, column=0)
ttk.Button(upload_frame, text='Browse', command=get_image).grid(row=0, column=1)

# upload watermark label and button
ttk.Label(upload_frame, text='Upload Watermark:').grid(row=1, column=0, padx=10)
ttk.Button(upload_frame, text='Browse', command=get_watermark).grid(row=1, column=1)

# labels for displaying photo and watermark
image_label = ttk.Label(preview_frame)
wm_label = ttk.Label(preview_frame)



app.mainloop()