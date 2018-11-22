from django.shortcuts import render
from django.views import generic

from .models import Post

# Create your views here.

#--- ListView
class PostLV(generic.ListView):
    model = Post # PostLV 의 대상 테이블은 Post 테이블
    template_name = 'blog/post_all.html' # 템플릿 파일 명 지정, 지정하지 않으면 default 템플릿 파일명은 blog/post_list.html이 됨
    context_object_name = 'posts' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명을 posts로 지정함, default 컨텍스트 변수명은 object_list
    paginate_by = 2 #