print('Welcome to Python Idle Tycoon!!!!')

Money = 25.00
Day = 1
StoreName = 'Lemonade Stand'
StoreCount = 0
StoreProfit = 1.50
StoreCost = 3


def DisplayStoreInfo():
    print('------------------------------------')
    print('Day #' + str(Day))
    print('Money = $' + str(Money))
    print('Store Count = ' + str(StoreCount))
    print('------------------------------------')


def BuyStore(StoreCount, Money):
    if StoreCost <= Money:
        StoreCount += 1
        Money -= StoreCost
    else:
        print('You don\'t have enough money.')
    return (StoreCount, Money)


def NextDay(Day, Money):
    Day += 1
    DailyProfit = StoreProfit * StoreCount
    Money += DailyProfit
    return (Day, Money)


while True:
    DisplayStoreInfo()

    print('Available option (N)ext Day, (B)uy Store, (Q)uit')
    result = input('Please Enter Your Selection:')

    if result == 'B' or result == 'b':
        StoreCount, Money = BuyStore(StoreCount, Money)
    if result == 'N' or result == 'n':
        Day, Money = NextDay(Day, Money)
    if result == 'Q' or result == 'q':
        break

print('Thank you for playing Python Idle Tycoon')
