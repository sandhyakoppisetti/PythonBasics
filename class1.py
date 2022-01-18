from typing_extensions import Self


class Mobile:
    def __init__(self,brand,battery,ram,camera,price):
        self.brand=brand
        self.battery=battery
        self.ram=ram
        self.camera=camera
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Battery:",self.battery)
        print("Ram:",self.ram)
        print("Camera:",self.camera)
        print("price:",self.price)


obj=Mobile("Iphone","700mh","1tb","14pixel","13000")
obj.display(Self)
