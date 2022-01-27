class library:
    def __init__(self,name,author,price,publishing_year):
        self.names = name
        self.authors = author
        self.prices = price
        self.publishingy = publishing_year
    def addabook(self):
        print("name: " + self.names)
        print("author: " + self.authors)
        print("price: " + str(self.prices))
        print("publishing year: " + str(self.publishingy))
        print("published " + str(2022-int(self.publishingy)) + " years ago.")
book = library("Falling", "I. Cantfly", 233, 1998)
book.addabook()