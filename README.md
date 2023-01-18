## Rundom notice

Скрипт отправки напоминания в telegram чат в рандомное время три раза в день.

Использование:

    cp .env.example .env

Впишите корректные данные в .env

Добавьте задания в крон:

    30 9  * * * /usr/bin/python3 /script_path/rundom_notice.py 1
    0 13  * * * /usr/bin/python3 /script_path/rundom_notice.py 2
    0 16  * * * /usr/bin/python3 /script_path/rundom_notice.py 3

