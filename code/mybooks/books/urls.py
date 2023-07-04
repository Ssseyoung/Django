
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

    # /books/author/    (author_list.html) - 저자 목록 화면
    path('author/', views.AuthorList.as_view(), name='author_list'),
    
    # /books/author/10      (author_detail.html) - 저자 상세 화면
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author_detail'),
    
    # /books/publisher/     (publisher_list.html) - 출판사 목록 화면
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),

    # /books/publisher/10       (publisher_detail.html) - 출판사 상세 화면
    path('publisher<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),

]