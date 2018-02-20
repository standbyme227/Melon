from django.shortcuts import render, redirect

from .models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(
        request,
        'artist/artist_list.html',
        context,
    )


def artist_add(request):
    # HTML에 Artist클래스가 받을 수 있는 모든 input을 구현
    #   img_profile은 제외
    # method가 POST면 request.POST에서 해당 데이터 처리
    #   새 Artist객체를 만들고 artist_list로 이동
    # method가 GET이면 artist_add.html을 표시

    # ** 생년월일은 YYYY-MM-DD 형식으로 받음
    #      이후 datetime.strptime을 사용해서 date객체로 변환

    # 1. artist_add.html 작성
    # 2. url과 연결, /artist/add/ 에 매핑
    # 3. GET요청시 잘 되는지 확인
    # 4. form method설정 후 POST요청시를 artist_add() view에서 분기
    # 5. POST요청의 값이 request.POST에 잘 오는지 확인
    #       name값만 받아서 name만 갖는 Artist를 먼저 생성
    #       성공 시 나머지 값들을 하나씩 적용해보기
    # 6. request.POST에 담긴 값을 사용해 Artist인스턴스 생성
    # 7. 생성 완료 후 'artist:artist-list' URL name에 해당하는 view로 이동

    # 1. artist/artist_add.html에 Artist_add다 라는 내용만 표시
    #   url, view를 서로 연결
    #   artist/add/ URL사용

    # 2. aritst_add.html에 form을 하나 생성
    #       input은 name이 'name'인 요소 한개만 생성
    #       POST방식으로 전송 후, 전달받은 'name'값을 바로 HttpResponse로 보여주기

    # 3. 전송받은 name을 이용해서 Artist를 생성
    #       이후 'artist:artist-list'로 redirect

    if request.method == 'POST':
        name = request.POST['name']
        Artist.objects.create(
            name=name,
        )
        return redirect('artist:artist-list')
    else:
        return render(request, 'artist/artist_add.html')


def artist_search_from_melon(request):
    """
    Template: artist/artist_search_from_melon.html
        form (input[name=keyword]한개, button한개)
    1. form에 주어진 'keyword'로 멜론 사이트의 아티스트 검색 결과를 크롤링
    2. 크롤링 된 검색결과를 적절히 파싱해서 검색 결과 목록을 생성
        -> list내에 dict들을 만드는 형태
        artist_info_list = [
            {'artist_id': 261143, 'name': '아이유', 'url_img_cover': 'http:...'},
            {'artist_id': 261143, 'name': '아이유', 'url_img_cover': 'http:...'},
            {'artist_id': 261143, 'name': '아이유', 'url_img_cover': 'http:...'},
            {'artist_id': 261143, 'name': '아이유', 'url_img_cover': 'http:...'},
        ]
    3. 해당 결과 목록을 템플릿에 출력
        context = {'artist_info_list': artist_info_list}로 전달 후
        템플릿에서 사용
    :param request:
    :return:
    """
    keyword = request.GET.get('keyword')
    if keyword:
        import requests
        from bs4 import BeautifulSoup
        URL = 'https://www.melon.com/search/artist/index.htm'
        params = {
            'q': keyword,
        }
    return render(request, 'artist/artist_search_from_melon.html')
