print("""
█░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄██""")
class VendingMachine:
    def __init__(self):
        self.items = {'1': {'name': 'coca-cola', 'price': 2, 'quantity': 10},
                      '2': {'name': 'energy drink', 'price': 1.50, 'quantity': 3},
                      '3': {'name': 'coconut water', 'price': 1.50, 'quantity': 6},
                      '4': {'name': 'barbican', 'price': 1.50, 'quantity': 8},
                      '5': {'name': 'lays chips', 'price': 1.50, 'quantity': 5},
                      '6': {'name': 'Candy', 'price': 3.50, 'quantity': 15},
                      '7':{'name':'sandwhich','price':3.00,'quantity':5},
                      '8':{'name':'protein bar','price':1.00,'quantity':20}}
        self.balance = 0

    def display_items(self):
        print("Available items:")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f} - Quantity: {item['quantity']}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}, Total Balance: ${self.balance:.2f}")

    def purchase_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"Purchased {item['name']} for ${item['price']:.2f}. Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance or item out of stock.")
        else:
            print("Invalid item code.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0

def main():
    vending_machine = VendingMachine()

    while True:
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input("Enter the amount to insert: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item_code = input("Enter the item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            vending_machine.return_change()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()