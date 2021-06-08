import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mini_project

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/running/current.nhn',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링 시작

ul = soup.select("#content > div.article > div:nth-child(1) > div.lst_wrap > ul")

for li in ul:
    items = li.select("li")
    movie_id = 1
    for item in items[:27]:
        #제목
        title = item.select_one("dl > dt > a").text.strip()

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

        
        doc = {"title": title, "genre": movie_genre, "rate": rate, "producer": producer, "date": parsed_date, "movie_id": movie_id}

        movie_id+= 1

        db.movie_details.insert_one(doc)
    
        

						












# num = 1
# for ls in ul:
#     item = ls.select_one(f"li:nth-child({num}) > dl > dt > a")
#     print(item.text)
#     num +=1
    

    

    
    



    
        
          
           
          
      
        

        
