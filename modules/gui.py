import PySimpleGUI as sg

layout = [
    [
        sg.Column([
            [sg.Text('Inventory ')],
            [sg.Table(values=[], headings=['ID', 'Name', 'Description', 'Type'], auto_size_columns=True, num_rows=10, key='-INVENTORY TABLE-')],
            [sg.HSeparator()],
            [sg.Button('Add Item', key='-ADD ITEM-'), sg.VSeperator(),  sg.Button('Remove Item', key='-REMOVE ITEM-'), sg.VSeperator(), sg.Button('Add Item to Project', key='-ADD TO PROJECT-')],
        ]),
        sg.VSeperator(),
        sg.Column([
            [sg.Button('Print Menue', key='-PRINT MENUE-')],
            [sg.DropDown(values=[], key='-PROJECTS-')],
            [sg.Table(values=[], headings=['ID', 'Name', 'Description', 'Type'], auto_size_columns=True, num_rows=10, key='-PROJECT TABLE-')],
            [sg.Button('Remove Item from Project', key='-REMOVE FROM PROJECT-'), sg.Button('Print Project', key='-PRINT PROJECT-')],
            [sg.Button('Create Project', key='-CREATE PROJECT-'), sg.Button('Delete Project', key='-DELETE PROJECT-')],

        ]),
    ]
]

global window


def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()


def init():
    global window
    window = sg.Window("SpyMiner Inventory System", layout)

def getWindows():
    global window
    return window