# start-django
first django project

# 1.  Rest API의 이해와 설계
REST는 웹의 창시자(HTTP) 중의 한 사람인 Roy Fielding의 2000년 논문에 의해서 소개되었음
** 웹의 장점을 최대 활용할 수 있는 네트워크 기반의 아키텍쳐: Representational safe transfer(REST)

(1) REST의 요소
  	리소스, 메소드, 메시지
  “이름이 Terry인 사용자를 생성한다”

  HTTP POST , http://myweb/users/
  {
      “users”:{
	    “name”:”terry”
      }
   }

  생성한다는 의미를 갖는 메서드는 HTTP Post 메서드, 
  생성하고자 하는 대상이 되는 리소스URI로 표현, 
  생성하고자 하는 디테일한 내용을 JSON 문서로 표현

(2)	HTTP 메서드
  REST는 행위에 대한 메서드를 HTTP 메서드를 그대로 사용한다.
  REST에서는 CRUD(Create, Read, Update, Delete)에 해당하는 4가지 메서드만 사용한다.
  메서드	의미	Idempotent
  POST	Create	No
  GET	Select	Yes
  PUT	Update	Yes
  DELETE	Delete	Yes

 
# 2.  Django RESTful API 서버 구현

(1)	REST framework 설치
  $ pip install djangorestframework
  DRF(Django Rest Framework) 라고 부름

(2) Error 사항 정리
  ①	OperationalError
  	에러창
 
  	문제점: DB 변경사항 저장 안됨: Column not found
  	해결책: Serializer의 속성 확인

(3) Django REST Framework 사용법
  ①	Model 생성
    	생성된 모델은 ORM 기능으로 테이블로 변환됨.
        from django.db import models
        class Movie(models.Model):
        title = models.CharField(max_length=30) # 제목
        genre = models.CharField(max_length=15) # 장르
        year = models.IntegerField() # 제작 년도
        def __str__(self): 
        return self.title
    	모델 생성 후 migration, migrate를 해준다
        $ python manage.py makemigrations
        $ python manage.py migrate

  ②	Serializer 생성
    	Serializer란 queryset과 모델 인스턴스와 같은 복잡한 데이터를 json, xml 또는 다른 콘텐츠 유형으로 쉽게 변환 가능 
    	받은 데이터의 유효성을 검사한 다음 복잡한 타입으로 형 변환하도록 serialization을 제공
        from rest_framework import serializers 
        from .models import Movie 
        class MovieSerializer(serializers.ModelSerializer): 
        class Meta: model = Movie # 모델 설정 
        fields = ('id','title','genre','year') # 필드 설정

  ③	views.py 작성
    	DRF는 사람들이 자주 사용하는 view 로직을 그룹화 한 viewset을 제공
    	CRUD를 직접 짜지 않아도 이 기능들을 사용 가능해진다.
        from rest_framework import viewsets 
        from .serializers import MovieSerializer 
        from .models import Movie 
        class MovieViewSet(viewsets.ModelViewSet): 
        queryset = Movie.objects.all() 
        serializer_class = MovieSerializer

  ④	urls.py 작성
    	DRF는 url을 자동으로 맵핑 해주는 router를 제공.
    	앞서 생성한 viewset을 router에 연결하면 자동으로 url 맵팽
        from django.conf.urls import url,include
        from django.contrib import admin
        from rest_framework import routers
        from movies.views import MovieViewSet

        router = routers.DefaultRouter() 
        router.register('movies',MovieViewSet) # prefix = movies , viewset = MovieViewSet

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^',include(router.urls)),
        ]

  ⑤	만든 API로 CRUD 요청
      GET /movies/		영화리스트 조회
      POST /movies/		영화 객체 추가
      GET /movies/{pk}		영화 객체 조회 (한 개)
      PUT / movies/{pk}		영화 객체 수정
      DELETE /movies/{pk}	영화 객체 삭제

  ⑥	Crawler API 생성
 

