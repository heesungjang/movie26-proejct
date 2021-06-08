import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mini_project

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/running/current.nhn',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링 시작

d=[
    "https://movie-phinf.pstatic.net/20210512_139/1620799657168vGIqq_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210512_139/1620799657168vGIqq_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210518_265/1621316858792fXwRb_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210421_37/1618971733493B4ykS_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210526_164/1622018439127m1L49_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210126_174/1611638248803840HH_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210517_51/16212169542411PAv1_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210506_101/1620287396480X8Wbi_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210416_118/1618536200110fLn7g_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210520_152/1621485754326FuY4e_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210506_164/1620277609542X5o2T_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210420_259/1618883729532zkiSo_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210604_231/1622788969819Gr0ta_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210518_70/1621322771769VkGHS_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210521_40/1621587883416Xe5Lu_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210325_116/16166363029599OMXS_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210412_292/1618209250689Ocdc6_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210511_239/1620717383918Q0bgO_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210426_268/1619414355444DtDxz_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210528_26/16221908172406snaw_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210510_287/16206206819509mLLg_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210506_173/1620292148907Ao11i_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210603_23/1622704695972mFTzK_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210325_146/1616648170782LcQeF_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210429_261/1619671359642hcXfp_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210421_169/1618982589882LFBPN_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210506_259/1620280381079wzSrW_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210520_89/1621492263055WWAzV_JPEG/movie_image.jpg",
    "https://movie-phinf.pstatic.net/20210406_18/16176849866815lk3B_JPEG/movie_image.jpg"
]

s=[
    "28.51",
    "24.83",
    "19.72",
    "4.79",
    "3.12",
    "2.29",
    "2.23",
    "1.81",
    "1.51",
    "1.18",
    "1.11",
    "0.99",
    "0.69",
    "0.59",
    "0.50",
    "0.50",
    "0.40",
    "0.40",
    "0.40",
    "0.40",
    "0.30",
    "0.30",
    "0.30",
    "0.30",
    "0.30",
    "0.30",
    "0.30",
]

v=[
            "https://youtu.be/yfSMTFzw-Kw",
            "https://youtu.be/-ph-C38VJkI",
            "https://youtu.be/L9Y-hn2COm0",
            "https://youtu.be/KbFhzL1b8iQ",
            "https://youtu.be/VQGCKyvzIM4",
            "https://youtu.be/4gxMoIF1f8c",
            "https://youtu.be/GIucaWI15G4",
            "https://youtu.be/2oGNXxeoZbE",
            "https://youtu.be/kymRai9G4rY",
            "https://youtu.be/BuSN_zYbfT4",
            "https://youtu.be/SYiEc5GO0-8",
            "https://youtu.be/itmdHqYW84Y",
            "https://youtu.be/IEKt_GtoAz0",
            "https://youtu.be/ILCB_f0IIyI",
            "https://youtu.be/tfmRVC_GADw",
            "https://youtu.be/RIi45-Aytt8",
            "https://youtu.be/dxpLWlQsXH4",
            "https://youtu.be/_tpCtzSPmO0",
            "https://youtu.be/_wXverrh8yg",
            "https://youtu.be/13fjHivAA-8",
            "https://youtu.be/EU6vg5QMYbg",
            "https://youtu.be/BEnu5wZnzIw",
            "https://youtu.be/0pqVUiDVpjw",
            "https://youtu.be/Kujn4nxrFBs",
            "https://youtu.be/jhu20svTpO0",
            "https://youtu.be/l6CZc3y0FsA",
            "https://youtu.be/w_ALTnlrv3k"
        ]


ul = soup.select("#content > div.article > div:nth-child(1) > div.lst_wrap > ul")

for li in ul:
    items = li.select("li")
    movie_id = 1
    img_id = 1
    booking_id = 0
    video_id = 0
    for item in items[:27]:
        #제목
        title = item.select_one("dl > dt > a").text.strip()
        img = d[img_id]
        booking = s[booking_id]
        video = v[video_id]
        #장르
        genres = item.select("dl > dd:nth-child(3) > dl > dd:nth-child(2)")
        movie_genre = ""
        for genre in genres:
            movie_genre = genre.select_one("span.link_txt > a")
            if movie_genre:
                movie_genre = movie_genre.text
            else:
                movie_genre = "독립"

        #상영일
        
        info = item.select_one("dl > dd:nth-child(3) > dl > dd").text.strip()
        info_list = list(info.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "").replace("|", ""))
        parsed_date = "".join(info_list[-12:])

        # 평점
        rate = item.select_one("dl > dd.star > dl.info_star > dd > div > a > span.num").text
        
        #감독
        producer = item.select_one("dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a").text

        
        doc = {"title": title, "genre": movie_genre, "rate": rate, "producer": producer, "date": parsed_date, "movie_id": movie_id, "image": img, "booking": booking, "video":video}

        movie_id+= 1
        img_id+=1
        booking_id+=1
        video_id+=1

        db.movie_details.insert_one(doc)



        