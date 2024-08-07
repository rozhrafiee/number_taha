import pickle

class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.scores = []

    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def add_score(self, score: int):
        self.scores.append(score)


class Products:
    def __init__(self):
        self.kalaha = []

    def add_product(self, product):
        self.kalaha.append(product)

    def search_by_name(self, name):
        tmp = [i for i in self.kalaha if i.name == name]
        counter = 1
        for i in tmp:
            i: Product
            print(f"{counter}  name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")
            counter += 1

    def return_searched_byname_item(self, name, cnt) -> Product:
        tmp = [i for i in self.kalaha if i.name == name]
        return tmp[cnt - 1]

    def search_by_price(self, min_price, max_price):
        tmp = [i for i in self.kalaha if min_price <= i.price <= max_price]
        counter = 1
        for i in tmp:
            i: Product
            print(f"{counter}  name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")
            counter += 1

    def return_search_byprice_item(self, min_price, max_price, cnt: int) -> Product:
        tmp = [i for i in self.kalaha if min_price <= i.price <= max_price]
        return tmp[cnt - 1]

    def search_by_category(self, category):
        tmp = [i for i in self.kalaha if i.category == category]
        counter = 1
        for i in tmp:
            i: Product
            print(f"{counter}  name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")
            counter += 1

    def return_search_bycategory(self, category, cnt: int) -> Product:
        tmp = [i for i in self.kalaha if i.category == category]
        return tmp[cnt - 1]

    def show_all(self):
        for i in self.kalaha:
            i: Product
            print(f"name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")


class Customer:
    def __init__(self):
        self.sabad_kharid = []
        self.buyed_item = []

    def see_what_in_sabad(self):
        for i in self.sabad_kharid:
            i: Product
            print(f"{i.name}, {i.category}, {i.price}, {i.average_score()}")

    def delete_from_sabad(self):
        counter = 1
        for i in self.sabad_kharid:
            i: Product
            print(f"{counter}  name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")
            counter += 1
        n = int(input("Choose the product that you want to remove: "))
        self.sabad_kharid.pop(n - 1)
        print("Removed successfully")

    def finalize_order(self):
        self.buyed_item.extend(self.sabad_kharid)
        self.sabad_kharid = []

    def show_last_kharid(self):
        for i in self.buyed_item:
            i: Product
            print(f"{i.name}, {i.category}, {i.price}, {i.average_score()}")

    def set_score_for_kharid(self) -> Product:
        counter = 1
        for i in self.buyed_item:
            i: Product
            print(f"{counter}  name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")
            counter += 1
        n = int(input("Please enter the product number you want to enter a score for: "))
        return self.buyed_item[n - 1]

    def show_last_order(self):
        counter = 1
        for i in self.buyed_item:
            i: Product
            print(f"{counter}  name: {i.name}, price: {i.price}, category: {i.category}, average score: {i.average_score()}")
            counter += 1
def save_data():
    with open('data.pkl', 'wb') as file:
        pickle.dump((products, customer), file)
def load_data():
    global products, customer
    with open('data.pkl', 'rb') as file:
        products, customer = pickle.load(file)
load_data()
while True:
    print("""
    Welcome to Pishikala
    1. Search product by name
    2. Search product by price
    3. Search product by category
    4. See what's in the cart
    5. Delete from cart
    6. Finalize order
    7. Show l1ast orders
    8. Set score for product
    9.exit()
    """)

    n = int(input())
    if n == 1:
        tmp = input("Enter product name: ")
        products.search_by_name(tmp)
        print("Which one do you want to add to your cart?")
        tmplo = int(input())
        h = products.return_searched_byname_item(tmp, tmplo)
        customer.sabad_kharid.append(h)
        print("Product added to your cart successfully")
    elif n == 2:
        tmp1, tmp2 = map(int, input("Enter price range (min max): ").split())
        products.search_by_price(tmp1, tmp2)
        print("Which one do you want to add to your cart?")
        tmplo = int(input())
        h = products.return_search_byprice_item(tmp1, tmp2, tmplo)
        customer.sabad_kharid.append(h)
        print("Product added successfully")
    elif n == 3:
        tmp = input("Enter product category: ")
        products.search_by_category(tmp)
        print("Which one do you want to add to your cart?")
        tmplo = int(input())
        h = products.return_search_bycategory(tmp, tmplo)
        customer.sabad_kharid.append(h)
        print("Product added to your cart successfully")
    elif n == 4:
        customer.see_what_in_sabad()
    elif n == 5:
        customer.delete_from_sabad()
    elif n == 6:
        customer.finalize_order()
        print("Thanks for your order. Wish to see you again soon!")
    elif n == 7:
        customer.show_last_order()
    elif n == 8:
        h: Product = customer.set_score_for_kharid()
        score = int(input("Please enter the score: "))
        h.add_score(score)
        print("Score set successfully")
    elif n == 9 : 
        save_data()
        print("bye for now :)))")
        break 