from math import trunc
import PySimpleGUI as sg
import json

new = False
max_points = 300
windowSZE = (400, 150)
maxTeams = 50
Teamtotal = {}
btnSze = (10, 2)
def saveShoot(file):
    print ("File selected", file)
    with open(file, "w") as outfile:
        json.dump(shooters, outfile)
        
def importShoot(file):
    global shooters
    global lstShooters
    global teamAmount
    global teamSize
    
    shooters = {}
    lstShooters = []
    teamAmount = 0
    # Opening JSON file
    f = open(file)
    shooters = json.load(f)
  
    for i in shooters:
        lstShooters.append(i)
        teamAmount += 1
        teamSize = 0
        for j in shooters[i]:
            teamSize += 1
    # Closing file
    f.close()
    
def averages():
    teamAvg = {}
    count = 1
    while count <= int(teamAmount):
        shootercount = 1
        string = "Team" + str(count) + ":"
        shooters[string]
        count += 1
        total = 0
        weeks = 0
        teamAvg.update({string:{}})
        while shootercount <= int(teamSize):
            weeks = 0
            total = 0
            shooterString = "Shooter" + str(shootercount) + ":"
            name = shooters[string][shooterString]["Name:"]
            teamAvg[string].update({shooterString:{"Name:": name}})
            shootercount += 1
            while weeks < len(shooters[string][shooterString]) - 2:
                weeks += 1
                shooterWeek = "Week" + str(weeks) + ":"
                total += shooters[string][shooterString][shooterWeek]["Score:"][0]
                
            avg = total // (len(shooters[string][shooterString]) - 2)
            teamAvg[string][shooterString].update({"Average:":avg})
    print("#--------------------------------------------------------------------#")
    for i in teamAvg:
        print(i)
        for j in teamAvg[i]:
            print("  ",j)
            for b in teamAvg[i][j]:
                print("     ",b , teamAvg[i][j][b])
    print("#--------------------------------------------------------------------#")
def totals():
    global Teamtotal
    Teamtotal = {}
    count = 1
    while count <= int(teamAmount):
        shootercount = 1
        string = "Team" + str(count) + ":"
        shooters[string]
        count += 1
        total = 0
        weeks = 0
        Teamtotal.update({string:0})
        while shootercount <= int(teamSize):
            weeks = 0
            shooterString = "Shooter" + str(shootercount) + ":"
            shootercount += 1
            while weeks < len(shooters[string][shooterString]) - 2:
                weeks += 1
                shooterWeek = "Week" + str(weeks) + ":"
                total += shooters[string][shooterString][shooterWeek]["Score:"][1]
                Teamtotal.update({string:total})
                    
    rank(Teamtotal)
    
def rank(dicti):
    shooterLst = []
    
    for i in dicti:
        shooterLst.append([i, dicti[i]])
        
    n = len(shooterLst)

    # perform bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            if shooterLst[j][1] > shooterLst[j+1][1]:
                shooterLst[j], shooterLst[j+1] = shooterLst[j+1], shooterLst[j]

    shooterLst = list(reversed(shooterLst))
    
    #format and print niceley
    rank = 1
    idx = 0
    for i in shooterLst:
        print(int(rank),".",shooterLst[idx][0],shooterLst[idx][1])
        if idx < len(shooterLst) - 1:
            if shooterLst[idx][1] != shooterLst[idx + 1][1]:
                rank += 1
        idx += 1
    
