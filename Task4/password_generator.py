from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list= password_letters+ password_symbols +password_numbers

    random.shuffle(password_list)

    password="".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- To SAVE PASSWORD ------------------------------- #
def save_data():

    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()

    new_data={
        website:{
            "email" : email,
            "password" : password
        }
    }

    if len(website)==0  or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oops" ,message="Please make sure you haven't left any field empty")
    
    else:
        is_ok=messagebox.askokcancel( message= website, detail=f"These are the details Entered.\n Email: {email}\n Password: {password}\n Is it Ok to Save? ")

        if is_ok:

            try:
                with open("saved_passwords.json","r") as data_file:
                    #Reading Old Data
                    data=json.load(data_file)
            except:
                with open("saved_passwords.json","w") as data_file:
                    #Reading Old Data
                    json.dump(new_data,data_file , indent=4)
            else:
                #Updating Old Data with New Data
                data.update(new_data)

                with open("saved_passwords.json","w") as data_file:
                    # Saving Updated Data 
                    json.dump(data,data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# -------------------------TO Find Password---------------------------------------------------
def find_password():
    website=website_entry.get()
    try:
        with open("saved_passwords.json", "r") as data_file :
            data=json.load(data_file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Error!!" ,message="No data file found.")

    else:   
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title= website , message=f" Email : {email}\n Password : {password}")
        
        else:
            messagebox.showinfo(title="Error!!" ,message=f"No details for {website} website exists.")



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


canvas=Canvas(width=200, height=200 )
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)


# Label : website
website_label=Label(text="Website : ")
website_label.grid(row=1, column=0)
website_label.config(pady=10)



# Label : Email/UserName
email_label=Label(text="Email/UserName : ")
email_label.grid(row=2, column=0)
website_label.config(pady=10)

# Label : Password
password_label=Label(text="Password : ")
password_label.grid(row=3, column=0)
website_label.config(pady=10)


# Input: website
website_entry=Entry(width=21)
website_entry.grid(row=1, column=1 , sticky="ew")
website_entry.focus()
website_label.config(pady=10)

# Input: Email:
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1 , columnspan=2 , sticky="ew")
email_entry.insert(0 ,"tanmayborse28@gmail.com")
website_label.config(pady=10)



# Input: Password:
password_entry=Entry(width=21)
password_entry.grid(row=3, column=1 , sticky="ew")
website_label.config(pady=10)




#Button1

button1=Button(text="Generate Password", command=generate_password)
button1.grid(row=3,column=2,  sticky="ew")
website_label.config(pady=10)

# Button2

button2=Button(text="ADD", width=35,command=save_data)
button2.grid(row=4,column=1, columnspan=2 , sticky="ew")
website_label.config(pady=10)


#Button3
button3=Button(text="Search",command=find_password)
button3.grid(row=1,column=2, sticky="ew")
website_label.config(pady=10)


window.mainloop()
