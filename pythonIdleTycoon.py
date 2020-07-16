import tkinter as tk
from tkinter import ttk
import time
import csv

FormatMoney = '${:0,.2f}'
dataFile = 'data.csv'

print('Welcome to Python Idle Tycoon!!!!')


class StoreTimer():
    UpdateFreq = 100

    def __init__(self, store):
        self.Timer = store.Timer
        self.store = store
        self.TimerRunning = False

    def StartTimer(self):
        if self.TimerRunning == False:
            self.TimerRunning = True
            self.startTime = time.time()
            root.after(StoreTimer.UpdateFreq, self.UpdateTimer)

    def UpdateTimer(self):
        elapsed = time.time() - self.startTime

        if elapsed < self.Timer:
            self.store.progressBar['value'] = elapsed / self.Timer * 100
            root.after(StoreTimer.UpdateFreq, self.UpdateTimer)
        else:
            self.TimerRunning = False
            self.store.progressBar['value'] = 0
            self.store.MakeMoney()

            if self.store.ManagerUnlocked == True:
                self.StartTimer()


class Store():
    Money = 25.00
    StoreList = []

    def __init__(self, storeName, storeProfit, storeCost, storeTimer, managerCost):
        self.StoreName = storeName
        self.StoreCount = 0
        self.StoreProfit = float(storeProfit)
        self.StoreCost = float(storeCost)
        self.Timer = float(storeTimer)
        self.ManagerUnlocked = False
        self.ManagerCost = float(managerCost)
        self.TimerObject = StoreTimer(self)

    @classmethod
    def DisplayStores(cls):
        store_label_col1 = tk.Label(
            root, text='Store Name', font='Helvetica 12 bold')
        store_label_col1.grid(row=4, column=0, padx=15)

        store_label_col2 = tk.Label(
            root, text='Progress', font='Helvetica 12 bold')
        store_label_col2.grid(row=4, column=1, padx=15)

        store_label_col3 = tk.Label(
            root, text='Store Cost', font='Helvetica 12 bold')
        store_label_col3.grid(row=4, column=2, padx=15)

        store_label_col4 = tk.Label(
            root, text='Store Count', font='Helvetica 12 bold')
        store_label_col4.grid(row=4, column=3, padx=15)

        store_label_col5 = tk.Label(
            root, text='Buy Store', font='Helvetica 12 bold')
        store_label_col5.grid(row=4, column=4, padx=15)

        store_label_col6 = tk.Label(
            root, text='Buy Manager', font='Helvetica 12 bold')
        store_label_col6.grid(row=4, column=5, padx=15)

        storeIndex = 1

        for store in cls.StoreList:
            store.DisplayStoreInfo(storeIndex)
            storeIndex += 1

    def ClickStore(self):
        self.TimerObject.StartTimer()

    def MakeMoney(self):
        DailyProfit = self.StoreProfit * self.StoreCount
        Store.Money += DailyProfit
        Game.UpdateUI()

    def DisplayStoreInfo(self, storeIndex):
        self.clickStoreButton = tk.Button(
            root, text=self.StoreName, width=20, font='10', command=lambda: self.ClickStore())
        self.clickStoreButton.grid(row=4 + storeIndex, column=0, padx=15, pady=10)

        self.progressBar = ttk.Progressbar(
            root, value=0, maximum=100, orient=tk.HORIZONTAL, length=100, mode='indeterminate')
        self.progressBar.grid(row=4 + storeIndex, column=1, padx=15, pady=10)

        self.storeCostLabel = tk.Label(
            root, text=FormatMoney.format(self.StoreCost), font='10')
        self.storeCostLabel.grid(
            row=4 + storeIndex, column=2, padx=15, pady=10)

        self.storeCountLabel = tk.Label(root, text=self.StoreCount, font='10')
        self.storeCountLabel.grid(
            row=4 + storeIndex, column=3, padx=15, pady=10)

        self.clickBuyButton = tk.Button(
            root, text='Buy: ' + FormatMoney.format(self.StoreCost), font='10', command=lambda: self.BuyStore())
        self.clickBuyButton.grid(
            row=4 + storeIndex, column=4, padx=15, pady=10)

        self.clickBuyManagerButton = tk.Button(
            root, text='Manager: ' + FormatMoney.format(self.ManagerCost), font='10', command=lambda: self.UnlockManager())
        self.clickBuyManagerButton.grid(
            row=4 + storeIndex, column=5, padx=15, pady=10)

    def BuyStore(self):
        if self.StoreCost <= Store.Money:
            self.StoreCount += 1
            Store.Money -= self.StoreCost
            self.storeCountLabel.config(text=self.StoreCount)
            Game.UpdateUI()
        else:
            print('You don\'t have enough money.')

    def UnlockManager(self):
        if self.ManagerUnlocked == False:
            if self.ManagerCost <= Store.Money:
                self.ManagerUnlocked = True
                Store.Money -= self.ManagerCost
                self.storeCountLabel.config(text=self.StoreCount)
                Game.UpdateUI()
            else:
                print('You don\'t have enough money.')


class GameManager():
    def __init__(self):
        self.CreateStore()
        self.DisplayGameHeader()
        self.DisplayStoreList()

    def CreateStore(self):
        with open(dataFile, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                Store.StoreList.append(Store(*row))

    def DisplayGameHeader(self):
        root.title('Python Idle Tycoon Business Game')

        root.geometry('1000x300')

        self.moneyAmount_label = tk.Label(
            root, text=FormatMoney.format(Store.Money), font='Helvetica 18 bold')
        self.moneyAmount_label.grid(row=1, column=0)

    def DisplayStoreList(self):
        Store.DisplayStores()

    def UpdateUI(self):
        self.moneyAmount_label.config(text=FormatMoney.format(Store.Money))


root = tk.Tk()

Game = GameManager()

root.mainloop()
