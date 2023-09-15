from datetime import date, timedelta, datetime



list_name = ['Владимир+Ким', 'KAZ+Minerals+Limited', 'Nova+Resources+B.V.',
               'Vostok+Cooper+B.V.', 'Vostok+Holdings+Ltd', 'Folin+Universal+Trust',
               'ТОО+«Корпорация+Казахмыс»']
list_name = ['Тимур+Кулибаев', 'Steppe+Capital+Pte+Ltd', 'KazStroyService+Infrastructure+BV',
             'Asset+Minerals+Holdings','АО+«Joint+Resources»,'
             'АО+«Кристалл+Менеджмент»','АО+«Каспий+нефть»', 'АО+«Шубарколь+Премиум»']
list_name = ['Динара+Кулибаева','Halyk+Bank','АО+«Народный+банк+Казахстана»',
             'АО+«Холдинговая+Группа+«Алмэкс»','ТОО+«Astana+IT+University»','АО+«Шубарколь+Премиум»',
             'ТОО+«Центр+инновационных+и+информационных+технологий»',
             'ТОО+«Private+clinic+Almaty»','Корпоративный+фонд+«SOS+Детские+деревни+Казахстана»']
list_name = ['Вячеслав+Ким', 'АО+«Алсеко»', 'ТОО+«Астана-ЕРЦ»','ТОО+«ELTOP+Soft»','ТОО+«Позитив+Инвест»',
             'Kaspi.kz']
list_name = ['Нурлан+Смагулов', '«Астана+Групп»','«Астана+Моторс»','ТРЦ+MEGA',
             'MEGA+Alma-Ata', 'MEGA+Park', 'MEGA+Silk+Way']
list_name = ['Александр+Машкевич',
             'Eurasian+National+Resources+corporation','АО+«Евразийская+финансовая+компания»',
             'АО+«Евразийская+промышленная+компания»','ТОО+«Евразийская+производственная+компания»',
             'АО+«Евразийский+банк»']


list_name_1 = ['Владимир Ким', 'KAZ Minerals Limited', 'Nova Resources B.V.',
               'Vostok Cooper B.V.', 'Vostok Holdings Ltd', 'Folin Universal Trust',
               'ТОО «Корпорация Казахмыс»']
list_name_1 = ['Тимур Кулибаев', 'Steppe Capital', 'KazStroyService Infrastructure BV',
             'Asset Minerals Holdings','АО «Joint Resources»',
             'АО «Кристалл Менеджмент»',' Каспий нефть', 'Шубарколь Премиум']
list_name_1 = ['Динара Кулибаева','Halyk Bank','Народный банк Казахстана',
             'Холдинговая Группа «Алмэкс','Astana IT University','Шубарколь Премиу',
             'Центр инновационных и информационных технологий',
             '«Private clinic Almaty','Корпоративный фонд «SOS+Детские деревни Казахстана»']
list_name_1 = ['Вячеслав Ким', 'Алсеко', 'Астана-ЕРЦ','Kaspi.kz']
list_name_1 = ['Нурлан Смагулов', 'Астана Групп','Астана Моторс','ТРЦ MEGA',
             'MEGA Alma-Ata', 'MEGA Park', 'MEGA Silk Way']
list_name_1 = ['Александр Машкевич',
             'Eurasian National Resources corporation','Евразийская финансовая компания',
             'Евразийский банк']

