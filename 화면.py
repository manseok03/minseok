from tkinter import *
import random
import webbrowser

# 각 메뉴에 대한 맛집 사이트 주소 설정
restaurants = {
    '쫄순두부찌개': {'식당': '메밀꽃', '가격': 6500, '홈페이지': 'https://map.naver.com/p/entry/place/1660381645?c=15.00,0,0,0,dh'},
    '닭칼국수': {'식당': '울엄마손칼국시', '가격': 8000, '홈페이지': 'https://map.naver.com/p/entry/place/36364349?c=15.00,0,0,0,dh'},
    '매운돼지갈비찜': {'식당': '손가', '가격': 13000, '홈페이지': 'https://map.naver.com/p/entry/place/1173544014?c=15.00,0,0,0,dh'},
    '제육볶음 또는 돼지불백': {'식당': 'The53', '가격': 11000, '홈페이지': 'https://map.naver.com/p/entry/place/1991840401?c=15.00,0,0,0,dh'},
    '삼겹살': {'식당': '조선부뚜막', '가격': 12900, '홈페이지': 'https://map.naver.com/p/entry/place/1633911574?c=15.00,0,0,0,dh'},
    '크림짬뽕우동': {'식당': '새우식탁', '가격': 9900, '홈페이지': 'https://map.naver.com/p/entry/place/1397101524?c=15.00,0,0,0,dh'},
    '치즈버거': {'식당': '크라이치즈버거', '가격': 7900, '홈페이지': 'https://map.naver.com/p/entry/place/37107229?c=15.00,0,0,0,dh'},
    'BBQ RIB': {'식당': '립플레이', '가격': 33000, '홈페이지': 'https://map.naver.com/p/entry/place/1217395136?c=15.00,0,0,0,dh'},
    '백종원피자': {'식당': '1983 pizza&pub', '가격': 15900, '홈페이지': 'https://map.naver.com/p/entry/place/1432952460?c=15.00,0,0,0,dh'},
    '브런치': {'식당': '꿈꾸는다락방', '가격': 13900, '홈페이지': 'https://map.naver.com/p/entry/place/33646608?c=19.39,0,0,0,dh'},
    '초밥': {'식당': '스시마리오', '가격': 14000, '홈페이지': 'https://map.naver.com/p/entry/place/35455910?c=18.30,0,0,0,dh'},
    '아부라소바': {'식당': '멘야시오리', '가격': 10000, '홈페이지': 'https://map.naver.com/p/entry/place/1557123816?c=18.30,0,0,0,dh'},
    '규카츠': {'식당': '신동랩', '가격': 15000, '홈페이지': 'https://map.naver.com/p/entry/place/1853654246?c=18.30,0,0,0,dh'},
    '마제소바': {'식당': '백소정', '가격': 9900, '홈페이지': 'https://map.naver.com/p/entry/place/1363613159?c=18.30,0,0,0,dh'},
    '라멘': {'식당': '호식당', '가격': 8500, '홈페이지': 'https://map.naver.com/p/entry/place/1366895261?c=18.35,0,0,0,dh'},
    '짜장면': {'식당': '북경', '가격': 6000, '홈페이지': 'https://map.naver.com/p/entry/place/1224193266?c=16.06,0,0,0,dh'},
    '짬뽕': {'식당': '남경', '가격': 7000, '홈페이지': 'https://map.naver.com/p/entry/place/18883568?c=16.06,0,0,0,dh'},
    '마라탕': {'식당': '탕화쿵푸마라탕', '가격': 1600, '홈페이지': 'https://map.naver.com/p/entry/place/1260068936?c=16.06,0,0,0,dh'},
    '마라전골': {'식당': '용용선생', '가격': 22900, '홈페이지': 'https://map.naver.com/p/entry/place/1132784805?c=20.00,0,0,0,dh'},
    '수타짜장면': {'식당': '황금루', '가격': 9500, '홈페이지': 'https://map.naver.com/p/entry/place/1309209880?c=18.30,0,0,0,dh'}
}

# Tkinter GUI 설정
window = Tk()
window.title("가대 오늘 뭐먹지")
window.config(padx=10, pady=10, bg="navy")

# Canvas 설정
canvas = Canvas(window, height=600, width=600, bg="white")
canvas.pack()

# 기본 이미지 설정
img_main = PhotoImage(file="images/001.png")
canvas_img = canvas.create_image(300, 280, image=img_main)

# 버튼 및 이벤트 설정
def rand_choice():
    # GUI 재설정
    recommendation_label.config(text="")
    like_button.config(state=DISABLED)
    dislike_button.config(state=DISABLED)
    recommend_button.config(state=NORMAL)

    show_recommendation()

recommend_button = Button(window, text="뭐먹지?", bg="white", fg="skyblue",
                          font=("나눔바른펜", 25, "bold"), command=rand_choice)
recommend_button.place(x=230, y=650)

def show_recommendation():
    selected_menu = random.choice(list(restaurants.keys()))
    recommendation_label.config(text=f'[{selected_menu}]을(를) 추천드립니다.')
    like_button.config(state=NORMAL)
    dislike_button.config(state=NORMAL)
    recommend_button.config(state=DISABLED)

recommend_button.config(command=show_recommendation)

# 레이블 및 버튼 설정
recommendation_label = Label(window, text="", font=("나눔바른펜", 18), bg="white")
recommendation_label.pack(pady=20)

def like_action():
    selected_menu_text = recommendation_label.cget("text").strip()
    # selected_menu_text에서 메뉴 이름 추출
    selected_menu_start = selected_menu_text.find('[')
    selected_menu_end = selected_menu_text.find(']')
    selected_menu = selected_menu_text[selected_menu_start + 1:selected_menu_end].strip()

    # 선택한 메뉴가 레스토랑 사전에 있는지 확인
    if selected_menu in restaurants:
        # 해당 웹 사이트 가져오기
        restaurant_info = restaurants[selected_menu]
        restaurant_website = restaurant_info.get('홈페이지')

        # 디버깅 정보를 콘솔로 프린트
        print("Selected Menu:", selected_menu)
        print("Restaurant Info:", restaurant_info)
        print("Restaurant Website:", restaurant_website)

        # 웹사이트를 이용할 수 있는지 확인
        if restaurant_website:
            # 새 창에서 연결된 웹 사이트 열기
            webbrowser.open_new(restaurant_website)

    # GUI 재설정
    recommendation_label.config(text="")
    like_button.config(state=DISABLED)
    dislike_button.config(state=DISABLED)
    recommend_button.config(state=NORMAL)


like_button = Button(window, text="좋아요", bg="green", fg="white",
                     font=("나눔바른펜", 18, "bold"), command=like_action, state=DISABLED)
like_button.pack(side=LEFT, padx=10)

dislike_button = Button(window, text="싫어요", bg="red", fg="white",
                        font=("나눔바른펜", 18, "bold"), command=rand_choice, state=DISABLED)
dislike_button.pack(side=RIGHT, padx=10)

window.mainloop()