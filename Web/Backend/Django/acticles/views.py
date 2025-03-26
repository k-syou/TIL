from django.shortcuts import render

# Create your views here.
def index(request):
    # 메인 페이지가 담겨있는 응답 객체를 반환

    # render(request, "{template path}")
    return render(request, 'articles/index.html')
