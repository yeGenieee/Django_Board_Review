from django.db import models
from django.urls import reverse # URL 패턴을 만들어 주는 Django 내장 함수

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        'TITLE',
        max_length=50
    ) # 컬럼에 대한 레이블 : TITLE (레이블 : 폼 화면에 나타나는 문구)
    slug = models.SlugField(
        'SLUG',
        max_length=50,
        unique=True,
        allow_unicode=True,
        help_text='one word for title alias.'
    ) # 제목의 별칭(컨텐츠 고유 주소) , allow_unicode 옵션 : 한글 처리 가능 , help_text = 해당 컬럼을 설명해주는 문구
    description = models.CharField(
        'DESCRIPTION',
        max_length=100,
        blank=True
    ) # 포스트 내용을 한 줄 설명
    content = models.TextField(
        'CONTENT'
    )
    create_date = models.DateTimeField(
        'CREATE_DATE',
        auto_now_add=True
    ) # auto_now_add : 객체가 생성될 때의 시각을 자동으로 기록하게 함
    modify_date = models.DateTimeField(
        'MODIFY_DATE',
        auto_now=True
    ) # auto_now : 객체가 db에 저장될 때의 시각을 자동으로 기록하게 함 (객체가 변경될 때의 시각이 기록됨)


    class Meta:
        verbose_name = 'post' # 테이블의 단수 별칭
        verbose_name_plural = 'posts' # 테이블의 복수 별칭
        db_table='my_post' # 데이터베이스에 저장되는 테이블 이름 지정
        ordering = ('-modify_date',) # 모델 객체의 리스트 출력 시, modify_date 기준으로 내림차순 정렬함

    # 객체의 문자열을 객체.title 로 표현
    def __str__(self):
        return self.title

    # 정의된 객체를 지칭하는 URL을 반환
    def get_absolute_url(self):
        return reverse('blog:post_detail' , args=(self.slug,))

    # modify_date 컬럼 기준으로 이전 포스트를 반환
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # modify_date 컬럼 기준으로 다음 포스트를 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()


