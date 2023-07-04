from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django. views.generic import ListView, DetailView

from .models import Book, Author, Publisher

# Create your views here.
# 장고의 제네릭 뷰
'''
    TemplateView    : 템플릿(화면)을 지정하고 렌더링
    ListView        : 조건에 맞는 여러 개의 객체를 보여줌
                    * ListView 를 상속받으면, model 로 지정한 객체를 
                      리스트로 구성하여 context 변수로 템플릿에 넘겨줌
    DetailView      : 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 넘겨줌
'''

class BooksModelView(TemplateView):
    # 템플릿 지정
    template_name = 'books/index.html'

    # 컨텍스트 지정
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        # context['model_list'] = ['Book']
        return context
    
# 도서 목록
class BookList(ListView):
    model = Book

    
# 도서 상세
class BookDetail(DetailView):
    model = Book
    
# 저자 목록
class AuthorList(ListView):
    model = Author

# 저자 상세
class AuthorDetail(DetailView):
    model = Author

# 출판사 목록
class PublisherList(ListView):
    model = Publisher

# 출판사 상세
class PublisherDetail(DetailView):
    model = Publisher