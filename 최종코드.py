import random
import time
import webbrowser

def determine_menu(user_choice):
    
    # '랜덤'을 선택했을 때의 메뉴 추천 코드
    
    if user_choice == '랜덤' :
        menu_categories = {
            '한식': ['국밥', '찌개', '고기', '제육볶음', '칼국수'],
            '양식': ['파스타', '피자', '햄버거'],
            '중식': ['짜장면', '짬뽕', '마라탕'],
            '일식': ['라멘', '돈부리', '돈카츠'],
            '분식': ['김밥', '떡볶이', '유부초밥']
            }
        
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
            selected_category = random.choice(list(menu_categories.keys()))
            print("\n----------------------------------------\n")
            user_response_category = input(f'랜덤으로 선택된 [{selected_category}] 중에서 메뉴를 추천드릴까요? (네/아니요) ')
            
            if user_response_category.lower() == '네':
                selected_menu = random.choice(menu_categories[selected_category])
                print("\n----------------------------------------\n")
                print(f'[{selected_category}] 중에서 [{selected_menu}]을(를) 추천드립니다.')
                print("\n----------------------------------------\n")
                user_response_menu = input(f'[{selected_menu}]의 맛집 정보를 확인하시겠습니까? (네/아니요) ')
                
                if user_response_menu.lower() == '네': 
                    restaurant_website = restaurant_websites.get(selected_menu, 'https://www.example.com')
                    print("\n----------------------------------------\n")
                    print(f'맛집 정보를 확인하려면 {restaurant_website}로 이동합니다...')
                    time.sleep(3)
                    webbrowser.open(restaurant_website)
                    return
                
                else:
                    print("\n----------------------------------------\n")
                    print('다음에 또 도움이 필요하시면 말씀해주세요.')
                    print("\n----------------------------------------\n")
                    return
                    
            elif user_response_category.lower() == '아니요':
                print("\n----------------------------------------\n")
                print('다음에 또 도움이 필요하시면 말씀해주세요.')
                return
                
            else:
                print("\n----------------------------------------\n")
                print('잘못된 입력입니다. 코드를 다시 실행시켜주세요.')
                return
    
    # '선택'을 선택했을 때의 메뉴 선택 코드
    
    elif user_choice == '선택' :
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
                return
                    
    else :
        print("\n----------------------------------------\n")
        print("'랜덤' or '선택' 중 하나를 골라주세요")
        return
    

print("랜덤 : 컴퓨터의 메뉴 추천")
print("선택 : 사용자의 메뉴 선택")
print("'랜덤' or '선택'을 적어주세요")
chnum = input()

determine_menu(chnum)