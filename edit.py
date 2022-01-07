# https://qiita.com/TANAKA-V/items/7ad0ccd5d08fc2258d63
import tkinter as tk
from tkinter import filedialog

class SbTextFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        text = tk.Text(self,wrap='none',undo=True)
        x_sb = tk.Scrollbar(self,orient='horizontal')
        y_sb = tk.Scrollbar(self,orient='vertical')
        x_sb.config(command=text.xview)
        y_sb.config(command=text.yview)
        text.config(xscrollcommand=x_sb.set,yscrollcommand=y_sb.set)
        text.grid(column=0,row=0,sticky='nsew')
        x_sb.grid(column=0,row=1,sticky='ew')
        y_sb.grid(column=1,row=0,sticky='ns')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.text = text
        self.x_sb = x_sb
        self.y_sb = y_sb

def fileopen():
    global fname,textframe,root
    fname = filedialog.askopenfilename()
    f = open(fname,'r')
    lines = f.readlines()
    f.close()
    textframe.text.delete('1.0','end')
    for line in lines:
        textframe.text.insert('end',line)
    root.title('editor - '+fname)

def filesave():
    global fname,textframe
    if fname == '':
        return
    f = open(fname,'w')
    lines = textframe.text.get('1.0','end-1c')
    f.writelines(lines)
    f.close()

def textcopy():
    pass
def textcut():
    pass
def textpast():
    pass
def main():
    global fname,textframe,root
    fname = ''
    root = tk.Tk()
    root.title('editor')
    root.geometry('400x300')
    textframe = SbTextFrame(root)
    textframe.pack(side='top',fill='both',expand=True)
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar,tearoff=0)
    filemenu.add_command(label='Open',command=fileopen)
    filemenu.add_command(label='Save',command=filesave)
    filemenu.add_command(label='Exit',command=exit)
    editmenu = tk.Menu(menubar, tearoff = 0)
    editmenu.add_command(label = 'copy', command = textcopy)
    editmenu.add_command(label = 'cut', command = textcut)
    editmenu.add_command(label = 'paste', command = textpast)
    menubar.add_cascade(label='File',menu=filemenu)
    menubar.add_cascade(label='edit',menu=editmenu)
    root.config(menu=menubar)
    root.mainloop()

if __name__ == '__main__':
    main()
