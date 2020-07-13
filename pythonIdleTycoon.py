print('Welcome to Python Idle Tycoon!!!!')


class Store():
    Money = 25.00
    Day = 1

    def __init__(self):
        self.StoreName = 'Lemonade Stand'
        self.StoreCount = 0
        self.StoreProfit = 1.50
        self.StoreCost = 3

    def DisplayStoreInfo(self):
        print('------------------------------------')
        print('Day #' + str(Store.Day))
        print('Money = $' + str(Store.Money))
        print('Store Count = ' + str(self.StoreCount))
        print('------------------------------------')

    def BuyStore(self):
        if self.StoreCost <= Store.Money:
            self.StoreCount += 1
            Store.Money -= self.StoreCost
        else:
            print('You don\'t have enough money.')

    # def NextDay(self):
    #     Store.Day += 1
    #     DailyProfit = self.StoreProfit * self.StoreCount
    #     Store.Money += DailyProfit


newstore = Store()
print(newstore.StoreName)
newstore.BuyStore()
print(newstore.StoreCount)

# while True:
#     DisplayStoreInfo()

#     print('Available option (N)ext Day, (B)uy Store, (Q)uit')
#     result = input('Please Enter Your Selection:')

#     if result == 'B' or result == 'b':
#         StoreCount, Money = BuyStore(StoreCount, Money)
#     elif result == 'N' or result == 'n':
#         Day, Money = NextDay(Day, Money)
#     elif result == 'Q' or result == 'q':
#         break
#     else:
#         print('Invalid Input. Try Again.')

print('Thank you for playing Python Idle Tycoon')
