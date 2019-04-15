from django.test import TestCase, Client
from .models import Book

# Create your tests here.
class ModelsTestCase(TestCase):
    def setUp(self):
        Book("0001", "Book1", "Writer1", 1991).save()
        Book("0002", "Book2", "Writer2", 1995).save()
        Book("0003", "Book3", "Writer3", 1999).save()
        Book("0004", "Book4", "Writer4", 2005).save()
        Book("0005", "Book5", "Writer5", 2011).save()
    
    def test_books_count(self):
        count = Book.objects.all().count()
        self.assertEqual(count, 5)
    
    def test_books_attributes(self):
        query1 = Book.objects.first().year
        query2 = Book.objects.filter(author="Writer2")[0].isbn
        query3 = Book.objects.filter(title__icontains="oo").count()
        query4 = Book.objects.filter(year__gte = 2018).count()
        query5 = Book.objects.filter(year = 2011).count()
        self.assertEqual(query1, 1991)
        self.assertEqual(query2, "0002")
        self.assertEqual(query3, 5)
        self.assertEqual(query4, 0)
        self.assertEqual(query5, 1)


class WebTestCase(TestCase):
    def test_web_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_book_page(self):
        c =Client()
        response = c.get("/book/0425098087")
        self.assertEqual(response.context["isbn"], "0425098087")
        self.assertEqual(response.status_code, 200)