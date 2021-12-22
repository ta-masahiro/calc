from tkinter import *
 
 
def func(v):
    var1.set(var1.get() + v)
 
 
def clear():
    var1.set("")
 
 
def result():
    try:
        var1.set(eval(var1.get()))
    except SyntaxError:
        var1.set("SyntaxError")
    except ZeroDivisionError:
        var1.set("ZeroDivisionError")
    except NameError:
        var1.set("NameError")
 
 
root = Tk()
 
# すべてのウィジェットのフォント指定
root.option_add("*Font", "Consolas 14")
 
var1 = StringVar()
 
# 0行目
label = Label(root, textvariable=var1, foreground="#ffffff", background="#000000", anchor=E, height=2)
label.grid(row=0, column=0, columnspan=4, sticky="EW")
 
# 1行目
btn_7 = Button(root, text="7", command=lambda: func("7"), width=5, height=2)
btn_7.grid(row=1, column=0)
 
btn_8 = Button(root, text="8", command=lambda: func("8"), width=5, height=2)
btn_8.grid(row=1, column=1)
 
btn_9 = Button(root, text="9", command=lambda: func("9"), width=5, height=2)
btn_9.grid(row=1, column=2)
 
btn_div = Button(root, text="/", command=lambda: func("/"), width=5, height=2)
btn_div.grid(row=1, column=3)
 
# 2行目
btn_4 = Button(root, text="4", command=lambda: func("4"), width=5, height=2)
btn_4.grid(row=2, column=0)
 
btn_5 = Button(root, text="5", command=lambda: func("5"), width=5, height=2)
btn_5.grid(row=2, column=1)
 
btn_6 = Button(root, text="6", command=lambda: func("6"), width=5, height=2)
btn_6.grid(row=2, column=2)
 
btn_mul = Button(root, text="*", command=lambda: func("*"), width=5, height=2)
btn_mul.grid(row=2, column=3)
 
# 3行目
btn_1 = Button(root, text="1", command=lambda: func("1"), width=5, height=2)
btn_1.grid(row=3, column=0)
 
btn_2 = Button(root, text="2", command=lambda: func("2"), width=5, height=2)
btn_2.grid(row=3, column=1)
 
btn_3 = Button(root, text="3", command=lambda: func("3"), width=5, height=2)
btn_3.grid(row=3, column=2)
 
btn_sub = Button(root, text="-", command=lambda: func("-"), width=5, height=2)
btn_sub.grid(row=3, column=3)
 
# 4行目
btn_0 = Button(root, text="0", command=lambda: func("0"), width=5, height=2)
btn_0.grid(row=4, column=0)
 
btn_c = Button(root, text="C", command=clear, width=5, height=2)
btn_c.grid(row=4, column=1)
 
btn_e = Button(root, text="=", command=result, width=5, height=2)
btn_e.grid(row=4, column=2)
 
btn_add = Button(root, text="+", command=lambda: func("+"), width=5, height=2)
btn_add.grid(row=4, column=3)
 
root.mainloop()
