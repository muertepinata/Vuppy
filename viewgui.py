import tkinter as tk

def enterclicked(entry):
    global tailnum
    tailnum = entry.get()
    print("Your tail number times five is", int(tailnum) * 5)

def inputtest():
    window = tk.Tk()
    window.title("Vampire Puppy")

#strain
    strainlbl = tk.Label(text="Select your strain.")
    strainlbl.grid(column=1, row = 1)

#tailnum input
    taillbl = tk.Label(text="Enter your tail number")
    entry = tk.Entry()
    button = tk.Button(window, text = "Enter", command=lambda:enterclicked(entry))

    taillbl.grid(column =3, row = 1)
    entry.grid(column = 3, row = 2)
    button.grid(column = 3, row = 3)

#go button
    golabel= tk.Label(text="Click 'go' when you're \n ready to calculate.")
    golabel.grid(column=2, row=4)
    gobutton = tk.Button(window, text = 'Go')
    gobutton.grid(column=2, row=5 )

    window.mainloop()

    return tailnum

def main():
    inputtest()

if __name__ == "__main__":
    main()