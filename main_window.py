import tkinter as tk
from PIL import Image, ImageTk
from HtmlTest import HTMLTEST
from CssTest import CSSTest
from JavaScriptTest import JavaScriptTest
def on_left_button_click():
    quiz_window = tk.Toplevel(window)
    HTMLTEST(quiz_window)

def on_middle_button_click():
    quiz_window = tk.Toplevel(window)
    CSSTest(quiz_window)

def on_right_button_click():
    quiz_window = tk.Toplevel(window)
    JavaScriptTest(quiz_window)

def create_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)


window = tk.Tk()
window.title("Тест по Front-end Разработке")
window.geometry("620x550")


icon_image = Image.open("iconn.ico")
icon_image = icon_image.resize((32, 32))
icon_image = ImageTk.PhotoImage(icon_image)
window.iconphoto(True, icon_image)

background_image_main = Image.open("background_main2.png")
background_image_main = background_image_main.resize((620, 550))
background_image_main = ImageTk.PhotoImage(background_image_main)
background_label_main = tk.Label(window, image=background_image_main)
background_label_main.place(relwidth=1, relheight=1)


left_image = Image.open("html.png")
left_image = left_image.resize((100, 100))
left_image = ImageTk.PhotoImage(left_image)
left_button = tk.Button(window, text="HTML", image=left_image, compound=tk.TOP, command=on_left_button_click)

middle_image = Image.open("CSS.png")
middle_image = middle_image.resize((100, 100))
middle_image = ImageTk.PhotoImage(middle_image)
middle_button = tk.Button(window, text="CSS", image=middle_image, compound=tk.TOP,
                          command=on_middle_button_click)

right_image = Image.open("JavaScript.png")
right_image = right_image.resize((100, 100))
right_image = ImageTk.PhotoImage(right_image)
right_button = tk.Button(window, text="JAVASCRIPT", image=right_image, compound=tk.TOP, command=on_right_button_click)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)


window.rowconfigure(0, weight=1)


left_button.grid(row=0, column=0, padx=10, pady=10)
middle_button.grid(row=0, column=1, padx=10, pady=10)
right_button.grid(row=0, column=2, padx=10, pady=10)


window.mainloop()