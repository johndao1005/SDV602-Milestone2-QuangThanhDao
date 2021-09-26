# matplotlib
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
#tkinter
import tkinter as tk
from tkinter import ttk
#work with url and json file
from datetime import date
import requests
import json
#pandas and numpy
import pandas as pd
import numpy as np

large_font = ("Verdana",12)
normal_font = ("Verdana",10)
small_font = ("Verdana",8)
style.use("ggplot")# other option dark_background,


f = Figure()
a = f.add_subplot(111) # 111 is plot number 1 and 121 is plot number 2

exchange = "BTC-e"
DatCounter = 9000
programName = "btce"

def changeExchange(toWhat,pn):
    global exchange
    global DatCounter
    global programName
    exchange = toWhat
    programName = pn
    DatCounter = 9000
    

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=normal_font)
    label.pack(side="top",fill="x",pady=10)
    button1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    popup.mainloop()
        

def animate(i):
    #ANCHOR first version
    # pullData = open("sample_data.txt","r").read()
    # dataList = pullData.split("\n")
    # xList = []
    # yList = []
    # for eachLine in dataList:
    #     if len(eachLine)>1:
    #         x,y = eachLine.split(",")
    #         xList.append(int(x))
    #         yList.append(int(y))
    # a.clear()
    # a.plot(xList,yList)
    
    #read data
    #with open(datasource, "r") as data:
    #   dataList = data.read().split("\n")
    #   for eachLine in dataList:
    #if len(eachLine)>1:
    #         x,y = eachLine.split(",")
    #         xList.append(int(x))
    #         yList.append(int(y))
    #append data
    # with open(datasource, "a") as data:
    #   
    
    
    #ANCHOR
    # API link
    # dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'#add parameter after the api link with ? and the paramter like limit = 2000
    # using urllib to open datalink
    # data = request.urlopen(dataLink)
    # read data from byte and change to utf-8
    # print(data)
    # data = data.readall().decode("utf-8")
    # print(data)
    # load the data with json
    # data = json.loads(data)
    # # using the key to get the value
    # data = data["btc_usd"]
    #  using pandas to change to pandas data set
    # data = pd.DataFrame(data)
    
    # buys = data[(data['type']== "bid")]
    # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
    # buyDates = (buys["datestamp"]).tolist()
    
    # sells = data[(data['type']== "ask")]
    # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
    # sellDates = (sells["datestamp"]).tolist()
    
    # a.clear()
    # a.plot_date(buyDates,buys["price"])
    # a.plot_date(sellDates,sells["price"])
    
    # btc ban 
    dataLink = "https://cex.io/api/trade_history/BTC/USD/?status=200"
    data = requests.request("GET", dataLink)
    data = data.json()
    df = pd.DataFrame(data)

    buys = df[(df['type'] == "buy")]
    buy_arr = buys['date'].to_numpy()
    blist = []
    for i in buy_arr:
        # print(i)
        abuy = date.fromtimestamp(int(i))
        blist.append(abuy)

    buys["datestamp"] = blist
    print(buys["datestamp"])

    buyDates = (buys["datestamp"]).tolist()


    sells = df[(df['type'] == "sell")]
    sell_arr = sells['date'].to_numpy()
    slist = []
    for i in sell_arr:
        # print(i)
        asell = date.fromtimestamp(int(i))
        slist.append(asell)

    sells["datestamp"] = slist
    sellDates = (sells["datestamp"]).tolist()

    # print(buyDates)
    # print(sellDates)

    a.clear()
    a.plot_date(buyDates, buys["price"], "#00a3e0", label="buys")
    a.plot_date(sellDates, sells["price"], "#183a54", label="sells")

    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)

    title = "BTC-e BTCUSD prices\n Last Price: "+str(df["price"][999])
    a.set_title(title)
    
    
class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side = 'top',fill = 'both', expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Save settings",command = lambda: popupmsg("Not support yet"))
        filemenu.add_separator()
        filemenu.add_command(label = "exit",command = quit)
        menubar.add_cascade(label = "File",menu=filemenu)
        
        exchangeChoice = tk.Menu(menubar,tearoff=1)
        exchangeChoice.add_command(label="BTC-e",
                                   command = lambda: changeExchange("BTC-e","btce"))
        exchangeChoice.add_command(label="Bitfinex",
                                   command = lambda: changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="Bitstamp",
                                   command = lambda: changeExchange("Bitstamp","bitstamp"))
        menubar.add_cascade(label ="exchange" ,menu =exchangeChoice)
        
        dataTF = tk.Menu(menubar,tearoff=1)
        dataTF.add_command(label="Tick",
                                   command = lambda: changeTimeFrame("tick"))
        dataTF.add_command(label="1 Day",
                                   command = lambda: changeTimeFrame("1d"))
        dataTF.add_command(label="3 Days",
                                   command = lambda: changeTimeFrame("3d"))
        dataTF.add_command(label="7 Days",
                                   command = lambda: changeTimeFrame("7d"))
        menubar.add_cascade(label ="Data Time Frame" ,menu =dataTF)
        
        exchangeChoice = tk.Menu(menubar,tearoff=1)
        exchangeChoice.add_command(label="BTC-e",
                                   command = lambda: changeExchange("BTC-e","btce"))
        exchangeChoice.add_command(label="Bitfinex",
                                   command = lambda: changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="Bitstamp",
                                   command = lambda: changeExchange("Bitstamp","bitstamp"))
        menubar.add_cascade(label ="exchange" ,menu =exchangeChoice)
        
        tk.Tk.config(self,menu=menubar)
        
        self.frames ={}
        for DES in (StartPage,PageOne,PageTwo,PageThree):
            frame = DES(container, self)
            self.frames[DES] = frame
            frame.grid(row=0,column = 0, sticky = "nsew")
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="STart Page")
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text ="Visit Page 1",
                            command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text ="Visit Page 2",
                            command=lambda:controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text ="Visit Page 3",
                            command=lambda:controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text ="Visit Page 4",
                            command=lambda:controller.show_frame(PageOne))
        button4.pack()
        
class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page One")
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text ="Back To Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text ="Visit Page 1",
                            command=lambda:controller.show_frame(PageTwo))
        button2.pack()
        
class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Page Two")
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text ="Back To Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text ="Page PageOne",
                            command=lambda:controller.show_frame(PageOne))
        button2.pack()
        
class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Graph Page")
        label.pack(pady=10,padx=10)
        
        # graph
        
        canvas = FigureCanvasTkAgg(f, self,)
        canvas.draw()
        
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack()
        canvas.get_tk_widget().pack(expand=True)
        
        # buttons
        button1 = ttk.Button(self, text ="Back To Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
        # button2 = ttk.Button(self, text ="Visit Page 1",
        #                     command=lambda:controller.show_frame(PageOne))
        # button2.pack()
        # button3 = ttk.Button(self, text ="Visit Page 1",
        #                     command=lambda:controller.show_frame(PageTwo))
        # button3.pack()
        
        
if __name__ == "__main__":    
    app = App()
    app.geometry("1280x720")
    ani = animation.FuncAnimation(f,animate, interval = 5000)
    app.mainloop()