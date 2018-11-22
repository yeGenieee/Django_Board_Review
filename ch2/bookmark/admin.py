from django.contrib import admin
from .models import Bookmark

# Register your models here.
# models.py에서 정의한 테이블을 Admin 사이트에 보이도록 등록해야함

# Bookmark 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url') # title과 url을 화면에 출력해라


admin.site.register(Bookmark, BookmarkAdmin) # admin.site.register() 를 사용해 Bookmark와 BookmarkAdmin 클래스를 등록