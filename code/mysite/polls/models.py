from django.db import models

# Create your models here.
# 데이터 모델을 정의
# class 로 정의

# 설문
# 질문 제목, 작성 일자
class Question(models.Model):
    
    def __str__(self):
        return self.question_text       # 관리자 페이지 목록에 출력될 이름
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    sum = models.IntegerField(default=0)
    
    
# 답변
# 답변 내용, 투표 수
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey( 참조할 테이블, on_delete=옵션 )
    # - Question 테이블의 데이터 삭제 시, 존속된 Choice 테이블에 데이터도 같이 삭제
    