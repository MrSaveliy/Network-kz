import time
from bs4 import BeautifulSoup
import requests

def get_data(url: str, person_id: int, assets_id: int):
    cookies = {
        '_ym_uid': '1692780624967630624',
        '_ym_d': '1692780624',
        'megaserver2_session': 'eyJpdiI6IjdVbkp5R0x3TW9GK012OFZXZGtBMHc9PSIsInZhbHVlIjoiNVRjUjNvNHRpbXFjVE9xU2RUZnVjSU1yT3NBeXAyVTNPTVFCVEwzZXd3NmtGa2dWU0JpQU9GUUJxNzRVUHdGWVViNXo2TzBLeXk4bVRncWx0b3lQZDRNRnhkeXJNdXl4bFQ3K2FnQ3ZLNlhKOFJ0YWpOUTBqZFAxN1B1NGFKVk4iLCJtYWMiOiJlZDhmNjg4YmE3OWE4MTZkYWFlNzg2ZmUyZTFmY2I1M2VmYTdmYmQ5NjIxMmEwNWFhOWE0MWEyMWU0NWMyMDcyIn0%3D',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        '_gid': 'GA1.2.997437757.1693397746',
        'srv7_session': 'eyJpdiI6ImloS05ZSXlhK1ptdDV2b2FFV1BjNWc9PSIsInZhbHVlIjoiUXdBZlJcL3g5RXJUOEpwTGVtYVF5emdoRVZyNTlmVVIzekNNbzJpNkVsRXpmSXcwMElvV1ZXREZ2YUtKdXVOR3k3REhGcUxrNDI1QTJ2WjhUSlVUcEFRckJLQ3RJdU9ucGlpdTFZUUtNSncxWU1WZkM5YjJ2ZGhwbTg0ajUwSDVrIiwibWFjIjoiMjRiZDI0OTYxZTgzYmI5ZTExNzQ5NDNmNzA2NTk5MWQ2YzBlMGE4YzhiOGZkNzgyZjdiY2UzODA4MjgxZDhiYiJ9',
        'XSRF-TOKEN': 'eyJpdiI6IjY3bEFtMm5QYnhOQ2RCMUhNRFJBRkE9PSIsInZhbHVlIjoiaUw3S3Nnc2NKXC9BalVuUW9wdHlGajVUQU1HNnFVTUhyaHV1cTBMZmgxWFo4QlpYT3FpRFNXcjVvTXhiaHVBQ0VyRk9LVVVQNlwvRzg3RE1ncm5YWnBqWSttbnZDZXYzWFlBRlNmWk5TSERLeGNsOGltVUoxXC9GV0wxWmo1d3NvRGQiLCJtYWMiOiIyZmY0NmYxYjRmYmJhNjMzNTRjNDdmMTRmY2ZkZTYwY2Q5YjQzMWU0Mjc0YWIzZWMxNTRkN2NlOGMzZWI3ZjNmIn0%3D',
        'megaserver1_session': 'eyJpdiI6IkZJTlMwKzZZa1hOU0Q0ZExKY1daU2c9PSIsInZhbHVlIjoib0pGOWx4cTAwbStNWVBZMWNQUVwvM3ZuYXlLdmZwc3JPM0ZyazFqakpzSVdpR2xYWWw5TDFXYitTNTdMeVMxbldOUEFGd1BNZjI5Uk4yMFFjejBEWGxGRlJSRzRHVHQ4S3RWcmY4TXFFODhyNnA0MGFzSXd6WUxDcXgxOHQ1TDRxIiwibWFjIjoiOTI2MDJiMTYwMDJiYTUyNTQxYzE1ZmExYWUyNTkwMmZiMWQ4MWNkYTZkZjllYTI1Y2RjZjgxZWMzNGZhNGVmNiJ9',
        '_dc_gtm_UA-19570424-1': '1',
        '_gat_UA-19570424-1': '1',
        '_ga_EKJ8741MGP': 'GS1.1.1693397746.3.1.1693397954.54.0.0',
        '_ga': 'GA1.1.292257908.1692780627',
    }

    headers = {
        'authority': 'tengrinews.kz',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_ym_uid=1692780624967630624; _ym_d=1692780624; megaserver2_session=eyJpdiI6IjdVbkp5R0x3TW9GK012OFZXZGtBMHc9PSIsInZhbHVlIjoiNVRjUjNvNHRpbXFjVE9xU2RUZnVjSU1yT3NBeXAyVTNPTVFCVEwzZXd3NmtGa2dWU0JpQU9GUUJxNzRVUHdGWVViNXo2TzBLeXk4bVRncWx0b3lQZDRNRnhkeXJNdXl4bFQ3K2FnQ3ZLNlhKOFJ0YWpOUTBqZFAxN1B1NGFKVk4iLCJtYWMiOiJlZDhmNjg4YmE3OWE4MTZkYWFlNzg2ZmUyZTFmY2I1M2VmYTdmYmQ5NjIxMmEwNWFhOWE0MWEyMWU0NWMyMDcyIn0%3D; _ym_isad=1; _ym_visorc=b; _gid=GA1.2.997437757.1693397746; srv7_session=eyJpdiI6ImloS05ZSXlhK1ptdDV2b2FFV1BjNWc9PSIsInZhbHVlIjoiUXdBZlJcL3g5RXJUOEpwTGVtYVF5emdoRVZyNTlmVVIzekNNbzJpNkVsRXpmSXcwMElvV1ZXREZ2YUtKdXVOR3k3REhGcUxrNDI1QTJ2WjhUSlVUcEFRckJLQ3RJdU9ucGlpdTFZUUtNSncxWU1WZkM5YjJ2ZGhwbTg0ajUwSDVrIiwibWFjIjoiMjRiZDI0OTYxZTgzYmI5ZTExNzQ5NDNmNzA2NTk5MWQ2YzBlMGE4YzhiOGZkNzgyZjdiY2UzODA4MjgxZDhiYiJ9; XSRF-TOKEN=eyJpdiI6IjY3bEFtMm5QYnhOQ2RCMUhNRFJBRkE9PSIsInZhbHVlIjoiaUw3S3Nnc2NKXC9BalVuUW9wdHlGajVUQU1HNnFVTUhyaHV1cTBMZmgxWFo4QlpYT3FpRFNXcjVvTXhiaHVBQ0VyRk9LVVVQNlwvRzg3RE1ncm5YWnBqWSttbnZDZXYzWFlBRlNmWk5TSERLeGNsOGltVUoxXC9GV0wxWmo1d3NvRGQiLCJtYWMiOiIyZmY0NmYxYjRmYmJhNjMzNTRjNDdmMTRmY2ZkZTYwY2Q5YjQzMWU0Mjc0YWIzZWMxNTRkN2NlOGMzZWI3ZjNmIn0%3D; megaserver1_session=eyJpdiI6IkZJTlMwKzZZa1hOU0Q0ZExKY1daU2c9PSIsInZhbHVlIjoib0pGOWx4cTAwbStNWVBZMWNQUVwvM3ZuYXlLdmZwc3JPM0ZyazFqakpzSVdpR2xYWWw5TDFXYitTNTdMeVMxbldOUEFGd1BNZjI5Uk4yMFFjejBEWGxGRlJSRzRHVHQ4S3RWcmY4TXFFODhyNnA0MGFzSXd6WUxDcXgxOHQ1TDRxIiwibWFjIjoiOTI2MDJiMTYwMDJiYTUyNTQxYzE1ZmExYWUyNTkwMmZiMWQ4MWNkYTZkZjllYTI1Y2RjZjgxZWMzNGZhNGVmNiJ9; _dc_gtm_UA-19570424-1=1; _gat_UA-19570424-1=1; _ga_EKJ8741MGP=GS1.1.1693397746.3.1.1693397954.54.0.0; _ga=GA1.1.292257908.1692780627',
        'referer': 'https://tengrinews.kz/search/?text=%D0%A2%D0%B8%D0%BC%D1%83%D1%80%20%D0%9A%D1%83%D0%BB%D0%B8%D0%B1%D0%B0%D0%B5%D0%B2&field=all',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    try:
        res = requests.get(url=url, cookies=cookies, headers=headers).text
        time.sleep(1)
        soup = BeautifulSoup(res, 'lxml')
        article_elements = soup.find("div", {"class": "tn-content"})
        title_elements = article_elements.find("h1", {"class": "tn-content-title"})
        if title_elements is not None:
            date_element = article_elements.find("span", {"class": "tn-hidden"})
            months_dict = {
                'января': '01',
                'февраля': '02',
                'марта': '03',
                'апреля': '04',
                'мая': '05',
                'июня': '06',
                'июля': '07',
                'августа': '08',
                'сентября': '09',
                'октября': '10',
                'ноября': '11',
                'декабря': '12'
            }
            if date_element is not None:
                date = date_element.get_text().rstrip()[:-7]
                day, month_name, year = date.split()
                month = months_dict[month_name]
                formatted_date = f'{day}.{month}.{year}'
            else:
                date_element = article_elements.find("li", {"class": "tn-hidden@lt"})
                if date_element is not None:
                    date = date_element.get_text().rstrip()[:-7]
                    day, month_name, year = date.split()
                    month = months_dict[month_name]
                    formatted_date = f'{day}.{month}.{year}'
                else:
                    date = ''    
            title = title_elements.text.replace(date_element.get_text(), '')
        else:    
            title = ''
        text_article_elements = soup.find("article", {"class": "tn-news-text"})
        if text_article_elements is not None:
            subtitle_elements = text_article_elements.find('p')
            if subtitle_elements is not None:
                subtitle = subtitle_elements.get_text()
            else:
                subtitle = ''
            text_element = text_article_elements.find_all('p')
            text_all = ''
            if text_element != []:
                for text in text_element:
                    text_all += text.get_text()
            else:
                text_all = text_article_elements.get_text().replace('\n', ' ').strip()
        else:
            print('Статья не найдена')           
        sourse = 'tengrinews.kz'    
        parse_article = {
            "title": title.rstrip().replace('\n', ''),
            "subtitle": subtitle,
            "url": url,
            "date": formatted_date,
            "text": text_all.replace('\xa0', ' '),
            "sourse": sourse,
            "person_id": person_id,
            "assets_id": assets_id
        }
        print(parse_article) 
    except Exception as ex:
        print(ex)

# get_data('https://tengrinews.kz/curious/naveki-tvoya-jansaya-abdumalik-vyishla-zamuj-497361/', person_id=1,assets_id=1)

parse = {
    # 1: {1:'Vladimir+Kim', 2:'Владимир+Ким', 3: 'KAZ+Minerals+Limited', 
    #     4:'Nova+Resources+B.V.', 5:'Vostok+Cooper+B.V.', 6:'Vostok+Holdings+Ltd', 
    #     7:'Folin+Universal+Trust', 8:'ТОО+«Корпорация+Казахмыс»'},          
    # 2: {9:'Timur+Kulibaev',10:'Тимур+Кулибаев',11:'Joint+Resources',
    #           12:'Кристалл+Менеджмент', 13:'Каспий+нефть', 14:'Шубарколь+Премиум'},
    # 3: {15:'Dinara+Kulibaeva', 16:'Динара+Кулибаева', 17:'Холдинговая+Группа+Алмэкс',
    #       18:'Astana+IT+University', 19:'Шубарколь+Премиум'},
    4: { 21: 'Вячеслав+Ким'}
    # 5: {25:'Nurlan+Smagulov',26:'Нурлан+Смагулов', 27: 'Астана+Групп', 28: 'Астана+Моторс',
    #           29:'ТРЦ+MEGA', 30:'MEGA+Alma-Ata', 31: 'MEGA+Park', 31: 'MEGA+Silk+Way'},
    # 6: {33:'Alexandr+Mashkevich', 34: 'Александр+Машкевич', 35: 'Eurasian+National+Resources+corporation',
    #          36:'Евразийская+финансовая+компания', 37:'Евразийский+банк'}           
    }
start = time.time()
parse_list = []
for items in parse.items():
    print( items[1])
    for item in items[1].items():
        page = 1
        print(f'Сбор даныных со страницы {page}', items[0], item[1],  item[0])
        