total_list =[['Vladimir Kim','Владимир Ким', 'kaz minerals limited',
              'nova resources b.v.',
              'Vostok Cooper B.V.', 'Vostok Holdings Ltd',
              'Folin Universal Trust','ТОО «Корпорация Казахмыс»'],
             ['Timur Kulibaev','Тимур Кулибаев','Joint Resources',
              'Кристалл Менеджмент', 'Каспий нефть', 'Шубарколь Премиум'],
             ['Dinara Kulibaeva','Динара Кулибаева','Холдинговая Группа Алмэкс',
              'Astana IT University','ШубаркольПремиум'],
             ['Vyacheslav Kim','Вячеслав Ким', 'Алсеко', 'Астана-ЕРЦ', 'Kaspi.kz'],
             ['Nurlan Smagulov','Нурлан Смагулов', 'Астана Групп', 'Астана Моторс',
              'ТРЦ MEGA', 'MEGA Alma-Ata', 'MEGA Park', 'MEGA Silk Way'],
             ['Alexandr Mashkevich','Александр Машкевич', 'Eurasian National Resources corporation',
             'Евразийская финансовая компания', 'Евразийский банк']]

parse = {
    1: ['Vladimir+Kim', 'Владимир+Ким', 'KAZ+Minerals+Limited', 'Nova+Resources+B.V.',
               'Vostok+Cooper+B.V.', 'Vostok+Holdings+Ltd', 'Folin+Universal+Trust',
               'ТОО+«Корпорация+Казахмыс»'],
    2: ['Timur+Kulibaev','Тимур+Кулибаев','Joint+Resources',
              'Кристалл+Менеджмент', 'Каспий+нефть', 'Шубарколь+Премиум'],
    3: ['Dinara+Kulibaeva','Динара+Кулибаева','Холдинговая+Группа+Алмэкс',
              'Astana+IT+University','Шубарколь+Премиум'],
    4: ['Vyacheslav+Kim','Вячеслав+Ким', 'Алсеко', 'Астана-ЕРЦ', 'Kaspi.kz'],
    5: ['Nurlan+Smagulov','Нурлан+Смагулов', 'Астана+Групп', 'Астана+Моторс',
              'ТРЦ+MEGA', 'MEGA+Alma-Ata', 'MEGA+Park', 'MEGA+Silk+Way'],
    6: ['Alexandr+Mashkevich','Александр+Машкевич', 'Eurasian+National+Resources+corporation',
             'Евразийская+финансовая+компания', 'Евразийский+банк']           
}

parse = {
    1: {1: 'Vladimir+Kim', 2:'Владимир+Ким', 3: 'KAZ+Minerals+Limited', 4:'Nova+Resources+B.V.',
               5:'Vostok+Cooper+B.V.', 6:'Vostok+Holdings+Ltd', 7:'Folin+Universal+Trust',
               8:'ТОО+«Корпорация+Казахмыс»'},
    2: {9:'Timur+Kulibaev',10:'Тимур+Кулибаев',11:'Joint+Resources',
              12:'Кристалл+Менеджмент', 13:'Каспий+нефть', 14:'Шубарколь+Премиум'},
    3: {15:'Dinara+Kulibaeva', 16:'Динара+Кулибаева', 17:'Холдинговая+Группа+Алмэкс',
              18:'Astana+IT+University', 19:'Шубарколь+Премиум'},
    4: {20: 'Vyacheslav+Kim', 21: 'Вячеслав+Ким',22: 'Алсеко', 23:'Астана-ЕРЦ', 24:'Kaspi.kz'},
    5: {25:'Nurlan+Smagulov',26:'Нурлан+Смагулов', 27:'Астана+Групп', 28:'Астана+Моторс',
              29:'ТРЦ+MEGA', 30:'MEGA+Alma-Ata', 31:'MEGA+Park', 31:'MEGA+Silk+Way'},
    6: {33:'Alexandr+Mashkevich',34: 'Александр+Машкевич',35: 'Eurasian+National+Resources+corporation',
             36:'Евразийская+финансовая+компания', 37:'Евразийский+банк'}           
}

today = datetime.now().date()
today_formatted = today.strftime('%d-%m-%Y').replace('-', '.')
yesterday = (today - timedelta(days=1)).strftime('%d-%m-%Y')
yesterday_formatted = yesterday.replace('-', '.')

print(today_formatted, yesterday_formatted)