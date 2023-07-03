from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

# Create your views here.
def index(request):
    
    # POST
    if request.method == 'POST':
        
        form = NameForm(request.POST)   # 요청 데이터 포함한 객체
        
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사 로직
            pass
            # 결과화면으로 이동
            return HttpResponseRedirect('/myapp/results')
            
    # GET
    else:
        form = NameForm()       # NameForm 객체 생성
    
    context = {'form' : form}
    
    return render(request, 'myapp/index.html', context)


# 결과 화면
def results(request):
    
    return render(request, 'myapp/results.html')
