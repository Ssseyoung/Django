from django import forms

# Form 양식 만들기
# forms.Form 클래스를 상속받아, Form 양식 클래스 정의
class NameForm(forms.Form):
    your_name = forms.CharField(label="이름", max_length=100)
    your_age = forms.IntegerField(label="나이", max_value=100)
    your_info = forms.CharField(label="자기소개", max_length=200
                              , widget=forms.Textarea
                              , required=False)
    
    # 화면에 렌더링 되는 코드
    '''
        <label for="your_name">이름 : </label>
        <input id="id_your_name" type="text"
               name="your_name" maxlength="100" required
    '''