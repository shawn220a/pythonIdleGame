import tkinter as tk
from tkinter import ttk
import time

FormatMoney = '${:0,.2f}'

print('Welcome to Python Idle Tycoon!!!!')


class StoreTimer():
    UpdateFreq = 100

    def __init__(self, store):
        self.Timer = store.Timer
        self.store = store
        self.StartTimer()

    def StartTimer(self):
        self.startTime = time.time()
        root.after(StoreTimer.UpdateFreq, self.UpdateTimer)

    def UpdateTimer(self):
        elapsed = time.time() - self.startTime

        if elapsed < self.Timer:
            self.store.progressBar['value'] = elapsed / self.Timer * 100
            root.after(StoreTimer.UpdateFreq, self.UpdateTimer)
        else:
            self.store.progressBar['value'] = 0
            self.store.MakeMoney()

            if self.store.ManagerUnlocked == True:
                self.StartTimer()


class Store():
    Money = 25.00
    Day = 1
    StoreList = []

    def __init__(self, storeName, storeProfit, storeCost, storeTimer, managerCost):
        self.StoreName = storeName
        self.StoreCount = 0
        self.StoreProfit = storeProfit
        self.StoreCost = storeCost
        self.Timer = storeTimer
        self.ManagerUnlocked = False
        self.ManagerCost = managerCost

    @classmethod
    def DisplayStores(cls):
        store_label_col1 = tk.Label(root, text='Store Name')
        store_label_col1.grid(row=4, column=0)

        store_label_col2 = tk.Label(root, text='Progress')
        store_label_col2.grid(row=4, column=1)

        store_label_col3 = tk.Label(root, text='Store Cost')
        store_label_col3.grid(row=4, column=2)

        store_label_col4 = tk.Label(root, text='Store Count')
        store_label_col4.grid(row=4, column=3)

        store_label_col5 = tk.Label(root, text='Buy Store')
        store_label_col5.grid(row=4, column=4)

        store_label_col6 = tk.Label(root, text='Buy Manager')
        store_label_col6.grid(row=4, column=5)

        storeIndex = 1

        for store in cls.StoreList:
            store.DisplayStoreInfo(storeIndex)
            storeIndex += 1

    def ClickStore(self):
        StoreTimer(self)

    def MakeMoney(self):
        DailyProfit = self.StoreProfit * self.StoreCount
        Store.Money += DailyProfit
        Game.UpdateUI()

    def DisplayStoreInfo(self, storeIndex):
        self.clickStoreButton = tk.Button(
            root, text=self.StoreName, command=lambda: self.ClickStore())
        self.clickStoreButton.grid(row=4 + storeIndex, column=0)

        self.progressBar = ttk.Progressbar(
            root, value=0, maximum=100, orient=tk.HORIZONTAL, length=100, mode='indeterminate')
        self.progressBar.grid(row=4 + storeIndex, column=1)

        self.storeCostLabel = tk.Label(
            root, text=FormatMoney.format(self.StoreCost))
        self.storeCostLabel.grid(row=4 + storeIndex, column=2)

        self.storeCountLabel = tk.Label(root, text=self.StoreCount)
        self.storeCountLabel.grid(row=4 + storeIndex, column=3)

        self.clickBuyButton = tk.Button(
            root, text='Buy', command=lambda: self.BuyStore())
        self.clickBuyButton.grid(row=4 + storeIndex, column=4)

        self.clickBuyManagerButton = tk.Button(
            root, text='Manager: ' + FormatMoney.format(self.ManagerCost), command=lambda: self.UnlockManager())
        self.clickBuyManagerButton.grid(row=4 + storeIndex, column=5)

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
        Store.StoreList.append(Store('Lemonade Stand', 1.50, 3, 3, 100))
        Store.StoreList.append(Store('Record Store', 5, 15, 10, 200))
        Store.StoreList.append(Store('Ice Cream Store', 10, 90, 30, 1000))

    def DisplayGameHeader(self):
        root.title('Python Idle Tycoon Business Game')

        root.geometry('700x300')

        money_label = tk.Label(root, text='Money')
        money_label.grid(row=0, column=0)
        self.moneyAmount_label = tk.Label(
            root, text=FormatMoney.format(Store.Money))
        self.moneyAmount_label.grid(row=1, column=0)

    def DisplayStoreList(self):
        Store.DisplayStores()

    def UpdateUI(self):
        self.moneyAmount_label.config(text=FormatMoney.format(Store.Money))


root = tk.Tk()

Game = GameManager()

root.mainloop()
