from tkinter import *
import tkinter.font as tkFont
import sets
import classes
import logic
from PIL import ImageTk, Image
import os

def resource_path(relative_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    return os.path.join(base_path, relative_path)


def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

def firstQuestion(clicked):
    global sidebar_step2
    sidebar_step2 = ImageTk.PhotoImage(Image.open(resource_path("sidebar\\sidebar_step2.png")))
    sidebar = Label(root, image=sidebar_step2)
    sidebar.grid(column=0, row=0)
    if clicked == "person":
        answers.append(classes.Answer(sets.methods[0].teams,1,False))
        updateFrame(2)
    else: updateFrame(1)

def saveTeam(amount):
    answers.append(classes.Answer(sets.methods[0].teams,amount,False))
    updateFrame(2)

def savePerson(amount):
    answers.append(classes.Answer(sets.methods[0].teamsize,amount,False))
    updateFrame(3)

def setIdeal(priorities):
    for i in range(len(priorities)):
        if priorities[i].get() == 1:
            answers[i].ideal = True
    calcResults()

def calcResults():
    global answers, idealMethods, alternativeMethods
    idealMethods, alternativeMethods = logic.check(answers)
    updateFrame("result")

def reset():
    sets.init()
    global answers 
    answers = []
    updateFrame(0)

def showSummary(method: classes.ProjectMethod):
    clear_frame()
    title = Label(frame, text="\n" + method.germanName)
    title.place(x=20, y=0) 
    title.configure(font=("Railway", 20,"bold"))
    y = 100
    decriptionTitle = Label(frame, text = "Zusammenfassung", )
    decriptionTitle.place(x=20, y=y)
    decriptionTitle.configure(font=("Railway", 14, "bold"))
    y = y + 30
    descriptionLabel  = Label(frame, text = sets.descriptionDict[method.name], wraplength=750)
    descriptionLabel.place(x=20, y=y)

def seeMore(method: classes.ProjectMethod, ideal:bool):
    showSummary(method)
    backButton = Button(frame, text="Zurück", command=lambda: updateFrame("result"), background="#909090", width=10)
    backButton.place(x=660,y=650)
    detailsButton = Button(frame, text="Kriterien", command=lambda method=method,ideal=ideal: seeDetails(method,ideal, False), background="#909090", width=10)
    detailsButton.place(x=20,y=700)

def seeDetails(method: classes.ProjectMethod, ideal:bool, summary: bool):
    clear_frame()
    title = Label(frame, text="\n" + method.germanName)
    title.place(x=20, y=0) 
    title.configure(font=("Railway", 20,"bold"))
    y = 100
    if summary == False:
        altTitle = Label(frame, text="Abweichende Kriterien:")
        altTitle.place(x=20, y=y)
        altTitle.configure(font=("Railway", 14, "bold"))
        y = y + 30
        if ideal == False:
            altParams = ""
            for answer in method.notIdeal:
                if altParams != "":
                    altParams = altParams + ", " + sets.attributeNameDict[answer.attribute.name] + " (" + str(answer.value)+ ")"
                else: altParams = sets.attributeNameDict[answer.attribute.name] + " (" + str(answer.value) + ")"
            altParamList = Label(frame, text=altParams, wraplength=750)
            altParamList.place(x=20, y=y)
        else:
            altParamList = Label(frame, text="Alle Kriterien liegen im idealen Bereich!")
            altParamList.place(x=20, y=y)
        y = y + 70
    y2 = y
    i = 0
    attributeNames = []
    attributeValues = []
    for value in sets.attributeNameDict.values():
        attributeNames.append(Label(frame, text=value, width=34, height=2, borderwidth=1, relief="solid", anchor="w"))
        attributeNames[i].place(x=15, y=y)
        y = y + 48
        i = i + 1
    i = 0
    for key in sets.attributeNameDict.keys():
        if str(method.__getattribute__(key).ideal_min) == str(method.__getattribute__(key).ideal_max):
            attributeValues.append(Label(frame, text=str(method.__getattribute__(key).ideal_min), width=35, height=2, borderwidth=1, relief="solid", anchor="w"))
        else:
            attributeValues.append(Label(frame, text=str(method.__getattribute__(key).ideal_min)+" - "+str(method.__getattribute__(key).ideal_max), width=35, height=2, borderwidth=1, relief="solid", anchor="w"))
        attributeValues[i].place(x=385, y=y2)
        y2 = y2 + 48
        i = i + 1
    if summary == False:
        backButton = Button(frame, text="Zurück", command=lambda method=method,ideal=ideal: seeMore(method,ideal), background="#909090", width=10)
        backButton.place(x=660,y=650)
    else:
        backButton = Button(frame, text="Zurück", command=lambda method=method,ideal=ideal: seeMethodInfo(method), background="#909090", width=10)
        backButton.place(x=660,y=650)

def seeMethodInfo(method: classes.ProjectMethod):
    showSummary(method)
    detailsButton = Button(frame, text="Kriterien", command=lambda method=method: seeDetails(method, True, True), background="#909090", width=10)
    detailsButton.place(x=20,y=700)

def seeInfos():
    clear_frame()
    global sidebar_home
    sidebar_home = ImageTk.PhotoImage(Image.open(resource_path("sidebar\\sidebar_home.png")))
    sidebar = Label(root, image=sidebar_home)
    sidebar.grid(column=0, row=0)
    labels = []
    buttons = []
    label_title = Label(frame,text="\nMethoden:")
    label_title.place(x=20, y=0)
    label_title.configure(font=("Railway", 18, "bold")) 
    for method in sets.methods:
        labels.append(Label(frame, text=method.germanName))
        buttons.append(Button(frame, text="Mehr Details", command=lambda method=method: seeMethodInfo(method)))
    y = 80
    i = 0
    for i in range(len(labels)):
        labels[i].place(x=20, y=y)
        buttons[i].place(x=500, y=y)
        buttons[i].config(bg="#cccccc")
        y = y + 50



def updateFrame(step):  
    match step:
        case 0:
            clear_frame()
            global sidebar
            global sidebar_step1
            sidebar_step1 = ImageTk.PhotoImage(Image.open(resource_path("sidebar\\sidebar_step1.png")))
            sidebar = Label(root, image=sidebar_step1)
            sidebar.grid(column=0, row=0)
            qLabel = Label(frame, text="\nWollen Sie Personen oder Teams managen?", wraplength=750)
            qLabel.place(x=20, y=0) 
            qLabel.configure(font=("Railway", 18, "bold"))  
            personLabel = Label(frame, text="Personen: Sie wollen Personen innerhalb eines einziges Teams managen.", wraplength=750)
            personLabel.place(x=20, y=80) 
            teamLabel = Label(frame, text="Teams: Sie wollen mehrere Teams, die zusammen an einem Produkt arbeiten, managen.", wraplength=750)
            teamLabel.place(x=20, y=110)       
            personButton = Button(frame, text="Personen", command=lambda: firstQuestion("person"), background="#909090", width=15, height=2, borderwidth=1, relief="solid") 
            personButton.place(x=490, y=300)
            teamButton = Button(frame, text="Teams", command=lambda: firstQuestion("teams"), background="#909090", width=15, height=2, borderwidth=1, relief="solid") 
            teamButton.place(x=130, y=300) 
        case 1:
            clear_frame()
            qLabel = Label(frame, text="\nWie viele Teams wollen Sie managen?", wraplength=750)
            qLabel.place(x=20, y=0) 
            qLabel.configure(font=("Railway", 18, "bold"))
            slider = Scale(frame, from_=1, to=20, orient=HORIZONTAL, length=500)
            slider.place(x=20, y=130) 
            nextButton = Button(frame, text="Weiter", command=lambda: saveTeam(slider.get()), background="#909090", width=10)
            nextButton.place(x=20, y=300) 
        case 2:
            clear_frame()
            qLabel = Label(frame, text="\nWie viele Personen wollen Sie (pro Team) managen?", wraplength=750)
            qLabel.place(x=20, y=0) 
            qLabel.configure(font=("Railway", 18, "bold"))
            slider = Scale(frame, from_=1, to=20, orient=HORIZONTAL, length=500)
            slider.place(x=20, y=130) 
            nextButton = Button(frame, text="Weiter", command=lambda: savePerson(slider.get()), background="#909090", width=10)
            nextButton.place(x=20, y=300) 
        case 3:
            clear_frame()
            qLabel = Label(frame, text="\nWie flexibel ist die Deadline des Projekts?", wraplength=750)
            qLabel.place(x=20, y=0)
            qLabel.configure(font=("Railway", 18, "bold"))           
            clicked.set(sets.deadlineSet[0])
            dropdown = OptionMenu(frame, clicked, *sets.deadlineSet)
            dropdown.place(x=20, y=130) 
            dropdown.config(bg="#cccccc") 
            menu = frame.nametowidget(dropdown.menuname)
            menu.config(font=("Railway",14), bg="#cccccc")
            nextButton = Button(frame, text="Weiter", command=lambda: updateFrame(4), background="#909090", width=10)
            nextButton.place(x=20, y=300) 
        case 4:
            answers.append(classes.Answer(sets.methods[0].deadline,clicked.get(),False))
            clear_frame()
            qLabel = Label(frame, text="\nWie flexibel sind die Anforderungen des Projekts?", wraplength=750)
            qLabel.place(x=20, y=0)
            qLabel.configure(font=("Railway", 18, "bold"))            
            clicked.set(sets.anforderungsSet[0])
            dropdown = OptionMenu(frame, clicked, *sets.anforderungsSet)
            dropdown.place(x=20, y=130) 
            dropdown.config(bg="#cccccc") 
            menu = frame.nametowidget(dropdown.menuname)
            menu.config(font=("Railway",14), bg="#cccccc")
            nextButton = Button(frame, text="Weiter", command=lambda: updateFrame(5), background="#909090", width=10)
            nextButton.place(x=20, y=300) 
        case 5:
            answers.append(classes.Answer(sets.methods[0].anforderung,clicked.get(),False))
            clear_frame()
            qLabel = Label(frame, text="\nWie stark sind Kunde und Stakeholder im Prozess involviert?", wraplength=750)
            qLabel.place(x=20, y=0) 
            qLabel.configure(font=("Railway", 18, "bold"))           
            clicked.set(sets.clientSet[0])
            dropdown = OptionMenu(frame, clicked, *sets.clientSet)
            dropdown.place(x=20, y=130) 
            dropdown.config(bg="#cccccc") 
            menu = frame.nametowidget(dropdown.menuname)
            menu.config(font=("Railway",14), bg="#cccccc")
            nextButton = Button(frame, text="Weiter", command=lambda: updateFrame(6), background="#909090", width=10)
            nextButton.place(x=20, y=300) 
        case 6:
            answers.append(classes.Answer(sets.methods[0].client,clicked.get(),False))
            clear_frame()
            qLabel = Label(frame, text="\nWie stark hängt das Projekt von äußeren Faktoren ab? (Zum Beispiel Lieferanten)", wraplength=750)
            qLabel.place(x=20, y=0)   
            qLabel.configure(font=("Railway", 18, "bold"))        
            clicked.set(sets.dependencySet[0])
            dropdown = OptionMenu(frame, clicked, *sets.dependencySet)
            dropdown.place(x=20, y=130) 
            dropdown.config(bg="#cccccc") 
            menu = frame.nametowidget(dropdown.menuname)
            menu.config(font=("Railway",14), bg="#cccccc")
            nextButton = Button(frame, text="Weiter", command=lambda: updateFrame("overview"), background="#909090", width=10)
            nextButton.place(x=20, y=300) 
        case "overview":
            answers.append(classes.Answer(sets.methods[0].dependency,clicked.get(),False))
            clear_frame()
            global sidebar_overview
            sidebar_overview = ImageTk.PhotoImage(Image.open(resource_path("sidebar\\sidebar_overview.png")))
            sidebar = Label(root, image=sidebar_overview)
            sidebar.grid(column=0, row=0)
            qLabel = Label(frame, text="\nBei der Auswertung werden alle Methoden ausgewählt, die verwendet werden können, auch wenn diese nicht ideal sind. Wählen Sie alle Eigenschaften aus, die ideal sein müssen.", wraplength=750)
            qLabel.place(x=20, y=0)
            qLabel.configure(font=("Railway", 18, "bold")) 
            infoLabel = Label(frame, text="Viele gewichtete (ideale) Eigenschaften führen zu einer stärkeren Filterung und somit zu weniger Ergebnissen.", wraplength=750)
            infoLabel.place(x=20, y=150)
            checkedArray = []
            checkboxes = []
            for answer in answers:
                checkedArray.append(IntVar())
            checkboxes.append(Checkbutton(frame, text=("Anzahl an Teams - "+str(answers[0].value)), variable=checkedArray[0]))
            checkboxes.append(Checkbutton(frame, text=("Anzahl an Personen pro Team - "+str(answers[1].value)), variable=checkedArray[1]))
            checkboxes.append(Checkbutton(frame, text=("Flexibilität der Deadline - "+str(answers[2].value)), variable=checkedArray[2]))
            checkboxes.append(Checkbutton(frame, text=("Flexibilität der Anforderungen - "+str(answers[3].value)), variable=checkedArray[3]))
            checkboxes.append(Checkbutton(frame, text=("Kunde und Stakeholder - "+str(answers[4].value)), variable=checkedArray[4]))
            checkboxes.append(Checkbutton(frame, text=("Äußere Faktoren - "+str(answers[5].value)), variable=checkedArray[5]))
            i = 240
            for checkbox in checkboxes:
                checkbox.place(x=20, y=i) 
                i = i + 40
            nextButton = Button(frame, text="Zur Auswertung", command=lambda: setIdeal(checkedArray), background="#909090")
            nextButton.place(x=20, y=i+60) 
        case "result":
            clear_frame()
            global sidebar_result
            sidebar_result = ImageTk.PhotoImage(Image.open(resource_path("sidebar\\sidebar_result.png")))
            sidebar = Label(root, image=sidebar_result)
            sidebar.grid(column=0, row=0)
            labels_ideal = []
            buttons_ideal = []
            labels_alternative = []
            buttons_alternative = []
            label_ideal = Label(frame,text="\nIdeale Methoden:")
            label_ideal.place(x=20, y=0)
            label_ideal.configure(font=("Railway", 18, "bold")) 
            global idealMethods
            for method in idealMethods:
                labels_ideal.append(Label(frame, text=method.germanName))
                buttons_ideal.append(Button(frame, text="Mehr Details", command=lambda method=method: seeMore(method,True)))
            y = 80
            i = 0
            for i in range(len(labels_ideal)):
                labels_ideal[i].place(x=20, y=y)
                buttons_ideal[i].place(x=500, y=y)
                buttons_ideal[i].config(bg="#cccccc")
                y = y + 50
            y = y + 40
            label_alternative = Label(frame,text="\nAlternative Methoden:")
            label_alternative.place(x=20, y=y)
            y = y + 80
            label_alternative.configure(font=("Railway", 18, "bold")) 
            alternativeMethods.sort(key=lambda x: len(x.notIdeal))
            for method in alternativeMethods:
                if method not in idealMethods:
                    labels_alternative.append(Label(frame, text=method.germanName))
                    buttons_alternative.append(Button(frame, text="Mehr Details", command=lambda method=method: seeMore(method,False)))
            i = 0
            for i in range(len(labels_alternative)):
                labels_alternative[i].place(x=20, y=y)
                buttons_alternative[i].place(x=500, y=y)
                buttons_alternative[i].config(bg="#cccccc")
                y = y + 50

    
def init():
    sets.init()
    global answers
    answers = []
    global root
    root = Tk()
    root.geometry('1080x854')
    root.title("Projektmanagementberatung")
    root.iconbitmap(resource_path("icons\\projectmanagement.ico"))
    root.resizable(width=0, height=0)
    #MainApp
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(family="Railway",size=14)
    sidebar_home = ImageTk.PhotoImage(Image.open(resource_path("sidebar\\sidebar_home.png")))
    global sidebar
    sidebar = Label(image=sidebar_home)
    sidebar.place(x=0, y=0)
    global frame
    frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
    introTitle = Label(frame, text="\nWelche Projektmanagementmethode?\n")
    introTitle.pack()
    introTitle.configure(font=("Railway", 20,"bold")) 
    intro = Label(frame, text="Sie sind sich noch unschlüssig, welche Projektmanagementmethode für Sie die richtige ist?\n\nBei diesem Problem wollen wir Ihnen helfen. Klicken Sie sich einfach durch das Programm durch und beantworten Sie die Fragen. Am Ende schlagen wir Ihnen Methoden vor, die für Ihr Projekt geeignet sind.\n\n\nHierbei werden folgende Methoden verglichen:\nWasserfall, V-Modell, Spiralmodell, SCRUM, Kanban, SCRUMban, SAFe und Nexus\nSie möchten beginnen? Dann klicken Sie einfach hier:\n\n", wraplength=750)
    intro.pack()
    #intro.configure(font=("Railway", 20)) 
    global clicked
    clicked = StringVar()
    startButton = Button(frame, text="Start", command=lambda: updateFrame(0), background="#909090", width=10)
    startButton.pack()
    resetButton = Button(root, text="Neu starten", command=reset, background="#909090", width=10)
    resetButton.place(x=950,y=700)
    infoButton = Button(root, text="Methoden", command=seeInfos, background="#909090", width=10)
    infoButton.place(x=950,y=750)
    frame.place(x=290, y=0, height=854, width=790)
    root.mainloop()
