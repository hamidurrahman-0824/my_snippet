"""Encapsulation (OOP design)
Correct cart management
Handling invalid inputs
Accurate price calculation
User-friendly output"""
class ShoppingCart:
    def __init__(self,**itmqt):
        
        self.items = {'Apple':20,'Pen':5, 'Fish':50,'Rice':10,'Petrol':40}
        self.itmqt=itmqt
        self.total= 0#self.items[item]*quantity
        self.demand = []
        self.cart = []
    def add(self,item,qt):
        if item in self.items:
            self.total += qt*self.items[item]
            self.cart.append(item)
        else:
            print(f"{item} is currently not availble, contact next week.")
            self.demand.append(item)
    def discard(self,item,qt):
        if item in self.cart:
            self.total -= qt*self.items[item]
            self.cart.remove(item)
        else:
            print(f"Haven't bought it yet.")
    def seeList(self):
        return list(self.cart)
    def total(self):
        for k,v in self.itmqt.items():
            if k in self.items:
                self.total += v*self.itmqt[k]
                self.cart.append(k)
            else:
                print(f"Not available item{k}")
        return self.total
buyer = ShoppingCart(Apples=5,Fish=50,Pen=21,nice=1)

print(buyer.seeList())
# print(buyer1.total)
class ShoppingCart:
    def __init__(self):
        self.items = {'Apple':20,'Pen':5,'Rice':10,'Fish':40,'Petrol':50}    
        self.cart = {}
    def add(self,item,qt):
        if item in self.items:
            if item not in self.cart:
                self.cart[item] = qt
            else:
                self.cart[item] += qt
        else:
            print(f"{item} is currently not available,contact next week.")
    def discard(self,item,qt):
        if item in self.cart:
            if self.cart[item]>qt:
                self.cart[item] -=qt
            else:
                del self.cart[item]
        else:
            print(f"Haven't bought it yet.")
    def seeList(self):
        return list(self.cart.keys())
    def calculate_total(self):
        return sum([self.items[item]*qty for item, qty in self.cart.items()])
buyer = ShoppingCart()
buyer.add('Apple',5)
print(buyer.seeList())
print('total price: ', buyer.calculate_total())    
class ShoppingCart:
    def __init__(self):
        # Store item prices
        self.items = {
            'Apple': 20,
            'Pen': 5,
            'Rice': 10,
            'Fish': 40,
            'Petrol': 50
        }
        
        # Cart dictionary -> {item: quantity}
        self.cart = {}

    def add(self, item, qty):
        """Add item to cart"""
        if item not in self.items:
            print(f"{item} is not available.")
            return
        
        if qty <= 0:
            print("Quantity must be positive.")
            return

        self.cart[item] = self.cart.get(item, 0) + qty
        print(f"{qty} {item}(s) added to cart.")

    def discard(self, item, qty):
        """Remove item quantity from cart"""
        if item not in self.cart:
            print(f"{item} not in cart.")
            return
        
        if qty >= self.cart[item]:
            del self.cart[item]
            print(f"{item} removed from cart.")
        else:
            self.cart[item] -= qty
            print(f"{qty} {item}(s) removed.")

    def seeList(self):
        """Display cart items"""
        if not self.cart:
            print("Cart is empty.")
            return
        
        print("Items in cart:")
        for item, qty in self.cart.items():
            print(f"{item} : {qty}")

    def calculate_total(self):
        """Calculate total price"""
        total = sum(self.items[item] * qty for item, qty in self.cart.items())
        return total

    def show_bill(self):
        """Print full bill"""
        if not self.cart:
            print("Cart is empty.")
            return

        print("\n------ BILL ------")
        total = 0

        for item, qty in self.cart.items():
            price = self.items[item] * qty
            total += price
            print(f"{item} ({qty}) = {price}")

        print("------------------")
        print("Total:", total)