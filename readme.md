## Описание
Тестовое задание по разработке лендинга.

## Установка
```shell
$ git clone https://github.com/GSPVK/vangertz
$ cd vangertz
$ pip install -r req.pip
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

#### Скопируйте файл .env.example и переименуйте его в .env, настройте в нём подключение к БД:
```sh
cp .env.example .env
```

## ТЗ
Необходимо собрать с помощью bootstrap 5 и запустить новую страницу по макету 
https://www.figma.com/file/csU67B0SQVZO1AkwvMZa3D/Тестовое-задание-N2?type=design&node-id=1-1012&mode=design&t=wz2qpqpXo6RochwT-0 

- сборку проекта осуществить с помощью python 3.9, Django 4.1 и MySQL
- проект разместить в git репозитории
- для сборки клиентской части страницы необходимо использовать bootstrap 5
- для запуска слайдера необходимо использовать slick slider http://kenwheeler.github.io/slick/ (см. Slider Syncing)
- по клику на большую фотографию на слайдере фотки должны открываться на весь экран и листаться галереей
- необходимо чтобы slider заполнялся через админку django. Необходимо настроить визуально понятный admin.py, чтобы выводилась картинка и название в списке записей элементов слайдера.
- для картинок модели слайдера необходимо использовать пакет django-filer и через него грузить картинки в слайдер
- для кадрирования картинок использовать easythumbnails
- записи слайдера в админке должны сортироваться при помощи drag&drop, для этого необходимо использовать пакет django-admin-sortable2
- все зависимости для запуска проекта расположить в файле req.pip в корне проекта.