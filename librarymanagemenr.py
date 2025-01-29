class library:
    def __init__(self,books=None,no_of_books=0):
        if books is None:
          books = []  
        self.no_of_books = no_of_books
        self.books=books

    def addbooks(self):
        while True:
            book = input("enter the books name u want to enter")
            if book.lower() == "done":
               break
            self.books.append(book) 
           

        self.no_of_books = len(self.books)
        print("The total books entered are:", self.books)
        print("Total number of books:", self.no_of_books)


newbook = library()
newbook.addbooks()