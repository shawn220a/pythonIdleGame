FormatMoney = '${:0,.2f}'
Divider = '------------------------------------'


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
        print(Divider)
        print('Day #' + str(cls.Day))
        print('Money = %s' % FormatMoney.format(cls.Money))
        print(Divider)
        print('Stores'.ljust(25) + 'Store Cost'.ljust(15) + 'Store Count')

        storeIndex = 1

        for store in cls.StoreList:
            store.DisplayStoreInfo(storeIndex)
            storeIndex += 1

        print(Divider)

    @classmethod
    def NextDay(cls):
        cls.Day += 1

        for store in cls.StoreList:
            DailyProfit = store.StoreProfit * store.StoreCount
            cls.Money += DailyProfit

    def DisplayStoreInfo(self, storeIndex):
        StoreCostStr = FormatMoney.format(self.StoreCost).rjust(12)

        print(str(storeIndex) + ') ' + self.StoreName.ljust(17) +
              StoreCostStr.ljust(20) + str(self.StoreCount))

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
