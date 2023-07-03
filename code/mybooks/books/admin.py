from django.contrib import admin
from .models import Book, Author, Publisher

# Register your models here.

# 관리자 페이지에 테이블 등록
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)