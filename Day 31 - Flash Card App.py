from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import tkinter.font
import glob
import json
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#00bfff"
FONT = "Arial"
# ---------------------------- CREATE DECK ------------------------------- #
def createDeck():
    def createJSON():
        fileName = createDeckInput1.get().strip()
        if len(fileName) < 1:
            windowCreateDeck.destroy()
            messagebox.showerror(title="Error!", message="Do not leave any fields blank!")
        else:
            windowCreateDeck.destroy()
            with open(f"./data/{fileName}.json", mode="w") as docs1:
                pass
    windowCreateDeck = Tk()
    windowCreateDeck.title("Create Deck")
    windowCreateDeck.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
    windowCreateDeck.minsize(width=350, height=100)
    windowCreateDeck.maxsize(width=350, height=100)
    createDeckInput1 = Entry(windowCreateDeck,width=40)
    createDeckInput1.place(x=-10, y=10)
    createDeckInput1.focus()
    createDeckLabel1 = Label(windowCreateDeck,text="Enter the name of the deck you want to create", font=(FONT,12),
    bg=BACKGROUND_COLOR)
    createDeckLabel1.place(x=-10,y=-15)
    createDeckButton1 = Button(windowCreateDeck,text="Create",command=createJSON)
    createDeckButton1.place(x=125,y=44)
    windowCreateDeck.mainloop()
