from escpos.printer import Usb, Dummy

class templates:
    def projectBox(boxID):
        global dummyPrinter
        dummyPrinter.set(align="center", font="a", text_type="b", width=2, height=2)
        dummyPrinter.text("SPYMINER\nINVENTORY SYSTEM\n\n")
        dummyPrinter.set(align="left", font="a", text_type="b", width=1, height=1)
        dummyPrinter.text("Project Box #" + str(boxID) + "\n\n")
        code = "555134235" + str(boxID).zfill(4)
        print(code)
        dummyPrinter.barcode(code, "EAN13", 100, 3)
        dummyPrinter.cut()
        return dummyPrinter.output, code


def init():
    global printer
    global dummyPrinter
    printer = Usb(0x0456, 0x0808, in_ep=0x81, out_ep=0x03)
    dummyPrinter = Dummy()

def getPrinter():
    return printer

def createTemplate():
    return templates
