import tkinter
import tkinter as tk

import json

def windowcreator():
    window = tk.Tk()
    window.title("Vampire Puppy")

#straininput
    strainlbl = tk.Label(text = "Select your strain")
    strainlbl.grid(column=1, row=1)



    value_inside = tk.StringVar(window)
    value_inside.set("Select a strain")

    question_menu = tk.OptionMenu(window, value_inside, *options_list)
    question_menu.grid(column = 1, row = 2)

    def print_strains():
            print("Selected Option {}".format (value_inside.get()))
            return None

    submit_button = tk.Button(window, text = "Submit", command = print_strains)
    submit_button.grid(column = 1, row = 3)

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

def tailnumtester(entry):
    global tailnum
    tailnum = entry.get()
    print("Your tail number times five is", int(tailnum) * 5)

def main():
    windowcreator()

if __name__ == "__main__":
    main()