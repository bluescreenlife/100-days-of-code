'''A simple GUI app for watermarking images.'''
from tkinter import Tk, ttk, Canvas, filedialog
from PIL import Image, ImageTk

image_to_mark = None # to be assigned PhotoImage object
watermark = None # to be assigned PhotoImage object
preview_size = (400, 400)
image_preview = None

def get_image():
    global image_to_mark
    global image_preview
    file_path = filedialog.askopenfilename(
        title='Select an Image',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        print(f'Image path obtained: {file_path}')

        # open file, create thumbnail copy and display in preview frame 
        image_to_mark = Image.open(file_path) # create a PIL image from file
        image_preview = image_to_mark.copy() # create a copy for thumbnail
        image_preview.thumbnail(preview_size) # use PIL to modify to fit in canvas dimensions
        image_preview = ImageTk.PhotoImage(image_preview) # convert to TK image
        preview_canvas.create_image(200, 200, image=image_preview) # place image on preview canvas

def get_watermark():
    pass


app = Tk()
app.title('WaterMarkIt')

# top frame for upload-images buttons and labels
upload_frame = ttk.Frame(app, width=400, height=100)
upload_frame.grid(row=0, column=1, columnspan=3, pady=10)

# bottom frame for displaying image
preview_frame = ttk.Frame(app, width=400, height=400, padding=20, borderwidth=5, relief='sunken')
preview_frame.grid(row=1, column=1, columnspan=3)

# upload image label and button
ttk.Label(upload_frame, text='Upload Image:').grid(row=0, column=0)
ttk.Button(upload_frame, text='Browse', command=get_image).grid(row=0, column=1)

# upload watermark label and button
ttk.Label(upload_frame, text='Upload Watermark:').grid(row=1, column=0, padx=10)
ttk.Button(upload_frame, text='Browse', command=get_watermark).grid(row=1, column=1)

# labels for displaying photo and watermark
preview_canvas = Canvas(preview_frame, width=400, height=400)
preview_canvas.pack(expand=True)


app.mainloop()