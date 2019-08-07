products_avl = {}


class Customer(object):
    def __init__(self, name, id, order):
        self.name = name
        self.id = id
        self.order = order
        self.cost=0
        self.num_items=0

    def disp(self):
         print("Name is ", self.name, " Id is ", self.id, "Order is", self.order)


    def cal_cost(self):
        print("-" * 130)
        print("Items", " " * (50 - len("Items")), "Quantity", " " * (50 - len("Quantity")), "Price")
        print("-" * 130)
        for key, val in self.order.items():
            if(key not in products_avl):
                print(key, " "*(50-len(key)), "Not Available", " "*(50-len("Not Available")), "Not Available")
            elif val <= 0:
                print(key, " " * (50 - len(key)), val, " " * (50 - len((str(val)))), "0/less items cannnot be ordered")
            elif(val> products_avl[key][1]):
                print(key, " "*(50-len(key)), val, " "*(50-len((str(val)))), "only "+str(products_avl[key][1])+' item(s) are available')
            else:
                products_avl[key][1] -= val
                cost = products_avl[key][0] * val
                self.cost += products_avl[key][0] * val
                print(key, " "*(50-len(key)), val, " "*(50-len((str(val)))), cost)
                self.num_items += val
        print("-"*130)
        print("Total", " "*(50-len("Total")), self.num_items, " "*(50-len((str(val)))), self.cost)
        print("-" * 130)
        print("Remaining Products", products_avl)




class Admin(object):
    def add_item(self,prod):
        for product, price_qty in prod.items():
            if product in products_avl:
                products_avl.update({product: [price_qty[0], products_avl[product][1]+price_qty[1]]})
                print("Product Updated")
            else:
                products_avl.update({product: [price_qty[0], price_qty[1]]})
                print("Product Added")


reuel = Admin()
reuel.add_item({'Iphone': [1000, 5]})
print(products_avl)

cus1 = Customer("Harish", 1, {"umbrella": 3,"chicken_thali": 12, "Kfc_chicken_bucket": 4, "Vivo": 10, "Mumbai_ticket": 0, "Iphone": 4})
cus1.disp()
cus1.cal_cost()

cus2 = Customer("Harish", 1, {"umbrella": 3,"chicken_thali": 12, "Kfc_chicken_bucket": 4, "Vivo": 10, "Mumbai_ticket": 0, "Iphone": 4})
cus2.disp()
cus2.cal_cost()
