class book :
    def __init__(self, title, author, price):
        self.title = title
        self.author = author 
        self.price = float(price)

    def display_details(self):
        print("title :", self.title)
        print(f"author : {self.author}")
        print(f"price : {self.price:.2f} $\n")

    def apply_discount (self,percent):
        percent = float(percent)
        self.price -= self.price * (percent/100)

        

title = input ("enter ur 'Title' for first book : ")       
author = input ("enter ur 'Author' for first book : ")
price = input ("enter ur 'Price' for first book : ")
book_1 = book (title,author,price)

title = input ("enter ur 'Title' for second book : ")
author = input ("enter ur 'Author' for second book : ")
price = input ("enter ur 'Price' for second book : " )
book_2 = book (title,author,price)

percent = input ("enter ur (%) of 'Discount' : ")


print("\n\n\nfirst book 'Before' change the price :")
book_1.display_details()

print("first book 'After' change the prices :")
book_1.apply_discount(percent)
book_1.display_details()

print("second book : ")
book_2.display_details()