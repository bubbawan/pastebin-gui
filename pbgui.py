""" Simple gui to access pastebin.com """
    
from pastebin_python import PastebinPython
from pastebin_python.pastebin_exceptions import PastebinBadRequestException, PastebinFileException
from pastebin_python.pastebin_constants import PASTE_PUBLIC, EXPIRE_1_MONTH
from pastebin_python.pastebin_formats import FORMAT_NONE

from Tkinter import *
API_KEY = '###### YOUR API KEY #########'

class pastebinGUI:
    
    def __init__(self,root):
        frame=Frame(root)
        self.makeMenuBar(frame)
        self.createTitleTextArea(frame)
        self.createContentTextArea(frame)
        frame.pack()

    def createTitleTextArea(self,frame):
        Label(frame, text='---------------------------------').pack(side=TOP)
        Label(frame, text='caption').pack(side=TOP)
        self.title = StringVar()
        entry = Entry(frame,textvariable=self.title)
        entry.pack(side=TOP)
        Label(frame, text='---------------------------------').pack(side=TOP)
        
    def createContentTextArea(self,frame):
        Label(frame, text='Content').pack(side=TOP)
        textContentFrame = Frame(frame)
        self.contentArea = Text(textContentFrame,height = 10,width = 50,background='white')
        scroll = Scrollbar(textContentFrame)
        self.contentArea.configure(yscrollcommand = scroll.set)
        self.contentArea.pack(side = LEFT)
        scroll.pack(side = RIGHT,fill = Y)
        textContentFrame.pack(side = BOTTOM)
    
    def makeMenuBar(self,frame):
        menubar = Frame(frame,relief = RAISED,borderwidth = 1)
        menubar.pack()
        mb_pastebin = Menubutton(menubar,text = 'PASTEBIN')
        mb_pastebin.pack(side = LEFT)
        mb_pastebin.menu = Menu(mb_pastebin)
        mb_pastebin.menu.add_command(label = 'publish',command = self.publish)
        mb_pastebin['menu'] = mb_pastebin.menu
 
    def publish(self):
        content = self.contentArea.get('1.0',END)
        pbin = PastebinPython(api_dev_key=API_KEY)
        try:
            print pbin.createPaste(content, self.title.get(), FORMAT_NONE, PASTE_PUBLIC, EXPIRE_1_MONTH)
        except PastebinBadRequestException as e:
            print e.message
        except PastebinFileException as e:
            print e.message


def main():
    root = Tk()
    pastebinGUI(root)
    root.title('PASTEBIN-GUI')
    root.mainloop()

main()