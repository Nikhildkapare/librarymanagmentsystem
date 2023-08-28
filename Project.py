#Librery Management System

class Library:

    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def displaybooks(self):
        print(f"WE have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)


    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can tae the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnbook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    Nikhil=Library(['Python','Rich dad poor dad','Harry Potter','C++ Basics','CLRS'],"Dnyandeep")

    while(True):
        print(f"Welcome to the {Nikhil.name} library. Enter your choice to continue.")
        print('1. Display Books')
        print('2. Lend a book')
        print('3. add a book')
        print('4. Return a book')

        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print('Please enter valid option')
            continue

        else:
            user_choice=int(user_choice)
        if user_choice==1:
            Nikhil.displaybooks()

        elif user_choice==2:
            book=input('Enter the name of the book you want to lend:')
            user=input('Enter your name')
            Nikhil.lendbook(user,book)

        elif user_choice==3:
            book=input('Enter the name of the book you want to add:')
            Nikhil.addbook(book)

        elif user_choice==4:
            book = input('Enter the name of the book you want to return:')
            Nikhil.returnbook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 =''
        while(user_choice2!='c' and user_choice2!='q'):
            user_choice2 = input()
            if user_choice2=='q':
                exit()
            if user_choice2=='c':
                continue