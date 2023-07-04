from typing import Any, Dict
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import *

# Create your views here.
# 게시글 목록
class BoardList(ListView):
    model = Board

# 게시글 상세
class BoardDetail(DetailView):
    model = Board

# 게시글 쓰기
class BoardInsert(TemplateView):
    template_name = 'board/board_insert.html'
    
    def post(self, request):
        # 요청 메시지의 title, content 가져오기
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Board 모델에 데이터 저장
        board = Board(title=title, content=content)
        board.save()
        
        # 게시글 목록으로 이동
        return redirect('/board')

# 게시글 수정
class BoardUpdate(View):
    # get
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        context = {'board' : board}
        return render(request, 'board/board_update.html', context)
 
    # post
    def post(self, request, pk):
        # 요청 메세지의 title, content 가져오기
        title = request.POST.get('title')
        content = request.POST.get('content')
        id = self.request.POST.get('board_id')
        board = get_object_or_404(Board, pk=id)
        
        # 게시글 수정
        board.title = title
        board.content = content
        board.save()
        
        # 게시글 목록으로 이동
        return redirect('/board')
    
# 게시글 삭제
class BoardDelete(View):
    # post
    def post(self, request, pk):
        board = get_object_or_404(Board, pk=pk)

        # 게시글 삭제
        board.delete()
        
        return redirect('/board')
