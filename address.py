class Address:

    index = "No name"
    town = "No name"
    street = "No name"
    home = "No name"
    apartment = "No name"
    
    def __init__(self, index, town, street, home, apartment):
        
        self.index = index
        self.town = town
        self.street = street
        self.home = home
        self.apartment = apartment

class Mailing:
    to = Address("index", "town", "street", "home", "apartment" )
    froms = Address("index ", "town", "street", "home", "apartment")
    cost = 1356
    track = "str"
    def __init__(self,  cost, track):
        self.cost = cost
        self.track = track
    def departure(self):
        print("Отправление ", self.track, " из ", self.froms.town,self.froms.street, self.froms.home, self.froms.apartment, 
        " в ", self.to.town,self.to.street, self.to.home, self.to.apartment,".", " Стоимость ", self.cost, " рублей.")
