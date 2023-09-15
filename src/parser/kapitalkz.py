from datetime import datetime, timedelta
import time
from bs4 import BeautifulSoup
import requests
today = datetime.now().date()
today_formatted = today.strftime('%d-%m-%Y').replace('-', '.')
yesterday = (today - timedelta(days=1)).strftime('%d-%m-%Y')
yesterday_formatted = yesterday.replace('-', '.')

def get_data(main_url: str, person_id: int, assets_id: int) -> list:
    cookies = {
        '_gid': 'GA1.2.1550729038.1692343797',
        '_ym_uid': '1692343797433219100',
        '_ym_d': '1692343797',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_zero_cc': 'dab59a0d36d9ae',
        '_csrf': '957473e6e5fa8b269b11c4aa5cf1df66655a313637f95fc350b35109f80062d4a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22KX6vnZXc73FAz1zfrQHCQ1duDqwZJk91%22%3B%7D',
        '_gat_UA-69990116-2': '1',
        '_gat_gtag_UA_69990116_2': '1',
        '_zero_ss': '64df1df56efb6.1692343797.1692345308.8',
        '_ga': 'GA1.1.240733105.1692343797',
        '_ga_795LXVBMCJ': 'GS1.1.1692343796.1.1.1692345307.60.0.0',
    }
    headers = {
        'authority': 'kapital.kz',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_gid=GA1.2.1550729038.1692343797; _ym_uid=1692343797433219100; _ym_d=1692343797; _ym_isad=1; _ym_visorc=w; _zero_cc=dab59a0d36d9ae; _csrf=957473e6e5fa8b269b11c4aa5cf1df66655a313637f95fc350b35109f80062d4a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22KX6vnZXc73FAz1zfrQHCQ1duDqwZJk91%22%3B%7D; _gat_UA-69990116-2=1; _gat_gtag_UA_69990116_2=1; _zero_ss=64df1df56efb6.1692343797.1692345308.8; _ga=GA1.1.240733105.1692343797; _ga_795LXVBMCJ=GS1.1.1692343796.1.1.1692345307.60.0.0',
        'referer': 'https://kapital.kz/search?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%9A%D0%B8%D0%BC',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    response = requests.get(url=main_url, cookies=cookies, headers=headers).text
    time.sleep(1)
    parse_list =[]
    try:
        # link
        soup = BeautifulSoup(response, 'lxml')
        # step = soup.find("li", {"class": "next"})
        articles = soup.find("div", {"class": "main-news"})
        link_article = articles.find_all("a", {"class": "main-news__name"})
        # take information on article
        for link in link_article:
            url = 'https://kapital.kz' + link.get('href')
            res = requests.get(url=url, cookies=cookies, headers=headers).text
            time.sleep(1)
            soup = BeautifulSoup(res, 'lxml')
            article_date = soup.find("time", {"class": "information-article__date"})
            if article_date is not None:
                normal_date_format = article_date.text[:10].replace(".","-")
                if normal_date_format != today_formatted:
                    break
                article_date = article_date.text
            else:
                article_date = ''
            title_html_element = soup.find("h1", {"class": "article__title"})
            if title_html_element is None:
                title_html_element = soup.find("h1", {"class": "longrid__title"})
                if title_html_element is not None:
                    title = title_html_element.text
                else: 
                    title = ''     
            else:
                title = title_html_element.text  
            subtitle_html_element = soup.find("h2", {"class": "article__subtitle"})
            if subtitle_html_element is None:
                subtitle_html_element = soup.find("h2", {"class": "longrid__subtitle"})
                if subtitle_html_element is not None:
                    subtitle= subtitle_html_element .text
                else:
                    subtitle = ''
            else:
                subtitle = subtitle_html_element.text
            article_body = soup.find("div", {"class": "article__body"})
            if article_body is None:
                article_body = soup.find("div", {"class": "longrid__body"})
            article_text = article_body.find_all("div", {"class": "row"})
            text = ''
            if article_text == []:
                article_text = article_body.find_all("p")
                for t in article_text:
                    text += t.text.replace('\xa0', ' ')
            else:
                for t in article_text:
                    text += t.text.replace('\xa0', ' ')
            sourse = 'kapital.kz'
            parse_article = {
                "title": title.replace('\xa0', ' '),
                "subtitle": subtitle.replace('\xa0', ' '),
                "url": url,
                "date": article_date[:10],
                "text": text.replace('\n', ''),
                "sourse": sourse,
                "person_id": person_id, 
                "assets_id": assets_id
            }
            parse_list.append(parse_article)
        #print(parse_list)       
        return parse_list
    except Exception as ex:
        print(ex)

def pagination(url):
    cookies = {
        '_gid': 'GA1.2.1550729038.1692343797',
        '_ym_uid': '1692343797433219100',
        '_ym_d': '1692343797',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_zero_cc': 'dab59a0d36d9ae',
        '_csrf': '957473e6e5fa8b269b11c4aa5cf1df66655a313637f95fc350b35109f80062d4a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22KX6vnZXc73FAz1zfrQHCQ1duDqwZJk91%22%3B%7D',
        '_gat_UA-69990116-2': '1',
        '_gat_gtag_UA_69990116_2': '1',
        '_zero_ss': '64df1df56efb6.1692343797.1692345308.8',
        '_ga': 'GA1.1.240733105.1692343797',
        '_ga_795LXVBMCJ': 'GS1.1.1692343796.1.1.1692345307.60.0.0',
    }
    headers = {
        'authority': 'kapital.kz',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_gid=GA1.2.1550729038.1692343797; _ym_uid=1692343797433219100; _ym_d=1692343797; _ym_isad=1; _ym_visorc=w; _zero_cc=dab59a0d36d9ae; _csrf=957473e6e5fa8b269b11c4aa5cf1df66655a313637f95fc350b35109f80062d4a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22KX6vnZXc73FAz1zfrQHCQ1duDqwZJk91%22%3B%7D; _gat_UA-69990116-2=1; _gat_gtag_UA_69990116_2=1; _zero_ss=64df1df56efb6.1692343797.1692345308.8; _ga=GA1.1.240733105.1692343797; _ga_795LXVBMCJ=GS1.1.1692343796.1.1.1692345307.60.0.0',
        'referer': 'https://kapital.kz/search?q=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80+%D0%9A%D0%B8%D0%BC',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    response = requests.get(url=url, cookies=cookies, headers=headers)
    if response is not None:
        response = response.text
    else:
        response = ''   
    time.sleep(1)
    soup = BeautifulSoup(response, 'lxml')
    next = soup.find("li", {"class": "next"})
    return next

def start_parser_kapitalkz():
    parse = {
    1: {1: 'Vladimir+Kim', 2:'Владимир+Ким', 3: 'KAZ+Minerals+Limited', 4:'Nova+Resources+B.V.',
               5:'Vostok+Cooper+B.V.', 6:'Vostok+Holdings+Ltd', 7:'Folin+Universal+Trust',
               8:'ТОО+«Корпорация+Казахмыс»'},
    2: {9: 'Timur+Kulibaev', 10: 'Тимур+Кулибаев', 11: 'Joint+Resources',
              12: 'Кристалл+Менеджмент', 13: 'Каспий+нефть', 14: 'Шубарколь+Премиум'},
    3: {15:'Dinara+Kulibaeva', 16:'Динара+Кулибаева', 17:'Холдинговая+Группа+Алмэкс',
              18:'Astana+IT+University', 19:'Шубарколь+Премиум'},
    4: {20: 'Vyacheslav+Kim', 21: 'Вячеслав+Ким',22: 'Алсеко', 23:'Астана+ЕРЦ', 24:'Kaspi.kz'},
    5: {25:'Nurlan+Smagulov',26:'Нурлан+Смагулов', 27:'Астана+Групп', 28:'Астана+Моторс',
              29:'ТРЦ+MEGA', 30:'MEGA+Alma-Ata', 31:'MEGA+Park', 32:'MEGA+Silk+Way'},
    6: {33:'Alexandr+Mashkevich',34: 'Александр+Машкевич',35: 'Eurasian+National+Resources+corporation',
             36:'Евразийская+финансовая+компания', 37:'Евразийский+банк'}           
    }
    start = time.time()
    parse_list = []
    for items in parse.items():
        for item in items[1].items():
            step = not None
            page = 1
            while step is not None:
                article_list = get_data(f'https://kapital.kz/search/default/index?q={item[1]}&page={page}', person_id=items[0], assets_id = item[0])
                if article_list != []:
                    print(f'Сбор даныных со страницы {page}', items[0], item[1],  item[0])
                    parse_list.append(article_list)
                else:
                    print(f'Информации по {item[1]} нет')   
                step = pagination(f'https://kapital.kz/search/default/index?q={item[1]}&page={page}')
                if step is None:
                    print(f'По запросу{item[1]} найдено {page} страниц')
                    page = 1
                    break
                page += 1
    end = time.time()
    total = round((end - start) / 60, 1)
    print('Время выполнения парса =', total, 'минут')    
    return parse_list
# start_parser()