from tkinter import Canvas, Label, Button, Tk, Entry, PhotoImage, END, messagebox
import re
from validator_collection import checkers
import string
import random
import json

character_list = string.ascii_letters + string.digits + string.punctuation
# ---------------------------- Search function ------------------------------- #

def serch_website():
    website = website_entry.get()

    try:
        with open("passwords.json", "r") as file:
            json_passwords = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File could not found", message="There is no file where all passwords are saved")
        return 0
    try:
        the_password = json_passwords[website]
    except KeyError:
        messagebox.showinfo(title="Fail", message="There isn't any data for the looking website. Check if you typed correctly name of the website. Search system is case sensitive")
        return 0
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    messagebox.showinfo(title="Success!", message=f"Search proccess completed successfully.\nwebsite: {website}\nusername: {the_password['username']}\npassword: {the_password['password']}")









# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    the_password = []
    for _ in range(14):
        the_password.append(random.choice(character_list))
    password_entry.insert(0, "".join(the_password))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    # take information from labels
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    # check if there no empry space
    if not(website or username or password):
        messagebox.showerror(title="Error", message="Fields cannot be empty!")

    # check if email is in correct format
    elif not checkers.is_email(username):
        messagebox.showerror(title="Error", message="Wrong email")
    
    # ask user if he wants to continue 
    elif messagebox.askokcancel(title=website, message="Are you want to save it?"):
        # write taken information as a dict
        dict_to_write = {"website":website, "username":username, "password":password}
        # open file where all password are save
        read_json = {}
        # check if file exists
        try:
            with open("passwords.json", "r") as file:
                read_json = json.load(file)
        except FileNotFoundError:
            pass

        # add new data to passwords and save it
        read_json[website] = dict_to_write
        with open("passwords.json", "w") as file:
            json.dump(read_json, file, indent=4)


        # deletes all text on entries
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
# screen setting
window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

# canvas setting
cv = Canvas(width=200, height=200, bg="white", highlightthickness=0)
cv.grid(column=1, row=0, columnspan=2)
lock_picture = PhotoImage(file="logo.png")
cv.create_image(100, 100, image=lock_picture)
# cv.config(bg="black")

# website label
website_l = Label(text="Website:", bg="white", highlightthickness=0)
website_l.grid(column=0, row=1)

# ID of storage
website_entry = Entry(width=25, bd=3)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()
# email/username label
username_l = Label(text="Email:", bg="white", highlightthickness=0)
username_l.grid(column=0, row=2)
# username
username_entry = Entry(width=50, bd=3)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")
# password label
password_l = Label(text="Password:", bg="white", highlightthickness=0)
password_l.grid(column=0, row=3)
# password white space
password_entry = Entry(width=25, bd=3, selectbackground="pink")
password_entry.grid(row=3, column=1, columnspan=1, sticky="W")


# generate password button
pass_button = Button(text="Generate Password", bg="white", command=password_generator, width=15)
pass_button.grid(column=2, row=3, sticky="E")
# add button
add_button = Button(text="Add", width=43, bg="white", command=add, border=2)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

# search button 
search_button = Button(text="Search", width=15, bg="white", command=serch_website)
search_button.grid(column=2, row=1, sticky="E")

window.mainloop()