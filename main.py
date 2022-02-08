import time
from tkinter import *
from PIL import ImageTk, Image
from utility import get_fuzzy_time, plot_fuzzy_minutes

root = Tk()
root.title("Fuzzy Clock")
root.geometry("1024x720")


while True:
    fuzzy_time = get_fuzzy_time()
    plot_fuzzy_minutes()

    my_label = Label(root, text=fuzzy_time)
    btn_quit = Button(root, text="Exit", command=root.quit)
    my_image = ImageTk.PhotoImage(Image.open("graph.png"))
    my_img_label = Label(image=my_image)

    my_img_label.pack()
    my_label.pack()
    btn_quit.pack()

    root.update_idletasks()
    root.update()

    time.sleep(5)
    btn_quit.pack_forget()
    my_label.pack_forget()
    my_img_label.pack_forget()



