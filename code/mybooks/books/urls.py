
from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    # /books/       (index.html) - 메인 화면
    path('', views.BooksModelView.as_view(), name='index'),
    
    # /books/book/  (book_list.html) - 도서 목록 화면
    path('book/', views.BookList.as_view(), name='book_list'),
    
    # /books/book/10    (book_detail.html)  - 도서 상세 화면
    path('book/<int:pk>', views.BookDetail.as_view(), name='book_detail'),

]