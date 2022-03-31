#imports libaries that will be needed to run the program
import PySimpleGUI as sg

#layout and theme for the inital program
#functions and buttons to also be added here
sg.theme("SystemDefaultForReal")
layout = [[sg.T("")], [sg.Text("Choose a CSV file:"), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]

#Building Window
window = sg.Window('Sort app', layout, size=(600,300))

#will be used for the main functionality of the program
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])