def teamAmount():
    slideNum = 0
    num = 0
    sze = 0
    #return sg.popup_get_text('Number of Teams', title="Textbox")
    
    col_7_0 = [
        [sg.Text('Enter Amount of Teams:')],
        [sg.InputText(key = "input", enable_events = True, default_text = "1", size = (3,1))],
        [sg.Slider((1, maxTeams), slideNum, 1, orientation = "h", key = "Slide", enable_events = True)],
        [sg.Text('Enter Team Size:'), sg.Text('0', key = 'Current')],
        [sg.Button('1', size = (4, 2)), sg.Button('2', size = (4, 2)),sg.Button('3', size = (4, 2))],
        [sg.Button('Enter', disabled = True, size = btnSze), sg.Button('Cancel', size = btnSze)]
    ]
    layout7 = [
        [sg.Column(col_7_0, element_justification = "c", justification = "c")]
    ]
    
    window7 = sg.Window('Team Setup', layout7)
    while True:
        event, values = window7.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            window7.close()
            break
        elif event == "input":
            num = values[event]
            if num == "":
                num = 0
            else:
                try:
                    num = int(num)
                    window7['Slide'].update(num)
                except:
                    sg.popup_ok("Enter Numbers Only")
        elif event == "Slide":
            num = values[event]
            num = int(num)
            window7['input'].update(num)
        if event == "1":
            sze = 1
            window7['Enter'].update(disabled = False)
            window7['Current'].update(sze)
        elif event == "2":
            sze = 2
            window7['Current'].update(sze)
            window7['Enter'].update(disabled = False)
        elif event == "3":
            sze = 3
            window7['Current'].update(sze)
            window7['Enter'].update(disabled = False)
        elif event == "Enter":
            window7.close()
            return values["Slide"], sze
            break
    
def dspStats(s):
    #print(s)
    window['shooterBox'].update(shooters[s])
    #window['nameBox'].update(s)
    
def printStats():
    #Print Shooters but formatted
    print("#--------------------------------------------------------------------#")
    for i in shooters:
        print("\n")
        print(i)
        for j in shooters[i]:
            print("  ",j)
            for b in shooters[i][j]:
                print("     ",b , shooters[i][j][b])
    print("#--------------------------------------------------------------------#")

                
def editName(team):
    if int(teamSize) == 1:
        layout2 = [
            [sg.Text('Shooter1:',size = (13, 1)), sg.InputText(key = "inputS1")],
            [sg.Button('Enter'), sg.Button('Cancel')]
        ]
    elif int(teamSize) == 2:
        layout2 = [
            [sg.Text('Shooter1:',size = (13, 1)), sg.InputText(key = "inputS1")],
            [sg.Text('Shooter2:',size = (13, 1)), sg.InputText(key = "inputS2")],
            [sg.Button('Enter'), sg.Button('Cancel')]
        ]   
    elif int(teamSize) == 3:
        layout2 = [
            [sg.Text('Shooter1:',size = (13, 1)), sg.InputText(key = "inputS1")],
            [sg.Text('Shooter2:',size = (13, 1)), sg.InputText(key = "inputS2")],
            [sg.Text('Shooter3:',size = (13, 1)), sg.InputText(key = "inputS3")],
            [sg.Button('Enter'), sg.Button('Cancel')]
        ]
    window2 = sg.Window('Edit Names', layout2,size = windowSZE)
    event, values = window2.read()
    if event == "Cancel":
        window2.close()
    else:
        if int(teamSize) == 1:
            shooters[team]["Shooter1:"]["Name:"] = values["inputS1"]
        elif int(teamSize) == 2:
            shooters[team]["Shooter1:"]["Name:"] = values["inputS1"]
            shooters[team]["Shooter2:"]["Name:"] = values["inputS2"]
        elif int(teamSize) == 3:
            shooters[team]["Shooter1:"]["Name:"] = values["inputS1"]
            shooters[team]["Shooter2:"]["Name:"] = values["inputS2"]
            shooters[team]["Shooter3:"]["Name:"] = values["inputS3"]
        
        window2.close()
    
