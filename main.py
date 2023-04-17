from modules import printer, db, gui
import PySimpleGUI as sg

def main():
    print("Hello World")
    template, code = printer.createTemplate().projectBox(1)
    p._raw(template)
    window = gui.getWindows()
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-PRINT MENUE-":
            gui.open_window()

    #db.addNewProjectBox(code)

def clean_up():
    print("failed to print, clean up")
    pass


if __name__ == '__main__':
    printer.init()
    gui.init()
    global p
    p = printer.getPrinter()
    db.init()
    try:
        main()
    except KeyboardInterrupt:
        clean_up()

