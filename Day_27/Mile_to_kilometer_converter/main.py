from tkinter import Tk, Label, Button, Entry

def main():
    # window settings
    window = Tk()
    window.minsize(width=200, height=100)
    window.title("Mile to kilometer converter")
    window.config(padx=30, pady=20)

    # function that converts miles to kilometers 
    def converter():
        try:
            miles = float(miles_to_convert.get())
        except ValueError:
            miles = "error"
        else:
            miles =f"{(miles * 1.6):.2f}"
        km_result["text"] = miles
    
    # km label
    km_label = Label(text="km")
    km_label.grid(column=2, row=1)
    # miles label
    mile_label = Label(text="miles")
    mile_label.grid(column=2, row=0)
    # label that shows the result of conversation
    km_result = Label(text="0")
    km_result.grid(column=1, row=1)
    # is equal to label
    is_equal = Label(text="is equal to")
    is_equal.grid(column=0, row=1)
    # space where you write miles to be converted into km
    miles_to_convert = Entry(width=14)
    miles_to_convert.insert(-1, "0")
    miles_to_convert.grid(column=1, row=0)
    # convert button
    convert = Button(text="Convert", command=converter)
    convert.grid(column=1, row=2)


    window.mainloop()



if __name__ == "__main__":
    main()