def editPoints(team):
    lstWeeks = []
    for i in shooters:
        if i == team:
            for j in shooters[i]:
                if j == "Shooter1:":
                    for b in shooters[i][j]:
                        if b != "Name:":
                            lstWeeks.append(b)
    col3=[
        [sg.Text('Teams:', size=sz2)],
        [sg.Listbox(lstWeeks, size=(25, 10), enable_events = True, key="listWeeks", disabled = False)]
    ]
    
    if int(teamSize) == 1:
        col4 = [ 
            [sg.Text('Shooter1:',size = (13, 1)), sg.InputText(key = "inputS1")],
        ]
    elif int(teamSize) == 2:
        col4 = [ 
            [sg.Text('Shooter1:',size = (13, 1)), sg.InputText(key = "inputS1")],
            [sg.Text('Shooter2:',size = (13, 1)), sg.InputText(key = "inputS2")],
        ]
    elif int(teamSize) == 3:
        col4 = [ 
            [sg.Text('Shooter1:',size = (13, 1)), sg.InputText(key = "inputS1")],
            [sg.Text('Shooter2:',size = (13, 1)), sg.InputText(key = "inputS2")],
            [sg.Text('Shooter3:',size = (13, 1)), sg.InputText(key = "inputS3")],
        ]
        
    layout3 = [  [sg.Column(col3),
            sg.VSeperator(),
            sg.Column(col4)],
            [sg.Button('Enter', disabled = True), sg.Button('Cancel')]

        ]
    
    window3 = sg.Window('Edit Points', layout3)
    
    while True:
        event, values = window3.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            window3.close()
            break
        elif event == "listWeeks":
            week = values[event][0]
            window3['Enter'].update(disabled = False)
        elif event == "Enter":
            if int(teamSize) == 1:
                if week != "Week0:":
                    val1 = int(values["inputS1"])
                    shooters[team]["Shooter1:"][week]["Score:"][0] = val1
                    if week == "Week1:":
                        shooters[team]["Shooter1:"][week]["Handycap:"] = getHandyWk1(team, "Shooter1:")
                    else:
                        shooters[team]["Shooter1:"][week]["Handycap:"] = getHandyWk2(team, "Shooter1:",week)
                    add(team, "Shooter1:", week)
                    window3.close()
                    break
                else:
                    val1 = int(values["inputS1"])
                    shooters[team]["Shooter1:"][week]["Score:"][0] = val1
                    window3.close()
                    break
            elif int(teamSize) == 2:
                if week != "Week0:":
                    val1 = int(values["inputS1"])
                    val2 = int(values["inputS2"])
                    shooters[team]["Shooter1:"][week]["Score:"][0] = val1
                    if week == "Week1:":
                        shooters[team]["Shooter1:"][week]["Handycap:"] = getHandyWk1(team, "Shooter1:")
                    else:
                        shooters[team]["Shooter1:"][week]["Handycap:"] = getHandyWk2(team, "Shooter1:",week)
                        
                    add(team, "Shooter1:", week)
                    shooters[team]["Shooter2:"][week]["Score:"][0] = val2
                    if week == "Week1:":
                        shooters[team]["Shooter2:"][week]["Handycap:"] = getHandyWk1(team, "Shooter2:")
                    else:
                        shooters[team]["Shooter2:"][week]["Handycap:"] = getHandyWk2(team, "Shooter2:",week)
                    add(team, "Shooter2:", week)
                    window3.close()
                    break
                else:
                    val1 = int(values["inputS1"])
                    val2 = int(values["inputS2"])
                    shooters[team]["Shooter1:"][week]["Score:"][0] = val1
                    shooters[team]["Shooter2:"][week]["Score:"][0] = val2
                    window3.close()
                    break
            elif int(teamSize) == 3:
                if week != "Week0:":
                    val1 = int(values["inputS1"])
                    val2 = int(values["inputS2"])
                    val3 = int(values["inputS3"])
                    shooters[team]["Shooter1:"][week]["Score:"][0] = val1
                    if week == "Week1:":
                        shooters[team]["Shooter1:"][week]["Handycap:"] = getHandyWk1(team, "Shooter1:")
                    else:
                        shooters[team]["Shooter1:"][week]["Handycap:"] = getHandyWk2(team, "Shooter1:",week)
                    add(team, "Shooter1:", week)
                    shooters[team]["Shooter2:"][week]["Score:"][0] = val2
                    if week == "Week1:":
                        shooters[team]["Shooter2:"][week]["Handycap:"] = getHandyWk1(team, "Shooter2:")
                    else:
                        shooters[team]["Shooter2:"][week]["Handycap:"] = getHandyWk2(team, "Shooter2:",week)
                    add(team, "Shooter2:", week)
                    shooters[team]["Shooter3:"][week]["Score:"][0] = val3
                    if week == "Week1:":
                        shooters[team]["Shooter3:"][week]["Handycap:"] = getHandyWk1(team, "Shooter3:")
                    else:
                        shooters[team]["Shooter3:"][week]["Handycap:"] = getHandyWk2(team, "Shooter3:",week)
                    add(team, "Shooter3:", week)
                    window3.close()
                    break
                else:
                    val1 = int(values["inputS1"])
                    val2 = int(values["inputS2"])
                    val3 = int(values["inputS3"])
                    shooters[team]["Shooter1:"][week]["Score:"][0] = val1
                    shooters[team]["Shooter2:"][week]["Score:"][0] = val2
                    shooters[team]["Shooter3:"][week]["Score:"][0] = val3
                    window3.close()
                    break
            window3.close()

