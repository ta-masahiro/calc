import tkinter as tk # Tkinterをインポート
fonts=("", 16) # フォントの書式とサイズを指定

class Calculator(tk.Frame):
    #ウィンドウの作成
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master.geometry()
        self.master.title('Calculator') # ウィンドウタイトルを指定
        self.entry = tk.Entry(self.master, justify='right', font=fonts) # テキストボックスを作成
        self.creat_widgets()

    #入力
    def input(self, num):
        def n():
            self.entry.insert(tk.END, num)
        return n

    #パーセント表示
    def one_hundredth(self):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, eval(text + '/100'))

    #計算を全てクリア
    def clear_all(self):
        self.entry.delete(0, tk.END)

    #1文字削除
    def clear_one(self):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text[:-1])

    #計算結果を表示
    def equals(self):
        self.value = eval(self.entry.get().replace('÷', '/').replace('×', '*').replace('＋', '+').replace('－', '-'))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.value)

    #ディスプレイ部分を作成
    def creat_widgets(self):
        Buttons = [ 
        ['7', '8', '9'], 
        ['4', '5', '6'], 
        ['1', '2', '3'], 
        ]

        # 各ボタンを配置
        for i, ro in enumerate(Buttons):
            for j, co in enumerate(ro):
                tk.Button(self.master, font=fonts, text=co, width=10, height=2, command=self.input(co)).grid(row=i+2, column=j)

        # テキストボックスを配置
        self.entry.grid(row=0, column=0, ipady=10, columnspan=4, sticky='nsew')
        
        # 各ボタンの処理
        tk.Button(self.master, text='%', font=fonts, width=10, height=2, command=lambda: self.one_hundredth()).grid(row=1, column=0)
        tk.Button(self.master, text='CE', font=fonts, width=10, height=2, command=lambda: self.clear_all()).grid(row=1, column=1)
        tk.Button(self.master, text='←', font=fonts, width=10, height=2, command=lambda: self.clear_one()).grid(row=1, column=2)
        tk.Button(self.master, text='÷', font=fonts, width=10, height=2, command=self.input('÷')).grid(row=1, column=3)
        tk.Button(self.master, text='×', font=fonts, width=10, height=2, command=self.input('×')).grid(row=2, column=3)
        tk.Button(self.master, text='－', font=fonts, width=10, height=2, command=self.input('－')).grid(row=3, column=3)
        tk.Button(self.master, text='＋', font=fonts, width=10, height=2, command=self.input('＋')).grid(row=4, column=3)
        tk.Button(self.master, text='＝', font=fonts, width=10, height=2, command=lambda: self.equals()).grid(row=5, column=3)
        tk.Button(self.master, text='0', font=fonts, width=21, height=2, command=self.input('0')).grid(row=5, column=0, columnspan=2)
        tk.Button(self.master, text='.', font=fonts, width=10, height=2, command=self.input('.')).grid(row=5, column=2)

# 実行
calc = Calculator(tk.Tk())
calc.mainloop()
