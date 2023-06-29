from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.core.urlresolvers import reverse
from django.urls import reverse

from polls.models import Question, Choice

# Create your views here.
# 설문 목록 뷰
def index(request):
    # return HttpResponse('Hello')
    # 설문 목록을 조회
    question_list = Question.objects.all()     # Question 테이블의 전체 목록
    
    # 투표수 합계
    for q in question_list:
        print( q.choice_set.all() )
        choice_list = q.choice_set.all()
        sum = 0
        for c in choice_list:
            sum = sum + c.votes
            print(c.votes)
        q.sum = sum
        
    context = {'question_list' : question_list}
    return render(request, 'polls/index.html', context)


# 설문 뷰
def detail(request, question_id):
    # question_id 로 데이터 조회
    question = get_object_or_404(Question, pk=question_id)
    
    # 응답할 템플릿을 지정 (detail.html)
    return render(request, 'polls/detail.html', {'question' : question})
    # render()
    # : 요청객체(request)를 지정해주고, 응답할 화면을 지정
    # HttpResponse 객체를 반환
    #   - 클라이언트에게 응답할 내용
    #   - 화면을 렌더링한 결과 포함
    
    
# 설문 선택 등록
def vote(request, question_id):
    # 설문 정보 조회
    question = get_object_or_404(Question, pk=question_id)
    
    # 선택 항목 조회
    choice_id = request.POST['choice']
    # SELECT * FROM choice WHERE choice_id = ?
    selected_choice = question.choice_set.get(pk=choice_id)
    # Choice 테이블에서 데이터를 조회
    # request.POST['choice'] : POST 방식으로 요청된 요청변수 choice
    
    # UPDATE choice SET votes = votes + 1 WHERE choice_id = ?
    selected_choice.votes += 1      # 투표수 1 증가
    selected_choice.save()          # 데이터 저장
    
    # 투표 결과 화면으로 이동
    # polls/10/resuits 경로로, results, args=경로속성값을 반대로 매핑하여 출력
    return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) ) 

    # reverse( '경로 패턴', args=튜플 )
    # - args : 경로에 매핑할 변수를 튜플로 지정


# 설문 결과 뷰
def results(request, question_id):
    # 설문 테이블 조회
    question = get_object_or_404(Question, pk=question_id)   

    # result.html 페이지
    return render(request, 'polls/results.html', { 'question' : question })
    