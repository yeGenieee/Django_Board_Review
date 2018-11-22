from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date') # Post 객체 보여줄 때 title과 modify_date를 화면에 출력해라
    list_filter = ('modify_date',) # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    search_fields = ('title', 'content') # 검색 박스를 표시하고, 입력된 단어는 title과 content 컬럼에서 검색하도록 함
    prepopulated_fields = { 'slug' : ('title',)} # slug 필드는 title 필드를 사용해 미리 채워지도록 함


admin.site.register(Post, PostAdmin)
