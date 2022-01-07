from tkinter import ttk
from tkinter import Tk
from tkinter import StringVar

#レイアウトを作成するために下記のようにすると楽だそうです
LAYOUT = [
    ['SUM+', '1/x', 'SQRT', 'LOG', 'LN'],
    ['SWP', 'RD', 'SIN', 'COS', 'TAN'], 
    ['USR', 'PGM', 'XEQ', 'SST', 'BAK'], 
    ['ON', 'f', 'a', 'STO', 'RCL'], 
    ['CHS', '-', '7', '8', '9'],
    ['EE', '+', '4', '5', '6'],
    ['ent', '*', '1', '2', '3'],
    [' ', '/', '0', '.', 'R/S'],
]

#記号をまとめた定数、if char in CAlC_SYMBOLS:…のように使うために定義しておく
CAlC_SYMBOLS = ('+', '-', '', '/', '*', '//')

class CalcApp(ttk.Frame):
  """ 電卓アプリ """
  def __init__(self, master=None):
     super().__init__(master)
     self.exp_list =['0']
     self.create_style()
     self.create_widgets()

  def create_style(self):
     """ボタン、ラベルのスタイルを変更"""
     style = ttk.Style()
     style.theme_use('default')

     #ラベルのスタイルを上書き
     style.configure('TLabel', font=('Helvetica', 10), background='black', foreground='white')

     #ボタンのスタイルを上書き
     style.configure('TButton', font=('Helvetica', 10))
  def create_widgets(self):  #ウィジェットの作成と配置

     #計算結果の表示ラベル
     self.display_var = StringVar()
     self.display_var.set('0') #初期値を0にする
     dispay_label = ttk.Label(self, textvariable=self.display_var)
     dispay_label.grid(column=0, row=0, columnspan=5, sticky='N, S, E, W')

     #レイアウトの作成
     for y, row in enumerate(LAYOUT, 1):
         for x, char in enumerate(row):
             button = ttk.Button(self, text=char)
             button.grid(column=x, row=y, sticky='N, S, E, W')
             button.bind('<Button-1>', self.calc)
     self.grid(column=0, row=0, sticky='N, S, E, W')  #これを忘れると表示されないので注意

     #各列の引き伸ばし設定
     self.columnconfigure(0, weight=1)
     self.columnconfigure(1, weight=1)
     self.columnconfigure(2, weight=1)
     self.columnconfigure(3, weight=1)
     self.columnconfigure(4, weight=1)
     self.columnconfigure(5, weight=1)

     #各行の引き伸ばし設定
     self.rowconfigure(0, weight=0)
     self.rowconfigure(1, weight=1)
     self.rowconfigure(2, weight=1)
     self.rowconfigure(3, weight=1)
     self.rowconfigure(4, weight=1)
     self.rowconfigure(5, weight=1)
     self.rowconfigure(6, weight=1)
     self.rowconfigure(7, weight=1)
     self.rowconfigure(8, weight=1)

     #トップレベルのウィジェットも引き伸ばしに対応させる
     self.master.columnconfigure(0, weight=1)
     self.master.rowconfigure(0, weight=1) 
  def calc(self, event):

     #押されたボタンのテキストを取得
     char = event.widget['text']

     #最後に押したボタンの内容
     last = self.exp_list[-1]

     #=を押した時
     if char == '=':
         if last in CAlC_SYMBOLS:
             self.exp_list.pop()
         exp = eval(''.join(self.exp_list))
         self.exp_list = [str(exp)]

     #ACを押した場合
     elif char == 'AC':
         self.exp_list = ['0']

     #Cを押した場合
     elif char == 'C':
         if len(self.exp_list) == 1:
             self.exp_list = ['0']
         else:
             self.exp_list = self.exp_list[:-1]

     #各演算記号を押した場合
     elif char in CAlC_SYMBOLS:
         if last == char == '/':
             self.exp_list[-1] += '/'
         elif last == char == '*':
             self.exp_list[-1] += '*'
         elif last in CAlC_SYMBOLS:
             self.exp_list[-1] = char
         else:
             self.exp_list.append(char)

     #数値のボタンを押した場合
     else:
         if last == '0':
             self.exp_list[-1] = char
         elif last in CAlC_SYMBOLS:
             self.exp_list.append(char)
         else:
             self.exp_list[-1] += char
     self.display_var.set(''.join(self.exp_list))

def main():
     root = Tk()
     root.title('簡易電卓')
     CalcApp(root)
     root.mainloop()

if __name__ == '__main__':
     main()
