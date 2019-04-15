from csv import reader
from main.models import Book

f = open('books.csv', 'r')  #open books.csv and insert each row in the database
table = reader(f, delimiter=',')
count = 0
for row in table:
    if count == 0:
        count += 1
        continue
    isbn = row[0]
    title = row[1]
    author = row[2]
    year = int(row[3])
    book = Book(isbn, title, author, year).save()
    count += 1
f.close()