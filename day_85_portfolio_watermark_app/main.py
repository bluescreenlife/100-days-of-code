'''A simple GUI app for watermarking images.'''
from tkinter import W, Tk, ttk, Canvas, filedialog, StringVar, IntVar
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

app = Tk()
app.title('WaterMarkIt')

# top frame for upload-images buttons and labels
button_frame = ttk.Frame(app, width=600, height=100)
button_frame.grid(row=0, column=1, columnspan=3, pady=10)

# watermark variables
watermark_str = StringVar(value='example') # reference for watermark
watermark_img = None
wm_alpha = IntVar(value=128) # RGB value 0-255
wm_label = ttk.Label(button_frame, text='WM Opacity').grid(row=0, column=3, padx=10)
watermark_coords = []
mockup_preview = None

# image variables
img_to_mark = None # reference for image
processed_image = None

# preview variables
img_preview = None # reference for preview pane image
preview_size = (600, 400)
draw_point = tuple(x/2 for x in preview_size)


# bottom frame for displaying image
preview_frame = ttk.Frame(app, width=preview_size[0], height=preview_size[1], padding=0, borderwidth=5, relief='sunken')
preview_frame.grid(row=1, column=1, columnspan=3)

# canvas for displaying preview
preview_canvas = Canvas(preview_frame, width=preview_size[0], height=preview_size[1], background='#4b4b4b')
preview_canvas.pack(expand=True)

def get_img():
    global img_to_mark
    global img_preview
    global draw_point

    # get file path of image
    file_path = filedialog.askopenfilename(
        title='Select an Image',
        filetypes=(('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('PNG', '*.png'), ('GIF', '.gif'))
    )

    if file_path:
        # confirm file path and set up image as PIL image
        print(f'Image path obtained: {file_path}')

        img_to_mark = Image.open(file_path) # open as PIL image, assign to image reference

        # place preview of image on canvas
        img_preview = img_to_mark.copy()
        img_preview.thumbnail(preview_size) # set to canvas size
        img_preview = ImageTk.PhotoImage(image=img_preview) # convert to photoimage
        preview_canvas.create_image(draw_point, image=img_preview) # draw image

def create_watermark():
    global watermark_str
    global watermark_img
    global wm_alpha
    global img_to_mark

    # set watermark parameters
    # font = ImageFont.truetype('arial.ttf', 36) # TODO: implement user font selection
    font = ImageFont.load_default(size=110)
    text = watermark_str.get()
    print(f'Watermark text: {text}')

    position = (100, 100) # TODO: set positon to lower left quadrant of any photo
    alpha = wm_alpha.get()

    # create watermark
    watermark = Image.new('RGBA', size=img_to_mark.size, color=(255, 255, 255, 0)) # blank image for the text, transparent
    draw = ImageDraw.Draw(watermark)
    draw.text(xy=position, text=text, font=font, fill=(255, 255, 255, alpha))

    watermark_img = watermark
    generate_preview()


def generate_preview():
    global watermark_img
    global mockup_preview
    global img_to_mark
    global img_preview
    global preview_canvas
    global preview_size
    global draw_point
    global processed_image


    # layer images
    processed_image = Image.alpha_composite(img_to_mark.convert('RGBA'), watermark_img)

    # save full image
    processed_image.save(fp='./mockup.png', format='PNG')

    # copy for preview
    mockup_preview = processed_image.copy()

    # resize for preview pane
    mockup_preview.thumbnail(preview_size)

    # convert to ImageTk for displaying in preview pane
    img_preview = ImageTk.PhotoImage(image=mockup_preview)

    # display in preview pane
    preview_canvas.create_image(draw_point, image=img_preview)


def export_final():
    global processed_image

    if processed_image:
        save_types = [('PNG Files', '*.png')]
        filepath = filedialog.asksaveasfilename(defaultextension='*.png', filetypes=save_types, title='Save Image As:')
        if filepath:
            processed_image.save(fp=filepath, format='PNG')



# upload image label and button
ttk.Label(button_frame, text='Upload Image:').grid(row=0, column=0)
ttk.Button(button_frame, text='Browse', command=get_img).grid(row=0, column=1)

# generate watermark label and button
ttk.Label(button_frame, text='Generate Watermark:').grid(row=1, column=3, padx=10)
ttk.Button(button_frame, text='Generate', command=create_watermark).grid(row=1, column=4)

# watermark scale
wm_alpha_scale = ttk.Scale(button_frame, length=100, from_=0, to=255, variable=wm_alpha).grid(row=0, column=4)

# watermark text input
ttk.Label(button_frame, text='WM Text:').grid(row=1, column=0)
wm_entry = ttk.Entry(button_frame, textvariable=watermark_str, width=10).grid(row=1, column=1, padx=10)

# buttons for generating preview/saving final
# ttk.Button(button_frame, text='Update Preview', command=generate_preview).grid(row=3, column=0, columnspan=2, 
#                                                                                  pady=(10,0))
ttk.Button(button_frame, text='Export Final', width=20, command=export_final).grid(row=2, column=1, columnspan=3,
                                                                        pady=(10,0))



app.mainloop()