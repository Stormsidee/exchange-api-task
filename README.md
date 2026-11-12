# Exchange Rate Export

Python-скрипт получает курсы валют из ExchangeRate-API и сохраняет исходный ответ в JSON, а таблицу курсов в CSV и XLSX.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python exchange_rates.py
```

На Windows активируйте окружение командой `.venv\Scripts\activate`. Для запуска нужен доступ к открытому API, ключ не требуется.

## Что получается

В каталоге `output/` есть пример результата:

| Файл | Содержимое |
| --- | --- |
| `exchange_rates_backup.json` | Исходный ответ API |
| `exchange_rates.csv` | Таблица курсов в CSV |
| `exchange_rates.xlsx` | Та же таблица в Excel |

API возвращает количество единиц валюты за доллар. Колонка `Rate_to_USD` показывает стоимость одной единицы валюты в долларах, поэтому исходный курс инвертируется. Скрипт использует таймаут HTTP-запроса, проверяет статус ответа и наличие курсов.
