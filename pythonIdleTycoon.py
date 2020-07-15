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
    def DisplayGameInfo(cls):
        print('------------------------------------')
        print('Day #' + str(cls.Day))
        print('Money = ${:0,.2f}'.format(cls.Money))
        print('------------------------------------')
        print('Stores'.ljust(25) + 'Store Cost'.ljust(15) + 'Store Count')

        for store in cls.StoreList:
            store.DisplayStoreInfo()

        print('------------------------------------')

    def DisplayStoreInfo(self):
        StoreCostStr = '${:0,.2f}'.format(self.StoreCost).rjust(12)

        print(self.StoreName.ljust(20) +
              StoreCostStr.ljust(20) + str(self.StoreCount))

    def BuyStore(self):
        if self.StoreCost <= Store.Money:
            self.StoreCount += 1
            Store.Money -= self.StoreCost
        else:
            print('You don\'t have enough money.')

    def NextDay(self):
        Store.Day += 1
        DailyProfit = self.StoreProfit * self.StoreCount
        Store.Money += DailyProfit


Store.StoreList.append(Store('Lemonade Stand', 1.50, 3))
Store.StoreList.append(Store('Record Store', 5, 15))
Store.StoreList.append(Store('Ice Cream Store', 10, 90))

while True:
    Store.DisplayGameInfo()
    print('Available option (N)ext Day, (B)uy Store, (Q)uit')
    result = input('Please Enter Your Selection:')

    if result == 'B' or result == 'b':
        Store.StoreList[0].BuyStore()
    elif result == 'N' or result == 'n':
        Store.StoreList[0].NextDay()
    elif result == 'Q' or result == 'q':
        break
    else:
        print('Invalid Input. Try Again.')

print('Thank you for playing Python Idle Tycoon')