# ---------------------------- EDIT DECK ------------------------------- #
def editDeckSelection():
    windowEditDeckSelection = Tk()
    windowEditDeckSelection.title("Select A Deck To Edit")
    windowEditDeckSelection.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
    windowEditDeckSelection.minsize(width=300, height=300)
    windowEditDeckSelection.maxsize(width=300, height=300)
    dataFolderFileNames = glob.glob("./data/*.json")

    windowEditDeckSelectionListBox = Listbox(windowEditDeckSelection,width=34,height=12)
    windowEditDeckSelectionListBox.place(x=-8,y=-10)

    for item in dataFolderFileNames:
        windowEditDeckSelectionListBox.insert(dataFolderFileNames.index(item), item)

    def deckSelected():
        windowRoot.state("iconic")
        try:
            selectedDeck = windowEditDeckSelectionListBox.get(windowEditDeckSelectionListBox.curselection())
            windowEditDeckSelection.destroy()
            windowDeckSelected = Tk()
            windowDeckSelected.title(f"{selectedDeck}")
        except TclError:
            pass
        except UnboundLocalError:
            pass

        def addCards():
            windowDeckSelected.destroy()
            windowAddCards = Tk()
            windowAddCards.title(f"Adding Cards to {selectedDeck}")
            windowAddCards.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
            windowAddCards.minsize(width=400, height=300)
            windowAddCards.maxsize(width=400, height=300)

            windowAddCardsLabel1 = Label(windowAddCards, text="Enter the card's question:",
            font=(FONT, 12), bg=BACKGROUND_COLOR)
            windowAddCardsLabel1.place(x=100,y=-10)

            windowAddCardsInput1 = Entry(windowAddCards, width=46)
            windowAddCardsInput1.place(x=-8, y=25)
            windowAddCardsInput1.focus()

            windowAddCardsLabel2 = Label(windowAddCards, text="Enter the card's answer:",
            font=(FONT, 12), bg=BACKGROUND_COLOR)
            windowAddCardsLabel2.place(x=100, y=125)

            windowAddCardsInput2 = Entry(windowAddCards, width=46)
            windowAddCardsInput2.place(x=-8, y=155)

            def addCardButtonPress():
                inputQuestion = windowAddCardsInput1.get().strip()
                inputAnswer = windowAddCardsInput2.get().strip()
                jsonData = {
                    inputQuestion: {
                        "Answer": inputAnswer
                    }
                }

                if len(inputQuestion) < 1 or len(inputAnswer) < 1:
                    windowAddCards.state(newstate="iconic")
                    messagebox.showerror(title="Error!", message="Do not leave any fields blank!")
                    windowAddCardsInput1.delete(0, END)
                    windowAddCardsInput2.delete(0, END)
                else:
                    windowAddCards.state("iconic")
                    question = messagebox.askokcancel(title="Confirmation",
                    message=f"The following information will be saved to {selectedDeck}:\n"
                    f"\nQuestion: {inputQuestion}\nAnswer: {inputAnswer}\n"
                    f"\nDo you want to proceed with saving this information?")
                    if question:
                        try:
                            with open(selectedDeck, mode="r") as docs1:
                                data = json.load(docs1)  # Reads old data
                                data.update(jsonData)  # Updates old data with new input data
                        except JSONDecodeError:
                            with open(selectedDeck, mode="w") as docs1:
                                json.dump(jsonData, docs1, indent=4)  # Creates JSON file and writes to it in the event the file is empty.
                        except FileNotFoundError:
                            with open(selectedDeck, mode="w") as docs1:
                                json.dump(jsonData, docs1, indent=4)  # Creates JSON file and writes to it in the event the file doesn't exist.
                        else:
                            with open(selectedDeck, mode="w") as docs2:
                                json.dump(data, docs2, indent=4)  # Saves updated data to JSON file
                        finally:
                            windowAddCards.state(newstate="normal")
                            windowAddCardsInput1.delete(0, END)
                            windowAddCardsInput2.delete(0, END)
                    else:
                        windowAddCards.state(newstate="normal")
                        windowAddCardsInput1.delete(0, END)
                        windowAddCardsInput2.delete(0, END)

            windowAddCardsButton1 = Button(windowAddCards, text="Add Card",command=addCardButtonPress)
            windowAddCardsButton1.place(x=140, y=225)

            windowAddCards.mainloop()

        windowDeckSelected.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
        windowDeckSelected.minsize(width=400, height=400)
        windowDeckSelected.maxsize(width=400, height=400)

        windowDeckSelectedLabel1 = Label(windowDeckSelected,text="Current Cards",
        font=(FONT,12), bg=BACKGROUND_COLOR)
        windowDeckSelectedLabel1.place(x=125,y=-10)

        windowDeckSelectedListBox = Listbox(windowDeckSelected, width=46, height=15)
        windowDeckSelectedListBox.place(x=-6, y=20)

        try:
            with open(selectedDeck,mode='r') as docs1:
                data = json.load(docs1)
                dataKeysList = list(data.keys())
                for i in dataKeysList:
                    windowDeckSelectedListBox.insert(dataKeysList.index(i), i)
        except JSONDecodeError:
            pass

        windowDeckSelectedButton1 = Button(windowDeckSelected, text="Add Cards",command=addCards)
        windowDeckSelectedButton1.place(x=0, y=332)

        def editCard():
            try:
                selectedCard = windowDeckSelectedListBox.get(windowDeckSelectedListBox.curselection())
            except TclError:
                messagebox.showerror(title="Error!", message="You must select a card when editing!")
            else:
                windowDeckSelected.destroy()
                windowEditCard = Tk()
                windowEditCard.title(f"Editing Card for {selectedDeck}")
                windowEditCard.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
                windowEditCard.minsize(width=400, height=300)
                windowEditCard.maxsize(width=400, height=300)

                windowEditCardLabel1 = Label(windowEditCard, text="Enter the card's question:",
                font=(FONT, 12), bg=BACKGROUND_COLOR)
                windowEditCardLabel1.place(x=100,y=-10)

                windowEditCardInput1 = Entry(windowEditCard, width=46)
                windowEditCardInput1.place(x=-8, y=25)
                windowEditCardInput1.focus()

                windowEditCardLabel2 = Label(windowEditCard, text="Enter the card's answer:",
                font=(FONT, 12), bg=BACKGROUND_COLOR)
                windowEditCardLabel2.place(x=100, y=125)

                windowEditCardInput2 = Entry(windowEditCard, width=46)
                windowEditCardInput2.place(x=-8, y=155)

                with open(selectedDeck, mode='r') as docs2:
                    data = json.load(docs2)
                    dataKeysList = list(data.keys())
                    dataValuesList = list(data.values())

                    for i in dataKeysList:
                        if i == selectedCard:
                            windowEditCardInput1.insert(0,i)
                            index = dataKeysList.index(i)

                    for i in dataValuesList:
                        if dataValuesList.index(i) == index:
                            windowEditCardInput2.insert(0,i["Answer"])

                    toDelete1 = windowEditCardInput1.get()
                    toDelete2 = windowEditCardInput2.get()

                    def confirmEdit():
                        if len(windowEditCardInput1.get()) < 1 or len(windowEditCardInput2.get()) < 1:
                            windowEditCard.state("iconic")
                            question = messagebox.askokcancel(title="Confirmation",
                            message=f"The following information will be DELETED from {selectedDeck}:\n"
                            f"\nQuestion: {toDelete1}\nAnswer: {toDelete2}\n"
                            f"\nDo you want to proceed with DELETING this information?")
                            if question:
                                with open(selectedDeck, mode="r") as docs3:
                                    windowEditCard.destroy()
                                    data = json.load(docs3)  # Reads old data
                                    data.pop(selectedCard)
                                    data.update(data)
                                    with open(selectedDeck, mode="w") as docs4:
                                        json.dump(data, docs4, indent=4)
                        else:
                            newQuestion = windowEditCardInput1.get()
                            newAnswer = windowEditCardInput2.get()
                            windowEditCard.state("iconic")
                            question = messagebox.askokcancel(title="Confirmation",
                            message=f"The following information will be saved to {selectedDeck}:\n"
                            f"\nQuestion: {newQuestion}\nAnswer: {newAnswer}\n"
                            f"\nDo you want to proceed with saving this information?")
                            if question:
                                with open(selectedDeck, mode="r") as docs3:
                                    windowEditCard.destroy()
                                    data = json.load(docs3)  # Reads old data
                                    val1 = data.pop(selectedCard)
                                    data[newQuestion] = val1
                                    data[newQuestion]["Answer"] = newAnswer
                                    data.update(data)  # Updates old data with new input data
                                    with open(selectedDeck, mode="w") as docs4:
                                        json.dump(data, docs4, indent=4)
                            else:
                               windowEditCard.state("normal")

                    windowEditCardButton1 = Button(windowEditCard, text="Confirm Edit",command=confirmEdit)
                    windowEditCardButton1.place(x=140, y=225)

        windowDeckSelectedButton1 = Button(windowDeckSelected, text="Edit Selected Card",command=editCard)
        windowDeckSelectedButton1.place(x=220, y=332)

    windowEditDeckSelectionButton1 = Button(windowEditDeckSelection,text="Confirm Selection",command=deckSelected)
    windowEditDeckSelectionButton1.place(x=63,y=240)

    windowEditDeckSelection.mainloop()
