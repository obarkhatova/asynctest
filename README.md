### Тестовое задание: ###

Напишите скрипт, запускающий асинхронные задачи, выводящие через случайное
количество времени (до 5 секунд) ваше имя, название этой вакансии,
ожидаемый уровень зарплаты через год.

После выполнения всех асинхронных задач скрипт должен прочитать stdin и вывести sha256
хэш от прочитанных данных.

Код должен проходить без замечаний проверку линтером wemake-python-styleguide.

Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration

Обязательно 100% покрытие тестами



### ###

```commandline

Usage: run.py [OPTIONS]

Options:
  --name TEXT            Your name
  --vacancy TEXT         Vacancy
  --salary INTEGER       Salary expected
  --delay FLOAT RANGE    Max delay  [0<=x<=9]
  --count INTEGER RANGE  Task count  [0<=x<=50]
  --help                 Show this message and exit.

```

Example

```commandline
python run.py --name Myname --salary 2000 --vacancy "UX" --delay 0.5 --count 5
Myname applies for "UX" position with expected salary 2000
Myname applies for "UX" position with expected salary 2000
Myname applies for "UX" position with expected salary 2000
Myname applies for "UX" position with expected salary 2000
Myname applies for "UX" position with expected salary 2000

Please type smth to finish  qwerty
65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
```
Run with default values

```commandline
python run.py
TestName applies for "Backend developer" position with expected salary 100
TestName applies for "Backend developer" position with expected salary 100
TestName applies for "Backend developer" position with expected salary 100

Please type smth to finish
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
