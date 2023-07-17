# ded95
# Flask/PostgreSQL/Gunicorn+Nginx
## Инструкция по развертыванию:
1. Открыть консоль, установить PostgreSQL:
```
sudo apt update
sudo apt -y install postgresql
```
2. Настройка PostgreSQL
```
# переключение на пользователя postgres
sudo -i -u postgres
# входим в консоль управления
psql
# проверка информации о подключении
\conninfo
# что бы выйти
\q
# Создадим пользователя postgres
createuser --interactive
```
3. Создать базу дунных
```
createdb имя_базы
# подключение к базе данных
sudo su - имя_пользователя
# проверка о подключении
psql
\conninfo
# выход
\q
```
4. Клонирование репозитория:
```
git clone https://github.com/IgorBukharevich/ded96.git
```
---
5. Создать в коталоге conf .env-файл
* Добавить в файл параметры:
```
# APP FLASK
HOST='host_flask_app'
PORT='port_falsk_app'
DEBUG='True'

# KEY FlASK PROJECT
KEY_FLASK='KEY_Flask_APP'

# SETTINGS DATABASES
DIALECT_DB='postgresql'
NAME_DB='name_database'
HOST_DB='host_database'
PORT_DB='port_database'
USER_DB='user_postgres'
PASSWORD_DB='password_database'

```
6. Установить все зависимотсти из файла requirements.txt:
```
python -m pip install -r requirements.txt
```
7. Создание файлов сокета и служебных файлов systemd для Gunicorn
* Создайть и открыть файл soket systemd для Gunicorn с привилегиями sudo:
```
sudo nano /etc/systemd/system/gunicorn.socket
```
*Конфигурационный файл gunicorn.socket*
после сохранить файл!
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
* Создать и отркыть файл service и служебных файлов systemd Gunicorn c привилегиями sudo:
```
sudo nano /etc/systemd/system/gunicorn.service
```
*Конфигурационный файл gunicorn.service* name_app(conf),project_name(ded95)
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=user_name
Group=group_name
WorkingDirectory=/home/user_name/name_app
ExecStart=/home/user_name/project_name/venv/bin/gunicorn \
          --access-logfile - \
          --workers 5 \
          --bind unix:/run/gunicorn.sock \
          name_app.wsgi:application

[Install]
WantedBy=multi-user.target
```
* Запуск и активация сокета
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```
* Проверка файла Gunicorn
```
# состояние процесса, удалось ли запустить
sudo systemctl status gunicorn.socket
# проверка наличие файла gunicorn.sock в каталоге /run
file /run/gunicorn.sock
```
* Тестирование и активация сокета
*Проверка статуса работы gunicorn.socket и gunicorn.service*
```
sudo systemctl status gunicorn
```
*Тестирование механизма активации сокета*
```
curl --unix-socket /run/gunicorn.sock localhost
```
8. Настройка Nginx как проксе для Gunicorn
* Для начала нужно создать и открыть новый серверный блок в каталоге Nginx sites-available
* *Конфигурационный файл Nginx*
```
server {
        listen 80;
        server_name ded96 www.ded96;

        location / {
                include proxy_params;
                proxy_pass http://unix:/home/name_develop/ded96/ded96.sock;
        }
}
```