# ---------------------------- SELECTING A DECK TO STUDY ------------------------------- #
indexCount = 0
usedNum = []
toLearn = []
restart = 0
def studyDeckSelection():
    windowStudyDeckSelection = Tk()
    windowStudyDeckSelection.title("Select A Deck To Study")
    windowStudyDeckSelection.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
    windowStudyDeckSelection.minsize(width=300, height=300)
    windowStudyDeckSelection.maxsize(width=300, height=300)
    dataFolderFileNames = glob.glob("./data/*.json")

    windowStudyDeckSelectionListBox = Listbox(windowStudyDeckSelection,width=34,height=12)
    windowStudyDeckSelectionListBox.place(x=-8,y=-10)

    for item in dataFolderFileNames:
        windowStudyDeckSelectionListBox.insert(dataFolderFileNames.index(item), item)

    def studyDeckSelected():
        global usedNum
        windowStudyDeckSelection.state(newstate="iconic")
        try:
            selectedDeck = windowStudyDeckSelectionListBox.get(windowStudyDeckSelectionListBox.curselection())
        except TclError:
            pass
        else:
            buttonRoot1.place_forget()
            buttonRoot2.place_forget()
            buttonRoot3.place_forget()
            with open(selectedDeck, mode="r") as docs5:
                data = json.load(docs5)
                dataKeysList = list(data.keys())

            while True:
                if restart == 0:
                    rng = random.randint(0,len(dataKeysList) - 1)
                    if rng in usedNum:
                        rng = random.randint(0, len(dataKeysList) - 1)
                    else:
                        usedNum.append(rng)
                        break
                elif restart == 1:
                    rng = random.randint(0, len(toLearn) - 1)
                    if rng in usedNum:
                        rng = random.randint(0, len(toLearn) - 1)
                    else:
                        usedNum.append(rng)
                        break

            canvasRoot.itemconfigure(topicTextRoot,text="Question")
            questionTextRoot.delete(1.0,"end")
            questionTextRoot.insert(1.0,dataKeysList[rng])
            questionTextRoot.tag_configure("center", justify='center')
            questionTextRoot.tag_add("center", 1.0, "end")

            def flipCard():
                global indexCount

                flipButton.destroy()

                canvasRoot.itemconfigure(topicTextRoot, text="Answer")
                questionTextRoot.delete(1.0, "end")
                questionTextRoot.insert(1.0, data[dataKeysList[rng]]["Answer"])
                questionTextRoot.tag_configure("center", justify='center')
                questionTextRoot.tag_add("center", 1.0, "end")

                indexCount += 1

                def moveOn():
                    global indexCount, restart
                    xMarkbutton1.destroy()
                    checkMarkbutton1.destroy()
                    if indexCount == len(dataKeysList) and restart == 0 and len(toLearn) == 0:
                        usedNum.clear()
                        indexCount = 0
                        windowRoot.state(newstate="iconic")
                        restart = messagebox.showinfo(title="Congratulations!",message="You've completed this deck!\n\n"
                        "Press OK to return to the main screen.")
                        if restart:
                            restart = 0
                            buttonRoot1.place(x=90, y=50)
                            buttonRoot2.place(x=665, y=50)
                            buttonRoot3.place(x=370, y=50)
                            canvasRoot.itemconfigure(topicTextRoot, text="Welcome!")
                            questionTextRoot.delete(1.0, "end")
                            questionTextRoot.insert(1.0, "Thanks for using the Simplicity Flash Card App! "
                            "Happy studying!")
                            questionTextRoot.tag_configure("center", justify='center')
                            questionTextRoot.tag_add("center", 1.0, "end")
                            windowStudyDeckSelection.destroy()
                            windowRoot.state(newstate="normal")
                    elif (indexCount == len(dataKeysList) and len(toLearn) >= 1) or (indexCount == len(toLearn) and restart == 1):
                        usedNum.clear()
                        indexCount = 0
                        windowRoot.state(newstate="iconic")
                        restart = messagebox.askyesno(title="Congratulations!",
                        message="You've completed this deck!\n\n"
                        "Would you like to practice the cards you had trouble understanding?")
                        if restart:
                            restart = 1
                            windowRoot.state(newstate="normal")
                            studyDeckSelected()
                        else:
                            toLearn.clear()
                            restart = 0
                            buttonRoot1.place(x=90, y=50)
                            buttonRoot2.place(x=665, y=50)
                            buttonRoot3.place(x=370, y=50)
                            canvasRoot.itemconfigure(topicTextRoot, text="Welcome!")
                            questionTextRoot.delete(1.0, "end")
                            questionTextRoot.insert(1.0, "Thanks for using the Simplicity Flash Card App! "
                            "Happy studying!")
                            questionTextRoot.tag_configure("center", justify='center')
                            questionTextRoot.tag_add("center", 1.0, "end")
                            windowStudyDeckSelection.destroy()
                            windowRoot.state(newstate="normal")
                    else:
                        studyDeckSelected()
                def morePractice():
                    if restart == 0:
                        toLearn.append(rng)
                    elif restart == 1:
                        pass
                    moveOn()

                xMarkbutton1 = Button(text="I need more practice with this card.",command=morePractice)
                xMarkbutton1.place(x=75, y=700)

                checkMarkbutton1 = Button(text="I understand this card!",command=moveOn)
                checkMarkbutton1.place(x=600, y=700)

            flipButton = Button(windowRoot,text="Flip Card!",width=15,command=flipCard)
            flipButton.place(x=370, y=725)

    windowEditDeckSelectionButton1 = Button(windowStudyDeckSelection,text="Confirm Selection",command=studyDeckSelected)
    windowEditDeckSelectionButton1.place(x=63, y=240)

    windowStudyDeckSelection.mainloop()
