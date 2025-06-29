from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import random
import json
# ---------------------------- CONSTANTS ------------------------------- #
FONT = "Calibri"
FONT_SIZE = 12
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- CLEAR FIELDS ------------------------------- #
def clear():
    input1.delete(0, END)
    input2.delete(0, END)
    input3.delete(0, END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
passwordPrelim = []
passwordFinal = ""
def passwordGenerator():
    global passwordPrelim,passwordFinal
    input3.delete(0, END)
    passwordPrelim.clear()
    passwordFinal = ""
    for value in range(int(spinbox1.get())):
        passwordPrelim.append(LETTERS[random.randint(0, len(LETTERS) - 1)])
    for value in range(int(spinbox2.get())):
        passwordPrelim.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
    for value in range(int(spinbox3.get())):
        passwordPrelim.append(SYMBOLS[random.randint(0, len(SYMBOLS) - 1)])
    random.shuffle(passwordPrelim)
    for value in passwordPrelim:
        passwordFinal += value
    input3.insert(END,string=passwordFinal)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global passwordPrelim, passwordFinal
    inputWebsite = input1.get().strip().lower()
    inputUsernameEmail = input2.get().strip()
    inputPassword = input3.get().strip()
    jsonData = {
        inputWebsite: {
            "Email/Username": inputUsernameEmail,
            "Password": inputPassword
        }
    }
    if len(inputWebsite) < 1 or len(inputUsernameEmail) < 1 or len(inputPassword) < 1:
        error = messagebox.showerror(title="Error!",message="Do not leave any fields blank!")
        if error:
            clear()
    else:
        question = messagebox.askokcancel(title="Confirmation",message=f"The following information will be saved to "
        f"SavedPasswords.json:\n"
        f"\nWebsite: {inputWebsite}\nEmail/Username: {inputUsernameEmail}\nPassword: {inputPassword}\n"
        f"\nDo you want to proceed with saving this information?")
        if question:
            try:
                with open("SavedPasswords.json",mode="r") as docs1:
                    data = json.load(docs1) #Reads old data
                    data.update(jsonData) #Updates old data with new input data
            except JSONDecodeError:
                with open("SavedPasswords.json",mode="w") as docs1:
                    json.dump(jsonData, docs1, indent=4) #Creates JSON file and writes to it in the event the file is empty.
            except FileNotFoundError:
                with open("SavedPasswords.json",mode="w") as docs1:
                    json.dump(jsonData, docs1, indent=4) #Creates JSON file and writes to it in the event the file doesn't exist.
            else:
                with open("SavedPasswords.json",mode="w") as docs2:
                    json.dump(data, docs2, indent=4)  #Saves updated data to JSON file
            finally:
                clear()
        else:
            clear()
# ---------------------------- JSON FILE SEARCH ------------------------------- #
def searchJSON():
    inputWebsite = input1.get().strip().lower()
    selection = radio_state.get()
    try:
        with open("SavedPasswords.json", mode="r") as docs1:
            data = json.load(docs1)
            keysList = list(data.keys())
            success = 1
            if inputWebsite == "all":
                for n in range(0,len(keysList)):
                    input1.delete(0,END)
                    input2.delete(0, END)
                    input3.delete(0, END)
                    storedEmailUsername = data[keysList[n]]["Email/Username"]
                    storedPassword = data[keysList[n]]["Password"]
                    input1.insert(END, string=keysList[n])
                    input2.insert(END, string=storedEmailUsername)
                    input3.insert(END, string=storedPassword)
                    window.clipboard_clear()
                    window.clipboard_append(input3.get())
                    messagebox.showinfo(title=f"Information for {keysList[n]}",
                    message=f"Email/Username for {keysList[n]}: \n{storedEmailUsername}"
                    f"\n\nPassword for {keysList[n]}: \n{storedPassword}\n\n"
                    f"PASSWORD COPIED TO CLIPBOARD!!!")
            elif selection == 1:
                if inputWebsite in keysList:
                    input1.delete(0, END)
                    input2.delete(0, END)
                    input3.delete(0, END)
                    storedEmailUsername = data[inputWebsite]["Email/Username"]
                    storedPassword = data[inputWebsite]["Password"]
                    input1.insert(END, string=inputWebsite)
                    input2.insert(END, string=storedEmailUsername)
                    input3.insert(END, string=storedPassword)
                    window.clipboard_clear()
                    window.clipboard_append(input3.get())
                    messagebox.showinfo(title=f"Information for {inputWebsite}",
                    message=f"Email/Username for {inputWebsite}: \n{storedEmailUsername}"
                    f"\n\nPassword for {inputWebsite}: \n{storedPassword}\n\n"
                    f"PASSWORD COPIED TO CLIPBOARD!!!")
                else:
                    raise KeyError
            elif selection == 2:
                for n in range(0, len(keysList) + 1):
                    if n == len(keysList):
                        success -= 1
                        raise KeyError
                    elif inputWebsite in keysList[n]:
                        break
                if success == 1:
                    for n in range(0,len(keysList) + 1):
                        if inputWebsite in keysList[n]:
                            input1.delete(0, END)
                            input2.delete(0, END)
                            input3.delete(0, END)
                            storedEmailUsername = data[keysList[n]]["Email/Username"]
                            storedPassword = data[keysList[n]]["Password"]
                            input1.insert(END, string=keysList[n])
                            input2.insert(END, string=storedEmailUsername)
                            input3.insert(END, string=storedPassword)
                            window.clipboard_clear()
                            window.clipboard_append(input3.get())
                            messagebox.showinfo(title=f"Information for {keysList[n]}",
                            message=f"Email/Username for {keysList[n]}: \n{storedEmailUsername}"
                            f"\n\nPassword for {keysList[n]}: \n{storedPassword}\n\n"
                            f"PASSWORD COPIED TO CLIPBOARD!!!")
    except KeyError:
        messagebox.showerror(title="Error", message=f"Information for \"{inputWebsite}\" is not in SavedPasswords.json!")
    except JSONDecodeError:
        messagebox.showerror(title="Error", message=f"Information for \"{inputWebsite}\" is not in SavedPasswords.json!")
    except IndexError:
        pass
    finally:
        clear()
# ---------------------------- HOW TO USE APP ------------------------------- #
def howToUse():
    win = Tk()
    win.title("Welcome to MyPass Password Manager!")
    Label(win, text="Instructions", font=(FONT, FONT_SIZE),
          background='green', foreground="white").grid(column=0, row=0)

    text_area = scrolledtext.ScrolledText(win, wrap=WORD, width=75, height=30, font=(FONT, 15))

    text_area.grid(column=0, pady=10, padx=10)

    text_area.insert(INSERT, "This a simple, "
f"easy to use locally-hosted password manager. Since it's locally hosted, this program is immune to the "
f"vulnerabilities faced by online or cloud-based password managers.\n\nTo use this app, simply enter in your account "
f"credentials for a particular website. Click on the 'Generate Password' button to randomly generate a password."
f" You can adjust how many letters, numbers, and symbols you want in your password by interacting with the widgets "
f"at the top of the app.\n\nBy clicking on the 'Save' button, the information you entered will be saved to the "
f"locally-stored 'SavedPasswords.json' file. Make sure to not leave any fields blank when saving your information.\n\n"
f"By clicking on the 'Search' button, the program will be able to search 'SavedPasswords.json' for the credentials "
f"you entered for a particular website and display it to the screen. Simply type the name of the website you want to"
f" search for into the Website text field BEFORE pressing the 'Search' button.\n\nIf you want to look up the credentials"
f" for ALL of the websites you've saved to 'SavedPasswords.json', then type 'all' (no quotation marks) into the"
f" Website text field.\n\nThe search functionality also comes with Complete Match and Partial Match search features."
f" For example, choose 'Complete Match' if you want the program to search for and display information for a single "
f"particular website. However, choose 'Partial Match' if you want the program to search for and display information"
f" for multiple websites at once. As an example, typing '.com' into the Website text field while 'Partial Match' is"
f" selected will cause the program to search and display information for all websites saved to 'SavedPasswords.json' "
f"that contain '.com' in their name.\n\nAs 'SavedPasswords.json' stores your passwords in cleartext, I highly"
f" suggest you encrypt the folder you designate to contain this program and 'SavedPasswords.json'."
f"\n\nCyberspace can be a dangerous place at times. Stay safe and stay vigilant out there!")
    text_area.configure(state ='disabled')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20,pady=20)
