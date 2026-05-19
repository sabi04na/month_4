from django.db import models

class Blog(models.Model):
    titel= models.CharField(max_length=50, verbose_name='yапишите название блга')
    description = models.TextField(verbose_name='напишите статью', blank=True)
    image = models.ImageField(upload_to='blog/',verbose_name='загрузите фото')
    blog_file = models.FileField(upload_to='blog/',verbose_name='загрузите пдф файл')
    TYPE_BLOG =(
        ('програмирование','pпрограмирование'),
        ('бизнес','бизнес'),
        ('медецина','медецина')
    )
    quantity = models.PositiveIntegerField(verbose_name='укажите количество скраниц', default=20, null=True)
    type_blog = models.CharField(max_length=100, choices=TYPE_BLOG, default='програмирование')
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.title