# ---------------------------- UI SETUP ------------------------------- #
windowRoot = Tk()
windowRoot.title("Simplicity Flash Card App")
windowRoot.config(padx=20,pady=20,bg=BACKGROUND_COLOR)
windowRoot.minsize(width=900,height=900)
windowRoot.maxsize(width=900,height=900)

canvasRoot = Canvas(windowRoot,width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
cardImg = PhotoImage(file="./images/card_front.png")
canvasRoot.create_image(400,260,image=cardImg)
canvasRoot.place(x=40,y=125)

buttonRoot1 = Button(windowRoot,text="Create Deck",command=createDeck,width=10)
buttonRoot1.place(x=90,y=50)
buttonRoot2 = Button(windowRoot,text="Edit Deck",command=editDeckSelection,width=10)
buttonRoot2.place(x=665,y=50)
buttonRoot3 = Button(windowRoot,text="Select Deck To Study",command=studyDeckSelection,width=15)
buttonRoot3.place(x=370,y=50)

topicTextRoot = canvasRoot.create_text(400, 50, text="Welcome!", fill="black", font=("Arial", 40, "italic"))
questionTextRoot = Text(height=7,width=32,bd=0,bg="white",fg="black",highlightthickness=0,borderwidth=0,wrap="word")
questionTextRoot.insert(END, "Thanks for using the Simplicity Flash Card App! Happy studying!")
questionTextRoot.tag_configure("center", justify='center')
questionTextRoot.tag_add("center", 1.0, "end")
cf = tkinter.font.Font(family="Arial", size=30)
questionTextRoot.configure(font=cf, state="normal")
questionTextRoot.place(x=76, y=250)

windowRoot.mainloop()