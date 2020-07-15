print('Welcome to Python Idle Tycoon!!!!')


class Store():
    Money = 25.00
    Day = 1

    def __init__(self):
        self.StoreName = 'Lemonade Stand'
        self.StoreCount = 0
        self.StoreProfit = 1.50
        self.StoreCost = 3

    @classmethod
    def DisplayGameInfo(cls):
        print('------------------------------------')
        print('Day #' + str(cls.Day))
        print('Money = ${:0, .2f}'.format(cls.Money))
        print('------------------------------------')

    def DisplayStoreInfo(self):
        print('------------------------------------')
        print('Store Name %s, Store Count = %d' % (self.StoreName, self.StoreCount))
        print('------------------------------------')

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


CurrentStore = Store()

while True:
    Store.DisplayGameInfo()
    CurrentStore.DisplayStoreInfo()
    print('Available option (N)ext Day, (B)uy Store, (Q)uit')
    result = input('Please Enter Your Selection:')

    if result == 'B' or result == 'b':
        CurrentStore.BuyStore()
    elif result == 'N' or result == 'n':
        CurrentStore.NextDay()
    elif result == 'Q' or result == 'q':
        break
    else:
        print('Invalid Input. Try Again.')

print('Thank you for playing Python Idle Tycoon')
