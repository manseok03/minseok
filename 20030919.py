import random
import webbrowser

def recommend_restaurant(cuisine):
    restaurants = {
        '한식': {
            '메뉴': ['비빔밥', '불고기', '김치찌개', '순두부찌개', '삼겹살'],
            '식당': {
                '비빔밥집': {'가격': 10000, '홈페이지': 'http://bibimbab.com'},
                '불고기포차': {'가격': 15000, '홈페이지': 'http://bulgogi-pocha.com'},
                '김치찌개마당': {'가격': 12000, '홈페이지': 'http://kimchijjigae-madang.com'},
                '순두부찌개하우스': {'가격': 11000, '홈페이지': 'http://sundubujjigae-house.com'},
                '삼겹살명가': {'가격': 18000, '홈페이지': 'http://samgyeopsal-myeongga.com'}
            }
        },
        '양식': {
            '메뉴': ['스테이크', '파스타', '샐러드', '피자', '그라탕'],
            '식당': {
                '스테이크하우스': {'가격': 30000, '홈페이지': 'http://steak-house.com'},
                '파스타놀이터': {'가격': 25000, '홈페이지': 'http://pasta-playground.com'},
                '샐러드파라다이스': {'가격': 15000, '홈페이지': 'http://salad-paradise.com'},
                '피자헤븐': {'가격': 20000, '홈페이지': 'http://pizza-heaven.com'},
                '그라탕존': {'가격': 18000, '홈페이지': 'http://gratin-zone.com'}
            }
        },
        '일식': {
            '메뉴': ['초밥', '라멘', '우동', '돈까스', '와규 스테이크'],
            '식당': {
                '초밥마스터': {'가격': 25000, '홈페이지': 'http://sushi-master.com'},
                '라멘도장': {'가격': 12000, '홈페이지': 'http://ramen-dojo.com'},
                '우동탐험대': {'가격': 15000, '홈페이지': 'http://udon-expedition.com'},
                '돈까스왕국': {'가격': 18000, '홈페이지': 'http://tonkatsu-kingdom.com'},
                '와규 스테이크하우스': {'가격': 35000, '홈페이지': 'http://wagyu-steak-house.com'}
            }
        },
        '중식': {
            '메뉴': ['짜장면', '짬뽕', '탕수육', '양장피', '마파두부'],
            '식당': {
                '짜장면궁전': {'가격': 12000, '홈페이지': 'http://jjajangmyeon-palace.com'},
                '짬뽕나라': {'가격': 13000, '홈페이지': 'http://jjamppong-country.com'},
                '탕수육의왕국': {'가격': 15000, '홈페이지': 'http://tangsuyuk-kingdom.com'},
                '양장피프라자': {'가격': 14000, '홈페이지': 'http://yangjangpi-plaza.com'},
                '마파두부마을': {'가격': 13000, '홈페이지': 'http://mapadubu-village.com'}
            }
        }
    }

    if cuisine in restaurants:
        print(f"{cuisine} 음식 메뉴:")
        menu_options = restaurants[cuisine]['메뉴']
        for i, menu in enumerate(menu_options, start=1):
            print(f"{i}. {menu}")

        menu_choice = int(input("선호하는 메뉴의 번호를 선택하세요: "))
        if 1 <= menu_choice <= len(menu_options):
            selected_menu = menu_options[menu_choice - 1]
            selected_restaurant = random.choice(list(restaurants[cuisine]['식당'].keys()))
            print(f"\n추천 식당: {selected_restaurant}")
            print(f"메뉴: {selected_menu}")
            print(f"가격: {restaurants[cuisine]['식당'][selected_restaurant]['가격']} 원")
            print(f"홈페이지: {restaurants[cuisine]['식당'][selected_restaurant]['홈페이지']}")
            webbrowser.open(restaurants[cuisine]['식당'][selected_restaurant]['홈페이지'])
        else:
            print("유효하지 않은 메뉴 번호입니다.")
    else:
        print("유효하지 않은 음식 종류입니다.")

if __name__ == "__main__":
    cuisine_choice = input("한식, 양식, 일식, 중식 중에서 원하는 음식 종류를 선택하세요: ")
    recommend_restaurant(cuisine_choice)