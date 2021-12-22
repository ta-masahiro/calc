# -*- coding:utf-8 -*-
import tkinter

# マウスボタンが押されていているかどうかの判断用
press = False

def mouse_move_func(event):
    global canvas

    # 現在のマウスの位置
    x = event.x
    y = event.y

    # マウスボタンが押されている時だけ円を描画
    if press:
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill = "blue", width=0)


def mouse_click_func(event):
    global press

    # マウスボタンが押された
    press = True

def mouse_release_func(event):
    global press

    # マウスボタンが離された
    press = False

# アプリの作成
app = tkinter.Tk()

# アプリの画面設定
app.geometry(
    "400x400" # アプリ画面のサイズ
)
app.title(
    "サンプルアプリ" # アプリのタイトル
)

# キャンバスの作成
canvas = tkinter.Canvas(
    app, # キャンバスの作成先アプリ
    width = 400, # キャンバスの横サイズ
    height = 400, # キャンバスの縦サイズ
    bg = "white" # キャンバスの色
)

# キャンバスの配置
canvas.pack()

# イベントの受付
app.bind(
    "<Motion>", # 受付けるイベント
    mouse_move_func # そのイベント時に実行する関数
)

app.bind(
    "<ButtonPress>", # 受付けるイベント
    mouse_click_func # そのイベント時に実行する関数
)

app.bind(
    "<ButtonRelease>", # 受付けるイベント
    mouse_release_func # そのイベント時に実行する関数
)

# アプリの待機
app.mainloop()