def editWeeks():
    col_4_0 = [
        [sg.Button('Add Week',size = btnSze), sg.Button('Delete Week', size = btnSze)],
        [sg.Button('Exit', size = btnSze)]
    ]

    layout4 = [
        [sg.Column(col_4_0,element_justification = "c", justification = "c")],
    ]
    window4 = sg.Window('Edit Weeks', layout4, size = windowSZE)
    event, values = window4.read()
    if event == "Exit":
        window4.close()
    elif event == "Add Week":
        #print("added")
        
        count = 1
        while count <= int(teamAmount):
            shootercount = 1
            string = "Team" + str(count) + ":"
            shooters[string]
            count += 1
            while shootercount <= int(teamSize):
                shooterString = "Shooter" + str(shootercount) + ":"
                shooterWeek = "Week" + str(len(shooters[string][shooterString]) - 1) + ":"
                if shooterWeek == "Week1:":
                    shooters[string][shooterString].update({shooterWeek:{"Handycap:":getHandyWk1(string, shooterString),"Score:":[0,0]}})
                    shootercount += 1
                else:
                    shooters[string][shooterString].update({shooterWeek:{"Handycap:":getHandyWk2(string, shooterString, shooterWeek),"Score:":[0,0]}})
                    shootercount += 1
        window4.close()

    elif event == "Delete Week":
        if len(shooters["Team1:"]["Shooter1:"]) < 3:
            sg.popup_ok('Please add a week first')
            window4.close()
        else:
            ch = sg.popup_yes_no("Do you want to Delete the most Recent Week?",  title="YesNo")
            if ch == "Yes":
                #print("del")
                window4.close()
                removeWeek()
            else:
                window4.close()
def removeWeek():
    count = 1
    while count <= int(teamAmount):
        shootercount = 1
        string = "Team" + str(count) + ":"
        shooters[string]
        count += 1
        while shootercount <= int(teamSize):
            shooterString = "Shooter" + str(shootercount) + ":"
            shooterWeek = "Week" + str(len(shooters[string][shooterString]) - 1) + ":"
            if shooterWeek == "Week1:":
                shooters[string][shooterString].popitem()
                shootercount += 1
            else:
                shooters[string][shooterString].popitem()
                shootercount += 1
            
def getHandyWk1(team, shooter):
    score = shooters[team][shooter]["Week0:"]["Score:"][0]
    hc = trunc((max_points - score)*.90)
    return hc

def getHandyWk2(team, shooter, week):
    slot1 = 0
    slot2 = 0
    count = 0
    final = 0
    for i in shooters:
        if i == team:
            for j in shooters[i]:
                if shooter == j:
                    for b in shooters[i][j]:
                        if b == week:
                            break
                        for c in shooters[i][j][b]:
                            if c == "Score:":
                                if count == 0:
                                    slot1 = shooters[i][j][b][c][0]
                                    count += 1
                                else:
                                    slot2 = shooters[i][j][b][c][0]
                                    count = 0
                                
    #print(slot1, slot2)
    final = (300 - ((slot1 + slot2)/2))*.9
    return(trunc(final))

def add(team, shooter, week):
    hc = 0
    score = 0
    total_added = 0
    for i in shooters:
        if i == team:
            for j in shooters[i]:
                if shooter == j:
                    for b in shooters[i][j]:
                        if b == week:
                            for c in shooters[i][j][b]:
                                if c == "Score:":
                                    score = shooters[i][j][b][c][0]
                                else:
                                    hc = shooters[i][j][b][c]
    total_added = score + hc
    if total_added > 300:
        total_added = 300
    
    #print("done", hc, score, team)
    shooters[team][shooter][week]["Score:"][1] = total_added
    return(total_added)
