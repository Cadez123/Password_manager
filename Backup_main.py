from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # Generate letters
    [password_list.append(choice(letters)) for x in range(randint(8, 10))]

    # Generate symbols
    [password_list.append(choice(symbols)) for x in range(randint(2, 4))]

    # Generate numbers
    [password_list.append(choice(numbers)) for x in range(randint(2, 4))]

    # Shuffle the characters in the password list and join them into a string
    shuffle(password_list)
    generated_password = "".join(password_list)

    # Empty the password field
    password_text.delete(0,'end')

    # Insert the new password
    password_text.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Save inputs as variables
    website = website_text.get()
    email = username_text.get()
    password = password_text.get()
    new_data = {
        website:{
            'email':email,
            'password':password,
        }}

    # Make sure important fields are not empty
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title='Error', message='You forgot to add a password or name of website.')
    else:
        # Update the data
        with open('Password_manager.json','r') as data_file:
            # Open json file and add the new data
            data = json.load(data_file)
            data.update(new_data)

        # Save the date
        with open('Password_manager.json','w') as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

        password_text.delete(0,'end')
        website_text.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title('Password manager')
window.config(pady=50, padx=50)

# Image
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

# Website label and input
website = Label(text='Website:')
website.grid(row=1, column=0)

website_text = Entry(width=42)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

# Username label and input
username = Label(text='Email/Username:')
username.grid(row=2, column=0)

username_text = Entry(width=42)
username_text.grid(row=2, column=1, columnspan=2)
username_text.insert(0,'example@email.com')

# Password label and input
password = Label(text='Password:')
password.grid(row=3, column=0)

password_text = Entry(width=24)
password_text.grid(row=3, column=1)


# Generate password button
password_button = Button(text='Generate Password', width=14, command=generate_password)
password_button.grid(row=3, column=2)

# Add button
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()



'''for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)'''