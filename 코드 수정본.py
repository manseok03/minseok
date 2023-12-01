import webbrowser
import time

restaurants = {
    '한식': {
        '쫄순두부찌개': {'식당': '메밀꽃', '가격': 6500, '홈페이지': 'https://map.naver.com/p/entry/place/1660381645?c=15.00,0,0,0,dh'},
        '닭칼국수': {'식당': '울엄마손칼국시', '가격': 8000, '홈페이지': 'https://map.naver.com/p/entry/place/36364349?c=15.00,0,0,0,dh'},
        '매운돼지갈비찜': {'식당': '손가', '가격': 13000, '홈페이지': 'https://map.naver.com/p/entry/place/1173544014?c=15.00,0,0,0,dh'},
        '제육볶음 또는 돼지불백': {'식당': 'The53', '가격': 11000, '홈페이지': 'https://map.naver.com/p/entry/place/1991840401?c=15.00,0,0,0,dh'},
        '삼겹살': {'식당': '조선부뚜막', '가격': 12900, '홈페이지': 'https://map.naver.com/p/entry/place/1633911574?c=15.00,0,0,0,dh'}
    },
    '양식': {
        '크림짬뽕우동': {'식당': '새우식탁', '가격': 9900, '홈페이지': 'https://map.naver.com/p/entry/place/1397101524?c=15.00,0,0,0,dh'},
        '치즈버거': {'식당': '크라이치즈버거', '가격': 7900, '홈페이지': 'https://map.naver.com/p/entry/place/37107229?c=15.00,0,0,0,dh'},
        'BBQ RIB': {'식당': '립플레이', '가격': 33000, '홈페이지': 'https://map.naver.com/p/entry/place/1217395136?c=15.00,0,0,0,dh'},
        '백종원피자': {'식당': '1983 pizza&pub', '가격': 15900, '홈페이지': 'https://map.naver.com/p/entry/place/1432952460?c=15.00,0,0,0,dh'},
        '브런치': {'식당': '꿈꾸는다락방', '가격': 13900, '홈페이지': 'https://map.naver.com/p/entry/place/33646608?c=19.39,0,0,0,dh'}
    },
    '일식': {
        '초밥': {'식당': '스시마리오', '가격': 14000, '홈페이지': 'https://map.naver.com/p/entry/place/35455910?c=18.30,0,0,0,dh'},
        '아부라소바': {'식당': '멘야시오리', '가격': 10000, '홈페이지': 'https://map.naver.com/p/entry/place/1557123816?c=18.30,0,0,0,dh'},
        '규카츠': {'식당': '신동랩', '가격': 15000, '홈페이지': 'https://map.naver.com/p/entry/place/1853654246?c=18.30,0,0,0,dh'},
        '마제소바': {'식당': '백소정', '가격': 9900, '홈페이지': 'https://map.naver.com/p/entry/place/1363613159?c=18.30,0,0,0,dh'},
        '라멘': {'식당': '호식당', '가격': 8500, '홈페이지': 'https://map.naver.com/p/entry/place/1366895261?c=18.35,0,0,0,dh'}
    },
    'Chinese': {
        '짜장면': {'식당': '북경', '가격': 6000, '홈페이지': 'https://map.naver.com/p/entry/place/1224193266?c=16.06,0,0,0,dh'},
        '짬뽕': {'식당': '남경', '가격': 7000, '홈페이지': 'https://map.naver.com/p/entry/place/18883568?c=16.06,0,0,0,dh'},
        '마라탕': {'식당': '탕화쿵푸마라탕', '가격': 1600, '홈페이지': 'https://map.naver.com/p/entry/place/1260068936?c=16.06,0,0,0,dh'},
        '마라전골': {'식당': '용용선생', '가격': 22900, '홈페이지': 'https://map.naver.com/p/entry/place/1132784805?c=20.00,0,0,0,dh'},
        '수타짜장면': {'식당': '황금루', '가격': 9500, '홈페이지': 'https://map.naver.com/p/entry/place/1309209880?c=18.30,0,0,0,dh'}
    }
}

def recommend_restaurant(cuisine):
    print("\n----------------------------------------\n")
    print(f"{cuisine} 요리는 다음 메뉴 중에서 선택 하세요 :")
    for i, menu in enumerate(restaurants[cuisine], start=1):
        print(f"{i}. {menu}")
    
    menu_choice = int(input("선호하는 메뉴의 번호를 선택하세요 : ")) - 1
    
    selected_menu = list(restaurants[cuisine].keys())[menu_choice]
    restaurant_info = restaurants[cuisine][selected_menu]
    
    print("\n----------------------------------------\n")
    print(f"\n추천 식당 : {restaurant_info['식당']}")
    print(f"메뉴 : {selected_menu}")
    print(f"가격 : {restaurant_info['가격']}")
    print(f"홈페이지 : {restaurant_info['홈페이지']}")
    print("\n----------------------------------------\n")
    time.sleep(3)
    webbrowser.open(restaurant_info['홈페이지'])

if __name__ == "__main__":
    print("\n----------------------------------------\n")
    cuisine_choice = input("원하는 음식 종류를 선택하세요 (한식, 양식, 일식, 중식): ")
    
    if cuisine_choice in restaurants:
        recommend_restaurant(cuisine_choice)
    else:
        print("\n----------------------------------------\n")
        print("유효하지 않은 음식 종류입니다 (한식, 양식, 일식, 중식)")