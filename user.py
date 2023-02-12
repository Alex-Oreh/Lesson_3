class User:
    first_name = "No name"
    last_name = "No name"
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def seyFirst(self):
        print(self.first_name)  

    def seyLast(self):
        print(self.last_name)    

    def seyFl(self):
        print(self.first_name, self.last_name)


