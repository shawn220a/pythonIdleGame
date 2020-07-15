import tkinter as tk
import storeManager as Sm

FormatMoney = '${:0,.2f}'

print('Welcome to Python Idle Tycoon!!!!')

class GameManager():
    def __init__(self):
        self.CreateStore()
        self.DisplayGameHeader()

    def CreateStore(self):
        Sm.Store.StoreList.append(Sm.Store('Lemonade Stand', 1.50, 3))
        Sm.Store.StoreList.append(Sm.Store('Record Store', 5, 15))
        Sm.Store.StoreList.append(Sm.Store('Ice Cream Store', 10, 90))

    def DisplayGameHeader(self):
        root.title('Python Idle Tycoon Business Game')

        root.geometry('700x300')

        money_label = tk.Label(root, text='Money')
        money_label.grid(row=0, column=0)
        moneyAmount_label = tk.Label(
            root, text=FormatMoney.format(Sm.Store.Money))
        moneyAmount_label.grid(row=1, column=0)

        day_label = tk.Label(root, text='Day')
        day_label.grid(row=0, column=1)
        dayAmount_label = tk.Label(root, text=Sm.Store.Day)
        dayAmount_label.grid(row=1, column=1)

root = tk.Tk()

Game = GameManager()

root.mainloop()
