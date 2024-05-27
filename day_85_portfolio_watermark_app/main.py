'''A simple GUI app for watermarking images.'''
from tkinter import Tk, ttk, Canvas, filedialog
from PIL import Image, ImageTk

image_to_mark = None # to be assigned PhotoImage object
image_preview = None # reference for preview pane image

watermark = None # to be assigned PhotoImage object
watermark_preview = None # reference for preview pane watermark

preview_size = (400, 400)
watermark_preview_size = tuple(int(x/4) for x in preview_size)
preview_center = tuple(int(x/2) for x in preview_size)

watermark_coords = ((preview_center[0] * .25), (preview_center[1]) * .75) # need fix placement

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
        preview_canvas.create_image(preview_center, image=image_preview) # place image on preview canvas

def get_watermark():
    global watermark
    global watermark_preview
    file_path = filedialog.askopenfilename(
        title='Select a Watermark',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        print(f'Watermark path obtained: {file_path}')

        # open file, create thumbnail copy and display in preview frame 
        watermark = Image.open(file_path) # create a PIL image from file
        watermark_preview = watermark.copy() # create a copy for thumbnail
        watermark_preview.thumbnail(watermark_preview_size) # set watermark to 25% of preview size
        watermark_preview.putalpha(128) # set watermark to half transparency
        watermark_preview = ImageTk.PhotoImage(watermark_preview) # convert to TK image
        preview_canvas.create_image(watermark_coords, image=watermark_preview) # place image on preview canvas


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