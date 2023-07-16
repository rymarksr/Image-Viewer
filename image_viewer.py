from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")

frame = LabelFrame(root, bg="#FFEFD5")
frame.pack()

img1 = ImageTk.PhotoImage(Image.open("mywalldisplays/10876.png"))
img2 = ImageTk.PhotoImage(Image.open("mywalldisplays/Beautiful-natural-landscape-Stock-Photo-03.jpg"))
img3 = ImageTk.PhotoImage(Image.open("mywalldisplays/depositphotos_29984153-stock-photo-spring-nature-beautiful-landscape-green.jpg"))
img4 = ImageTk.PhotoImage(Image.open("mywalldisplays/landscape-tree-nature-forest-wilderness-mountain-99087-pxhere.com_-600x400.jpg"))
img5 = ImageTk.PhotoImage(Image.open("mywalldisplays/5OlUiS.png"))
img6 = ImageTk.PhotoImage(Image.open("mywalldisplays/Beautiful_Landscape_Painting.jpg"))

img_list = [img1, img2, img3, img4, img5, img6]

label = Label(frame, image=img1, bd=5)
label.grid(row=0, column=0, columnspan=3)

status = Label(frame, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, bg="#F0FFF0", anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def forward(img_number):
    global label
    global b_back
    global b_forward
    global status

    label.grid_forget()
    label = Label(frame, image=img_list[img_number-1], bd=5)
    label.grid(row=0, column=0, columnspan=3)
    b_forward = Button(frame, text=">>", command=lambda: forward(img_number+1), fg="#1E90FF")
    b_forward.grid(row=1, column=2)
    b_back = Button(frame, text="<<", command=lambda: back(img_number-1), fg="#1E90FF")
    b_back.grid(row=1, column=0)

    status = Label(frame, text="Image " + str(img_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, bg="#F0FFF0", anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    if img_number == 6:
        b_forward = Button(frame, text=">>", state=DISABLED, fg="#1E90FF")
        b_forward.grid(row=1, column=2)


def back(img_number):
    global label
    global b_back
    global b_forward
    global status

    label.grid_forget()
    label = Label(frame, image=img_list[img_number - 1], bd=5)
    label.grid(row=0, column=0, columnspan=3)
    b_forward = Button(frame, text=">>", command=lambda: forward(img_number + 1), fg="#1E90FF")
    b_forward.grid(row=1, column=2)
    b_back = Button(frame, text="<<", command=lambda: back(img_number - 1), fg="#1E90FF")
    b_back.grid(row=1, column=0)

    status = Label(frame, text="Image " + str(img_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, bg="#F0FFF0", anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    if img_number == 1:
        b_back = Button(frame, text="<<", state=DISABLED, fg="#1E90FF")
        b_back.grid(row=1, column=0)


b_back = Button(frame, text="<<", command=back, state=DISABLED, fg="#1E90FF")
b_back.grid(row=1, column=0)
b_exit = Button(frame, text="exit", command=root.quit, fg="#DC143C")
b_exit.grid(row=1, column=1, pady=10)
b_forward = Button(frame, text=">>", command=lambda: forward(2), fg="#1E90FF")
b_forward.grid(row=1, column=2)

root.mainloop()