#---------------------------------------------------------------#
col_0_0 = [
    [sg.Text('Start a New League or Import an existing League:')]
] 
col_0_1 = [
    [sg.Button('New', size = btnSze), sg.Button('Import', size = btnSze)]
]
layout0 = [
    [sg.Column(col_0_0, justification = "c")],
    [sg.Column(col_0_1, justification = "c")]
]      
window1 = sg.Window('Start Up', layout0, size = windowSZE)    

event, values = window1.read()
if event == 'New':
    new = True
window1.close()
#---------------------------------------------------------------#

#First window ^
#Generate Dict v

#---------------------------------------------------------------#
if new == True:
    teamAmount, teamSize = teamAmount()

    count = 1
    #Generate the Dictionary
    shooters = {}
    lstShooters = []
    while count <= int(teamAmount):
        shootercount = 1
        string = "Team" + str(count) + ":"
        shooters.update({string:{}},)
        lstShooters.append(string)
        count += 1
        while shootercount <= int(teamSize):
            shooterString = "Shooter" + str(shootercount) + ":"
            shooters[string].update({shooterString:{"Name:":"NULL", "Week0:":{"Handycap:":0,"Score:": [0,0]}}})
            shootercount += 1
else:
    text = sg.popup_get_text('Enter file name', title="Textbox")
    text = str(text)
    text = text + ".json"
    importShoot(text)
#---------------------------------------------------------------#
#Main Window
sz1=(50,1)
sz2 = (25,1)

btnCol1= [
   [sg.Button('Print', size = btnSze)],
   [sg.Button('Averages', size = btnSze)],
   [sg.Button('Team Totals', size = btnSze)]
    
]

btnCol2= [
    [sg.Button('Edit Names', disabled = True, size = btnSze)],
    [sg.Button('Edit Points', disabled = True, size = btnSze)],
    [sg.Button('Edit Weeks', size = btnSze)]
]


btnCol3= [
    [sg.Button('Exit', size = btnSze), sg.Button('Save Shoot', size = btnSze)]
    
]

bottom_box = [
    [sg.Text('Selected Team:'), sg.Text('', size = (sz1), key = "nameBox")],
    [sg.Multiline('{}', size = (50, 10), key = "shooterBox")]
]

col1=[
    [sg.Text('Docs Archery Script', size=sz1, justification = "c")],
    [sg.Column(btnCol1, vertical_alignment = "t"), sg.Column(btnCol2, vertical_alignment = "t")],
    [sg.Column(bottom_box, vertical_alignment = "b")]
    
]

col2=[
    [sg.Text('Teams:', size=sz2)],
    [sg.Listbox(lstShooters, size=(25, 10), enable_events = True, key="list", disabled = False)]
]


layout1 = [  [sg.Column(col1, element_justification = "c", vertical_alignment = "t"),
            sg.VSeperator(),
            sg.Column(col2)],
            [sg.Column(btnCol3)]
]


window = sg.Window('Docs Archery', layout1)
selection = 0
while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'list':
        window['Edit Names'].update(disabled = False)
        window['Edit Points'].update(disabled = False)
        window['Edit Weeks'].update(disabled = False)
        
        selection = values[event]
        dspStats(selection[0])
    elif event == 'Print':
        printStats()
    elif event == 'Edit Names':
        editName(selection[0])
        dspStats(selection[0])
    elif event == 'Edit Points':
        editPoints(selection[0])
        dspStats(selection[0])
    elif event == 'Edit Weeks':
        editWeeks()
        if selection != 0:
            dspStats(selection[0])
    elif event == 'Averages':
        averages()
    elif event == 'Team Totals':
        totals()
    elif event == "Save Shoot":
        text = sg.popup_get_text('Enter file name', title="Textbox")
        text = str(text)
        text = text + ".json"
        saveShoot(text)
        
window.close()