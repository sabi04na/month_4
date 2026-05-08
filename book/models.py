from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=255, verbose_name="Название")
   
    author = models.CharField(max_length=255, verbose_name="Автор")
    
    description = models.TextField(verbose_name="Описание")
   
    image = models.ImageField(upload_to="books/", verbose_name="Обложка")
    
    book_file = models.FileField(upload_to="book_files/", verbose_name="Файл книги")
    
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    
    year = models.IntegerField(verbose_name="Год издания")
    
    publisher = models.CharField(max_length=255, verbose_name="Издательство")
    
    pages = models.IntegerField(verbose_name="Количество страниц")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

