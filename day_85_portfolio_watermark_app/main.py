'''A simple GUI app for watermarking images.'''
from tkinter import W, Tk, ttk, Canvas, filedialog, StringVar, IntVar
from PIL import Image, ImageTk, ImageDraw, ImageFont

app = Tk()
app.title('WaterMarkIt')

# top frame for upload-images buttons and labels
button_frame = ttk.Frame(app, width=600, height=100)
button_frame.grid(row=0, column=1, columnspan=3, pady=10)

# watermark variables
watermark_str = StringVar() # reference for watermark
watermark_img = None
wm_opac = IntVar(value=128) # RGB value 0-255
wm_label = ttk.Label(button_frame, text='WM Opacity').grid(row=0, column=3, padx=10)
watermark_coords = []

# image variables
img_to_mark = None # reference for image

# preview variables
img_preview = None # reference for preview pane image
preview_size = (600, 400)

# bottom frame for displaying image
preview_frame = ttk.Frame(app, width=preview_size[0], height=preview_size[1], padding=0, borderwidth=5, relief='sunken')
preview_frame.grid(row=1, column=1, columnspan=3)

def get_img():
    global img_to_mark

    # get file path of image
    file_path = filedialog.askopenfilename(
        title='Select an Image',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        # confirm file path and set up image as PIL image
        print(f'Image path obtained: {file_path}')

        img_to_mark = Image.open(file_path) # open as PIL image, assign to image reference


def get_watermark_img():
    global watermark_img

    # get file path of watermark
    file_path = filedialog.askopenfilename(
        title='Select a Watermark',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        # confirm file path and set up watermark as PIL image
        print(f'Watermark path obtained: {file_path}')

        watermark_img = Image.open(file_path) # open watermark as PIL image
        # TODO: make watermark size a %age of image size rather than always 50x50
        watermark_img.thumbnail((50, 50)) # convert to thumbnail size
        watermark_img.putalpha(wm_opac) # set opacity

def generate_preview():
    pass

def export_final():
    pass


# upload image label and button
ttk.Label(button_frame, text='Upload Image:').grid(row=0, column=0)
ttk.Button(button_frame, text='Browse', command=get_img).grid(row=0, column=1)

# upload watermark label and button
ttk.Label(button_frame, text='Upload Watermark:').grid(row=1, column=0, padx=10)
ttk.Button(button_frame, text='Browse', command=get_watermark_img).grid(row=1, column=1)

# watermark scale
wm_opac_scale = ttk.Scale(button_frame, length=100, from_=0, to=255, variable=wm_opac).grid(row=0, column=4)

# watermark text input
ttk.Label(button_frame, text='WM Text:').grid(row=1, column=3)
wm_entry = ttk.Entry(button_frame, textvariable=watermark_str, width=10).grid(row=1, column=4, padx=10)

# buttons for generating preview/saving final
ttk.Button(button_frame, text='Generate Preview', command=generate_preview).grid(row=3, column=0, columnspan=2, 
                                                                                 pady=(10,0))
ttk.Button(button_frame, text='Export Final', command=export_final).grid(row=3, column=2, columnspan=2, 
                                                                        pady=(10,0))

# canvas for displaying preview
preview_canvas = Canvas(preview_frame, width=preview_size[0], height=preview_size[1], background='#4b4b4b')
preview_canvas.pack(expand=True)


app.mainloop()