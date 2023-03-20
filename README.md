# Учебный проект: сайт - интерактивная карта Москвы с интересными местами
Рабочая версия сайта - http://tren123.pythonanywhere.com/  
Фронтенд предоставила команда devman - [репозиторий](https://github.com/devmanorg/where-to-go-frontend)

## Особенности проекта:
- Кастомизированная панель админа - превью загружаемых фотографий, удобный редактор описаний мест, удобное добавление и сортировка фотографий в одном окне 
- API с 1 методом для передачи данных с бэкэнда на фронтэнд
- Пользовательская консольная команда для загрузки контента из файла json: 
```
$ python3 manage.py load_place http://адрес/файла.json
```


## Инструкция по поднятию dev версии на локальном компьютере:
- клонировать репозиторий
```
$ git clone https://github.com/Tren-123/where_to_go
```
- установить зависимости
```
$ pip install -r requirements.txt
```
- создать и наполнить бд тестовыми данными
```
$ python3 manage.py migrate
```
[репозиторий](https://github.com/devmanorg/where-to-go-places/tree/master/places) с тестовыми данными\
команда для загрузки тестовых данных:
```
$ python3 manage.py load_place http://адрес/файла.json
```
- создать пользователя админки
```
$ python3 manage.py createsuperuser
```
- запустить сайт на локальном компьютетере
```
$ python3 manage.py runserver
```
- ссылка на сайт http://127.0.0.1:8000/
- ссылка на панель админа http://127.0.0.1:8000/admin/

## Переменные окружения и пример json файла с контентом для сайта
Для работы проекта требуются следующие переменные окружения:
- $SECRET_KEY - секретный ключ, не выкладывайте данное значение в открытый доступ. Подробнее в [документации](https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key) django
- $DEBUG - настройка представления информации об ошибках. Никогда не используйте значение True в продакшене. Подробнее в [документации](https://docs.djangoproject.com/en/4.1/ref/settings/#debug) django
- $ALLOWED_HOSTS - Список доверенных значений хост/домен. Подробнее в [документации](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts
) django 
Пример файла .env со значениями переменных для запуска **dev** версии сайта
```
$SECRET_KEY=your_secret_key_keep_it_in_secret
$DEBUG=true
$ALLOWED_HOSTS=127.0.0.1:8000 localhost:8000
```
Пример файла .env со значениями переменных для запуска **prod** версии сайта
```
$SECRET_KEY=your_secret_key_keep_it_in_secret
$DEBUG=false
$ALLOWED_HOSTS=your_host_name_1 your_host_name_2 ...
```
Пример json файла с контентом для сайта
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
