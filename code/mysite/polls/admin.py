from django.contrib import admin
from .models import *       # models 모듈

# Register your models here.
# 관리자 페이지 모델 선정

# Question 테이블에 종속된 Choice 데이터 같이 보기
# class ChoiceInline(admin.StackedInline):     # 늘려놓는 형식으로 보기
class ChoiceInline(admin.TabularInline):       # 테이블 형식으로 보기
    model = Choice                             # 테이블 지정
    extra = 1                                  # 기존 데이터 외의 추가 항목 개수

# 필드 순서 변경
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']   # 순서 변경
    # 필드를 분리하여 출력
    fieldsets = [
        ('설문 제목', {'fields' : ['question_text']}),
        # 필드 접기
        ('등록 일자', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    
    # Choice 테이블 포함하기
    inlines = [ChoiceInline]        # 종속된 Choice 테이블 같이 보기

    # 리스트 출력 항목 지정
    list_display = ('question_text', 'pub_date')
    
    # 리스트 필터 추가 (날짜 순)
    list_filter = ['pub_date']
    
    # 검색창 추가
    search_fields = ['question_text']


# 관리자 페이지에서 polls 애플리케이션을 관리하도록 등록
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
