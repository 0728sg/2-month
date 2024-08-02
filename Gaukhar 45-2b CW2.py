#ООП
#Принципы ООП
class Book:
    strr = 400
    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

    def info(self):
        print(self.title, self.author, self.color, self.strr)

    def __len__(self):
        return len(self.title)+len(self.author)+len(self.color)

    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author},\n'
                f' Color: {self.color}, Strr: {self.strr}\n')

War_and_love = Book('war and love', 'Lev Tolstoy', 'yellow')
print(len(War_and_love))
War_and_love.info()

