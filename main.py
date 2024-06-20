from tkinter import *
from time import *
window = Tk()
window.title("Clock")

def update():
    while True:
        timeString = strftime("%I" + " : " + "%M" + " : " + "%S")
        timeLabel.config(text=timeString)
        window.update()
        dayString = strftime("%A")
        dayLabel.config(text=dayString)
        dateString = strftime("%B" + " " + "%d" + ", " + "%Y")
        dateLabel.config(text=dateString)


timeLabel = Label(window, font=("Impact",50), foreground="yellow", background="black", width=15)
timeLabel.pack()
dayLabel = Label(window, font=("Impact",30), foreground="black", background="white", width=24)
dayLabel.pack()
dateLabel = Label(window, font=("Impact",50), foreground="black", background="white", width=15)
dateLabel.pack()

update()
window.mainloop()