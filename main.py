import random
import tkinter as tk

def dice():
    number = random.randint(1,6)
    label.config(text=str(number), font=("Arial", 100))

root = tk.Tk()
root.title("roll the dice")

label = tk.Label(root, text="", font=("Arial", 100))
label.pack(pady=20)

button = tk.Button(root,text=("dice"), command=dice, font=("Arial", 20))
button.pack()


root.mainloop()