from django.db import models


# Create your models here.

class Info(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPE = (
        (HARDCOVER, 'HardCover'),
        (PAPERBACK, 'Paperack'),
        (EBOOK, 'E-book')
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPE,default=1)

    def __str__(self):
        return self.title
