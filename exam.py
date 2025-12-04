class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, name):
        self.name = name
    
    def place_order(self, item):
        return item

class Driver(Person):
    def __init__(self, name, vehicle):
        self.vehicle = vehicle
        self.name = name

    def deliver(self, order, customer):
        print(f"{self.name} is delivering {order} to {customer.name} using {self.vehicle}")
class Deliveryorder:
    def __init__(self, customer, item , status='preparing'):
        self.customer = customer
        self.item = item
        self.status = status

    def assign_driver(self, driver):
        print(
            '\nOrder Summary:' 
            f'\nItem: {self.item}'
            f'\nCustomer: {self.customer}'
            f'\nStatus: {self.status}'
            f'\ndriver: {driver.name}' 
        )

    def summary(self):
        return (f"Order for {self.item} → {self.status} " )

custome1 = Customer('Alice')
custome2 = Customer('Bob')
driver = Driver('David', 'Motorcycle')
custome1.introduce()
custome2.introduce()
driver.introduce()
delivery1 = Deliveryorder('Alice', 'Labtop')
delivery2 = Deliveryorder('Bob', 'Headphones')
delivery1.assign_driver(driver)
delivery2.assign_driver(driver)
delivery1.status = 'delivered'
delivery2.status = 'delivered'
print()
driver.deliver('Laptop', custome1)
driver.deliver('Headphone', custome2)
print('\nFinal Status:')
print(delivery1.summary())
print(delivery2.summary())