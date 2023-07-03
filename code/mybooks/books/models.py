from django.db import models

# Create your models here.
# Book 테이블
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')  # M:N 관계
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()
    # models.ManyToManyFie('참조테이블')
    # - 다대다(M:N)의 관계로 필드를 설정
    
    # models.ForeignKey('참조테이블', 옵션)
    # - Book(N) : Publisher(1) 관계로 필드를 설정
    
    def __str__(self):
        return self.title
    
    
# Author 테이블
class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)   # 인사말
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    
# Publisher 테이블
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name