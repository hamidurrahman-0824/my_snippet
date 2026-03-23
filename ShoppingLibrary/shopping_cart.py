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