window.minsize(width=500,height=400)
window.maxsize(width=500,height=400)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logoImg)
canvas.pack()

label1 = Label(text="Website:",font=(FONT,FONT_SIZE))
label1.place(x=50,y=200)
label2 = Label(text="Email/Username:",font=(FONT,FONT_SIZE))
label2.place(x=-7, y=228)
label3 = Label(text="Password:",font=(FONT,FONT_SIZE))
label3.place(x=43,y=258)
label4 = Label(text="# of letters:",font=(FONT,FONT_SIZE))
label4.place(x=-20,y=-10)
label5 = Label(text="# of numbers:",font=(FONT,FONT_SIZE))
label5.place(x=175,y=-10)
label6 = Label(text="# of symbols:",font=(FONT,FONT_SIZE))
label6.place(x=345,y=-10)
label7 = Label(text="Interact with the widgets at the top to configure password character options.",font=(FONT,11))
label7.place(x=0,y=360)
label8 = Label(text="Select Search Mode:",font=(FONT,FONT_SIZE))
label8.place(x=315,y=75)

input1 = Entry(width=25)
input1.place(x=125,y=196)
input1.focus()
input2 = Entry(width=37)
input2.place(x=125,y=225)
input3 = Entry(width=21)
input3.place(x=125,y=255)

button1 = Button(text="Generate Password",width=13,font=(FONT,10),command=passwordGenerator)
button1.place(x=308,y=254)
button2 = Button(text="Save",width=34,command=save)
button2.place(x=127,y=290)
button3 = Button(text="Search",width=8,font=(FONT,10),command=searchJSON)
button3.place(x=340,y=194)
button4 = Button(text="How to Use App",font=(FONT,FONT_SIZE),command=howToUse)
button4.place(x=10,y=75)

spinbox1 = Spinbox(from_=0, to=52, width=3)
spinbox1.delete(0, END)
spinbox1.insert(0,4)
spinbox1.place(x=60,y=-14)
spinbox2 = Spinbox(from_=0, to=10, width=3)
spinbox2.delete(0, END)
spinbox2.insert(0,4)
spinbox2.place(x=270,y=-14)
spinbox3 = Spinbox(from_=0, to=9, width=3)
spinbox3.delete(0, END)
spinbox3.insert(0,4)
spinbox3.place(x=435,y=-14)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Complete Match", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="Partial Match", value=2, variable=radio_state)
radiobutton1.place(x=310,y=100)
radiobutton1.select()
radiobutton2.place(x=310,y=125)

window.mainloop()