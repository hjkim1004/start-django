# 1. start-django

## 1.1 project settings
* 프로젝트명 : API
* 하위 폴더 : API(프로젝트 설정파일), crawler(웹에서 정보를 수집), data(학습데이터 정제)
```
1) App 기본 파일
	- admin.py => localhost/admin 사이트에 모델 등록
	- apps.py => app 설정파일
	- models.py => 테이블 정의
	- serializer, views, urls의 viewSet => REST api 사용

```
```
1. API/API/settings.py
	- 앱관리
	- Database 정보: USER and PASSWORD 지정, PORT and HOST default 지정

2. API/data/crawled_data/frames.py
	- crawled_data 폴더 안에 있는 부품 정보들을 frames.py로 받아옴. pandas의 DataFrame 객체로 받을 수 있음.	
	
3. API/data/preprocessing.py 
	- frames의 DataFrame을 받아와서 정제함; NA처리
	
4. API/data/saving.py
	- 정제한 frame을 Model과 맵핑하여 DB에 저장

5. API/crawler
	- 용주오빠가 구현한 크롤러를 받아옴. Model은 정의되어 있으나 수집한 데이터 Mapping은 안된 상태임.
```
link : [leeyoungju's crawler](https://github.com/leeyongjoo/crawler-selenium)

[**API/data/saving.py**] => 문제의 파일 <br>
model에 저장하는것까지 되었으나 에러뜸 <br>
django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.<br>


	$ python manage.py runserver
	http://localhost:8000/admin/

# 2. Django REST framework - Api root
## 2.1 Concat URL
	Concat database api mapping
	http://localhost:8000/concat/
	
## 2.2 data URL
	data for Machine learning
	http://localhost:8000/ml/data/
