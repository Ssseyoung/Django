
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ""(루트) 경로 요청, views.py 파일의 index 함수 호출
    # name="경로 이름"
    # http://localhost:8000/polls  -->  index()
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),            # /polls/10
    path("<int:question_id>/vote", views.vote, name="vote"),            # /polls/10/vote
    path("<int:question_id>/results", views.results, name="results"),   # /polls/10/vote/results

]

'''
    path("<int:question_id>/", ...)
    - polls/10
    : 10 이라는 데이터를 요청변수 int 타입의 question_id 로 연결해준다.
'''
