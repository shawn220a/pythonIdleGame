import tkinter as tk

FormatMoney = '${:0,.2f}'

print('Welcome to Python Idle Tycoon!!!!')


class Store():
    Money = 25.00
    Day = 1
    StoreList = []

    def __init__(self, storeName, storeProfit, storeCost):
        self.StoreName = storeName
        self.StoreCount = 0
        self.StoreProfit = storeProfit
        self.StoreCost = storeCost

    @classmethod
    def DisplayStores(cls):
        store_label_col1 = tk.Label(root, text='Store Name')
        store_label_col1.grid(row=4, column=0)

        store_label_col2 = tk.Label(root, text='Store Cost')
        store_label_col2.grid(row=4, column=1)

        store_label_col3 = tk.Label(root, text='Store Count')
        store_label_col3.grid(row=4, column=2)

        storeIndex = 1

        for store in cls.StoreList:
            store.DisplayStoreInfo(storeIndex)
            storeIndex += 1

    @classmethod
    def NextDay(cls):
        cls.Day += 1

        for store in cls.StoreList:
            DailyProfit = store.StoreProfit * store.StoreCount
            cls.Money += DailyProfit

    def DisplayStoreInfo(self, storeIndex):
        self.storeNameLabel = tk.Label(root, text=self.StoreName)
        self.storeNameLabel.grid(row=4 + storeIndex, column=0)

        self.storeCostLabel = tk.Label(root, text=FormatMoney.format(self.StoreCost))
        self.storeCostLabel.grid(row=4 + storeIndex, column=1)

        self.storeCountLabel = tk.Label(root, text=self.StoreCount)
        self.storeCountLabel.grid(row=4 + storeIndex, column=2)

    def SelectStore(self):
        try:
            whichStore = int(
                input('Which Store do you wish to buy? (1-%s):' % len(Store.StoreList)))
        except:
            print('Invalid Input. Buy Aborted')
            return

        self.VerifyStore(whichStore)

    def BuyStore(self, store):
        if store.StoreCost <= Store.Money:
            store.StoreCount += 1
            Store.Money -= store.StoreCost
        else:
            print('You don\'t have enough money.')

    def VerifyStore(self, whichStore):
        if whichStore >= 1 and whichStore <= len(Store.StoreList):
            self.BuyStore(Store.StoreList[whichStore - 1])
        else:
            print('Invalid Selection. Enter a number 1-%s' %
                  len(Store.StoreList))


class GameManager():
    def __init__(self):
        self.CreateStore()
        self.DisplayGameHeader()
        Store.DisplayStores()

    def CreateStore(self):
        Store.StoreList.append(Store('Lemonade Stand', 1.50, 3))
        Store.StoreList.append(Store('Record Store', 5, 15))
        Store.StoreList.append(Store('Ice Cream Store', 10, 90))

    def DisplayGameHeader(self):
        root.title('Python Idle Tycoon Business Game')

        root.geometry('700x300')

        money_label = tk.Label(root, text='Money')
        money_label.grid(row=0, column=0)
        moneyAmount_label = tk.Label(
            root, text=FormatMoney.format(Store.Money))
        moneyAmount_label.grid(row=1, column=0)

        day_label = tk.Label(root, text='Day')
        day_label.grid(row=0, column=1)
        dayAmount_label = tk.Label(root, text=Store.Day)
        dayAmount_label.grid(row=1, column=1)

    def DisplayStoreList(self):
        pass


root = tk.Tk()

Game = GameManager()

root.mainloop()
