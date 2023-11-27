import random
import webbrowser

# 각 음식 카테고리에 대한 리스트 정의
menu_categories = {
    '한식': ['국밥', '찌개', '고기', '제육볶음', '칼국수'],
    '양식': ['파스타', '피자', '햄버거'],
    '중식': ['짜장면', '짬뽕', '마라탕'],
    '일식': ['라멘', '돈부리', '돈카츠'],
    '분식': ['김밥', '떡볶이', '유부초밥']
}

# 각 메뉴에 대한 맛집 사이트 주소 설정
restaurant_websites = {
    '국밥': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EA%B5%AD%EB%B0%A5?c=15.00,0,0,0,dh',
    '찌개': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EC%B0%8C%EA%B0%9C?c=15.00,0,0,0,dh',
    '고기': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EA%B3%A0%EA%B8%B0?c=15.00,0,0,0,dh',
    '제육볶음': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EC%A0%9C%EC%9C%A1%EB%B3%B6%EC%9D%8C?c=14.00,0,0,0,dh',
    '칼국수': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EC%B9%BC%EA%B5%AD%EC%88%98?c=15.00,0,0,0,dh',
    '파스타': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%ED%8C%8C%EC%8A%A4%ED%83%80?c=15.00,0,0,0,dh',
    '피자': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%ED%94%BC%EC%9E%90?c=15.00,0,0,0,dh',
    '햄버거': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%ED%96%84%EB%B2%84%EA%B1%B0?c=13.00,0,0,0,dh',
    '짜장면': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EC%A7%9C%EC%9E%A5%EB%A9%B4?c=15.00,0,0,0,dh',
    '짬뽕': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EC%A7%AC%EB%BD%95?c=15.00,0,0,0,dh',
    '마라탕': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EB%A7%88%EB%9D%BC%ED%83%95?c=13.00,0,0,0,dh',
    '라멘': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EB%9D%BC%EB%A9%98?c=13.00,0,0,0,dh',
    '돈부리': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EB%8F%88%EB%B6%80%EB%A6%AC?c=15.00,0,0,0,dh',
    '돈카츠': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EB%8F%88%EC%B9%B4%EC%B8%A0?c=15.00,0,0,0,dh',
    '김밥': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EA%B9%80%EB%B0%A5?c=15.00,0,0,0,dh',
    '떡볶이': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EB%96%A1%EB%B3%B6%EC%9D%B4?c=15.00,0,0,0,dh',
    '유부초밥': 'https://map.naver.com/p/search/%EC%97%AD%EA%B3%A1%20%EC%9C%A0%EB%B6%80%EC%B4%88%EB%B0%A5?c=13.00,0,0,0,dh'
}

while True:
    # 랜덤으로 음식 카테고리 선택
    selected_category = random.choice(list(menu_categories.keys()))

    # 사용자에게 선택 결과를 보여줌
    user_response_category = input(f'랜덤으로 선택된 [{selected_category}] 중에서 메뉴를 추천드릴까요? (네/아니요) ')

    # 사용자가 확인하면 해당 카테고리의 구체적인 메뉴를 추천
    if user_response_category.lower() == '네':
        selected_menu = random.choice(menu_categories[selected_category])
        print(f'[{selected_category}] 중에서 [{selected_menu}]을(를) 추천드립니다.')

        # 사용자에게 맛집 정보를 확인하려면 주소로 이동 여부를 물어봄
        user_response_menu = input(f'[{selected_menu}]의 맛집 정보를 확인하시겠습니까? (네/아니요) ')

        # 사용자가 확인하면 해당 메뉴의 맛집 사이트로 이동
        if user_response_menu.lower() == '네':
            # 각 메뉴에 대한 맛집 사이트 주소를 설정
            restaurant_website = restaurant_websites.get(selected_menu, 'https://www.example.com')
            print(f'맛집 정보를 확인하려면 {restaurant_website}로 이동합니다...')
            webbrowser.open(restaurant_website)
        else:
            print('다음에 또 도움이 필요하시면 말씀해주세요.')
    elif user_response_category.lower() == '아니요':
        print('다시 음식 카테고리를 선택합니다.')
    else:
        print('잘못된 입력입니다. "네" 또는 "아니요"로 입력해주세요.')