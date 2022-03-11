import datetime
import urllib.request
from lxml import html
import tkinter as tk


root = tk.Tk()
root.title("比特币实时价格：")
root.geometry("500x140")
root.iconbitmap("./img/bitcoin_1.ico")
root.config(bg="black")

frm = tk.Frame(root, bg="black")
frm.pack(pady=20)

logo = tk.PhotoImage(file="./img/bitcoin_2.png")
cvs = tk.Canvas(frm, bg="black", width=100, height=100, highlightthickness=0)
cvs.grid(row=0, column=0, rowspan=2)
cvs.create_image(50, 50, image=logo)

lbl_bc = tk.Label(frm, text="Price", font=("Ds-Digital", 45), bg="black", fg="cyan", bd=0)
lbl_bc.grid(row=0, column=1, padx=20, sticky=tk.S)

lbl_time = tk.Label(frm, text="datetime", font=("Ds-Digital", 20), bg="black", fg="cyan", bd=0)
lbl_time.grid(row=1, column=1, sticky=tk.N)


def price_update():
    url = "https://www.coindesk.com/price/bitcoin"
    rsp = urllib.request.urlopen(url)

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    if rsp.status == 200:
        src = html.fromstring(rsp.read().decode())
        price = src.xpath("//div[@class='price-large']/text()")[0]

        lbl_bc.config(text=f"$ {price}")
        lbl_time.config(text=time)

        root.after(10000, price_update)
        print("中国时间:{0} 比特币的价格:{1}".format(time, price))
    else:
        print("中国时间:{0} 比特币的价格取得失败".format(time))


price_update()
root.mainloop()
