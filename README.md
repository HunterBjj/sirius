# <p align="center"> ![image](https://github.com/HunterBjj/sirius/assets/64096687/cf1e2932-8043-4441-a22b-b199c0544999) </p>
# Тестовое задание компании Сириус на позицию “Разработчик”

Реализовать API с 3мя эндпоинтами.
1.1. Принимает json с картинкой (base64) и описание картинки в виде текста.

1.2. Отдает список картинок с описанием.

1.3. Удаляет картинку из бд по ID.

Реализовать интерфейс который общается с API из пункта 1.
2.1. Форма по отправке картинки с описанием.

2.2. Список всех картинок с кнопкой удаления.

Реализуйте класс “Test”. При создании экземпляра, класс должен принимать 2 именованных аргумента x, y. Должны быть соблюдены следующие проверки и методы:

3.1. Аргументы при создании экземпляра класса должны быть числами, реализовать проверку.

3.2. Метод который будет получать x викторин с https://jservice.io/ и записывать в бд с проверкой на уникальность. Записи должны быть разложены по категориям.

3.4. Метод получения кол-ва записей в категории. Принимает название категории в качестве аргумента. Аргумент должен быть строкой.

3.3. Метод который будет возвращать y записей с бд и сохранять в json c названием текущей даты запроса данных.

Технологии:  Python 3, Django (DRF), Vue.js, Любая база данных SQL.

# Итог

Для запуска приложение необходимо:
- git clone https://github.com/HunterBjj/rait_scan_birds;
- провеcти миграции python manage.py makemigrations, python manage.py migrate;
- запустить локальный сервер python manage.py runserver.

  Приложение состоит из пяти html страниц:

   <p align="center"> Рисунок 1 - Авторизация </p>

    <p align="center"> Рисунок 2 - Регистрация </p>
    

    <p align="center"> Рисунок 3 - Просмотр птиц </p>
  

      База данных SQLlite состоит одной таблицы:
    - Image(картинки).

      
    <p align="center"> Заключение </p>
    
> . 
