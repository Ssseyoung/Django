# URL 과 뷰 매핑

패턴                      뷰 이름        처리 로직
/polls                    index()        index.html 템플릿 응답      (설문 목록)
/polls/10                 detail()       detail.html 템플릿 응답     (설문)
/polls/10/vote            vote()         설문-답변 정보를 등록처리
/polls/10/vote/result     result()       result.html 템플릿 응답     (설문 결과)