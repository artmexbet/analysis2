# Описание программы

## Обзор

Программа реализует MapReduce-решение для Apache Hadoop, которое анализирует логи веб-сервера и находит четырёх пользователей, выполнивших максимальное количество одинаковых запросов.

## Формат входных данных

Входные данные представляют собой лог-файл в формате Apache:
```
IP - Username [timestamp] METHOD /path status size referrer
```

Пример:
```
192.168.0.0 - User0 [2022-10-14T14:37:37.840489] GET /big_image.png 200 1048576 https://mysite.com
```

## Структура решения

### Шаг 1: Подсчёт одинаковых запросов

**Директория:** `step1/`

#### mapper.py
Парсит каждую строку лога и извлекает:
- Имя пользователя (Username)
- Тип запроса (METHOD + путь)

Выходной формат: `Username\tMETHOD /path`

#### reducer.py
Подсчитывает количество одинаковых запросов от каждого пользователя.

Выходной формат: `Username\tMETHOD /path\tcount`

### Шаг 2: Нахождение топ-4 пользователей

**Директория:** `step2/`

#### mapper.py
Переформатирует данные для сортировки по количеству запросов.

Выходной формат: `count\tUsername\tMETHOD /path`

#### reducer.py
Сортирует результаты по убыванию количества запросов и выводит топ-4.

Выходной формат: `Username\tMETHOD /path\tcount`

## Запуск в Hadoop

### Шаг 1
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -input /home/input \
  -output /home/output-step1 \
  -mapper /home/step1/mapper.py \
  -reducer /home/step1/reducer.py
```

### Шаг 2
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -input /home/output-step1 \
  -output /home/output-step2 \
  -mapper /home/step2/mapper.py \
  -reducer /home/step2/reducer.py
```

## Локальное тестирование

Для тестирования без Hadoop можно использовать симуляцию MapReduce:

```bash
# Шаг 1
cat example.txt | python3 step1/mapper.py | sort | python3 step1/reducer.py

# Полная обработка (Шаг 1 + Шаг 2)
cat example.txt | python3 step1/mapper.py | sort | python3 step1/reducer.py | \
  python3 step2/mapper.py | sort -t$'\t' -k1,1nr | python3 step2/reducer.py
```

## Пример результата

Входные данные (example.txt):
```
192.168.0.0 - User0 [2022-10-14T14:37:37.840489] GET /big_image.png 200 1048576 https://mysite.com
...
```

Результат:
```
User0   GET /big_image.png   100
```

## Особенности реализации

1. **Эффективность**: Программа оптимизирована для обработки больших объёмов данных (более 1 ГБ) благодаря использованию потоковой обработки (streaming) и MapReduce-подхода.

2. **Простота**: Код максимально простой и понятный, без использования сторонних библиотек.

3. **Совместимость с Hadoop**: Скрипты используют стандартный ввод/вывод (stdin/stdout), что обеспечивает совместимость с Hadoop Streaming.

4. **Обработка ошибок**: Скрипты пропускают некорректные строки, обеспечивая устойчивость к ошибкам в данных.
