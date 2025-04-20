# Проект "GooseCycleWords"

### Инструкция по начальной настройке проекта:
1. Обновить pip и установить все необходимое:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. Синхронизировать структуру базы данных с моделями: 
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Создать суперпользователя
   ```bash
   python manage.py createsuperuser
   ```

### Добавление слов в базу данных:
1. Пройти по [ссылке](https://docs.google.com/spreadsheets/d/1YbYf7SLtEpUzzKlDy3BGpTMENcaaVtO6DuReRQio6NU/edit?usp=sharing) 
и скачать таблицы *Task9*, *Task10*, *Task11*, *Task12* в формате **csv**
---
![tables](.readme_media/tables.png)
![files](.readme_media/files.png)
![download_csv](.readme_media/download_csv.png)
---
2. Зайти в админ-панель */admin* под аккаунтом, который был создан командой createsuperuser
---
![admin](.readme_media/admin.png)
---
3. Загрузить таблицы соответственно моделям
---
![models](.readme_media/models.png)
![import](.readme_media/import.png)
![import2](.readme_media/import2.png)
![import3](.readme_media/import3.png)
![confirm](.readme_media/confirm.png)
---