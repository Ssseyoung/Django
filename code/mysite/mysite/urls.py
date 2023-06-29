"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

'''
    path( 'url', view, name )
    - route(url) : URL 패턴을 정의
    - view : URL 패턴과 일치하는 경우 호출하는 함수
    - name : URL 패턴에 대한 이름 정의
            * 템플릿이나 부에서 해당 URL 을 참조하는 이름으로 사용
            
    incluse('앱.urls')
    - 하위 애플리케이션의 urls.py 파일을 등록하여, 전체 요청 경로를 매핑
    
'''