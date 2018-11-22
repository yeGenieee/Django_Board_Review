from django.shortcuts import render
from django.views import generic

from .models import Post

# Create your views here.

#--- ListView
class PostLV(generic.ListView):
    model = Post # PostLV 의 대상 테이블은 Post 테이블
    template_name = 'blog/post_all.html' # 템플릿 파일 명 지정, 지정하지 않으면 default 템플릿 파일명은 blog/post_list.html이 됨
    context_object_name = 'posts' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명을 posts로 지정함, default 컨텍스트 변수명은 object_list
    paginate_by = 2 # 한 페이지에 보여주는 객체 리스트의 숫자 (페이징 기능)

#--- DetailView
class PostDV(generic.DetailView):
    model = Post

#--- ArchiveIndexView
#--- ArchiveIndexView는 테이블로부터 객체 리스트를 가져와 날짜 필드를 기준으로 최신 객체를 먼저 출력
class PostAV(generic.ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

#--- YearArchiveView
#--- YearArchiveView는 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와, 그 객체들이 속한 월을 리스트로 출력함
class PostYAV(generic.YearArchiveView):
    model = Post
    date_field = 'modify_date' # 기준이 되는 날짜 필드, 변경날짜가 YYYY인 포스트를 검색하여 그 포스트들의 변경 월을 출력함
    make_object_list = True # True 이면 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨줌, default 값은 false


# --- MonthArciveView
# --- MonthArchiveView는 테이블로부터 날짜 필드의 연월 기준으로 객체 리스트를 가져와, 그 리스트를 출력함
class PostMAV(generic.MonthArchiveView):
    model = Post
    date_field = 'modify_date' # 기준이 되는 날짜 필드, 변경날짜 연월을 기준으로 포스트를 검색하여 그 포스트들의 리스트를 출력함

# --- DayArchiveView
# --- DayArchiveView는 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와, 그 객체들의 리스트를 출력함
class PostDAV(generic.DayArchiveView):
    model = Post
    date_field = 'modify_date' # 기준이 되는 날짜 필드, 변경날짜 연월일을 기준으로 포스트를 검색하여 그 포스트들의 리스트를 출력함

# --- TodayArchiveView
# --- TodayArchiveView는 테이블로부터 날짜 필드가 오늘인 객체 리스트를 가져와, 그 객체들이 속한 리스트를 출력함
class PostYAV(generic.TodayArchiveView):
    model = Post
    date_field = 'modify_date' # 기준이 되는 날짜 필드, 변경날짜가 오늘인 포스트를 검색하여 그 포스트들의 리스트를 출력함








