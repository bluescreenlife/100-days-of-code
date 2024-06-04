'''A simple GUI app for watermarking images.'''
from tkinter import Tk, ttk, Canvas, filedialog, StringVar, IntVar, OptionMenu
from tkinter.constants import DISABLED, NORMAL
from PIL import Image, ImageTk, ImageDraw, ImageFont
from matplotlib import font_manager

app = Tk()
app.title('WaterMarkIt')

# set up fonts
system_fonts = font_manager.findSystemFonts() # get list of truetype fonts in system
system_fonts = [name.split('/')[-1].split('.')[0] for name in system_fonts]
system_fonts.sort()
wm_font = StringVar(app)
wm_font.set('(select font)')

font_sizes = ['36', '44', '64', '81', '96', '128']
wm_size = StringVar(app)
wm_size.set('96')

# top frame for upload-images buttons and labels
button_frame = ttk.Frame(app, width=600, height=100)
button_frame.grid(row=0, column=1, columnspan=3, pady=10)

# watermark variables
watermark_str = StringVar() # reference for watermark
watermark_img = None
wm_alpha = IntVar(value=128) # RGB value 0-255

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
    '''Load from file diaglog the image the user wants to watermark.'''
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
    '''Generate the watermark image from user-chosen parameters.'''
    global watermark_str
    global watermark_img
    global wm_alpha
    global wm_font
    global wm_size
    global img_to_mark

    # set watermark parameters
    font_select = font_manager.FontProperties(family=wm_font.get()) # select font with the name user has chosen
    font_file = font_manager.findfont(font_select)
    font = ImageFont.truetype(font_file, int(wm_size.get()))
    
    text = watermark_str.get()

    position = (100, 100) # TODO: set positon to lower left quadrant of any photo
    alpha = wm_alpha.get()

    # create watermark
    watermark = Image.new('RGBA', size=img_to_mark.size, color=(255, 255, 255, 0)) # blank image for the text, transparent
    draw = ImageDraw.Draw(watermark)
    draw.text(xy=position, text=text, font=font, fill=(255, 255, 255, alpha))

    watermark_img = watermark
    generate_preview()
    generate_final_btn.config(state=NORMAL)

def generate_preview():
    '''Process the watermark and display the updated image on the canvas.'''
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

    # copy for preview
    mockup_preview = processed_image.copy()

    # resize for preview pane
    mockup_preview.thumbnail(preview_size)

    # convert to ImageTk for displaying in preview pane
    img_preview = ImageTk.PhotoImage(image=mockup_preview)

    # display in preview pane
    preview_canvas.create_image(draw_point, image=img_preview)

def export_final():
    '''Save final image as png via file dialog.'''
    global processed_image

    if processed_image:
        save_types = [('PNG Files', '*.png')]
        filepath = filedialog.asksaveasfilename(defaultextension='*.png', filetypes=save_types, title='Save Image As:')
        if filepath:
            processed_image.save(fp=filepath, format='PNG')

def capture_wm(*args):
    '''For tracing the watermark text, enabling wm generation once text entered.'''
    if watermark_str.get():
        wm_generate_btn.config(state=NORMAL)
    else:
        wm_generate_btn.config(state=DISABLED)


# upload image label and button
select_img_btn = ttk.Button(button_frame, text='Select Image', width=20, command=get_img)
select_img_btn.grid(row=0, column=0, columnspan=4, pady=(0, 10))

# watermark text input
ttk.Label(button_frame, text='WM Text:').grid(row=1, column=0, pady=(0,5))
wm_entry = ttk.Entry(button_frame, textvariable=watermark_str, width=10)
wm_entry.grid(row=1, column=1, padx=10, pady=(0,5))

# watermark scale
ttk.Label(button_frame, text='WM Opacity').grid(row=1, column=2, padx=(0, 10), pady=(0,5))
wm_alpha_scale = ttk.Scale(button_frame, length=100, from_=0, to=255, variable=wm_alpha)
wm_alpha_scale.grid(row=1, column=3, pady=(0,5))

# watermark font selection
font_menu = OptionMenu(button_frame, wm_font, *system_fonts)
font_menu.config(width=15)
font_menu.grid(row=2, column=0, columnspan=2)

# watermark size selection
ttk.Label(button_frame, text='Size:').grid(row=2, column=2)
font_sz_menu = OptionMenu(button_frame, wm_size, *font_sizes)
font_sz_menu.config(width=5)
font_sz_menu.grid(row=2, column=3)

# generate watermark label and button
wm_generate_btn = ttk.Button(button_frame, text='Generate Watermark', width=15, state=DISABLED, command=create_watermark)
wm_generate_btn.grid(row=3, column=0, columnspan=2, pady=(10,0))

# final image generation/save button
generate_final_btn = ttk.Button(button_frame, text='Export Final', width=15, state=DISABLED, command=export_final)
generate_final_btn.grid(row=3, column=2, columnspan=2, pady=(10,0))

# variable tracing and main app loop
watermark_str.trace_add(mode='write', callback=capture_wm)
app.mainloop()