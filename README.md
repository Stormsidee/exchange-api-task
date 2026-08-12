# Exchange Rate API Task

A small Python 3.11+ script that requests exchange rates from ExchangeRate-API,
backs up the original JSON response, converts the data to a pandas DataFrame,
and saves the result as CSV and XLSX files.

## Data source

The script uses the public endpoint:

```text
https://open.er-api.com/v6/latest/USD
```

The API response contains rates with USD as the base currency. The output column
`Rate_to_USD` stores the value of one unit of each currency in USD, so the rate
returned by the API is inverted with `1 / rate`.

## Output

After a successful run, the `output` directory contains:

```text
exchange_rates_backup.json
exchange_rates.csv
exchange_rates.xlsx
```

The CSV and XLSX files contain two columns:

- `Currency` — currency code
- `Rate_to_USD` — value of one unit of the currency in USD

## Requirements

- Python 3.11+
- requests
- pandas
- openpyxl

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python exchange_rates.py
```

Basic logging is printed to the console. HTTP errors are handled by
`raise_for_status()`, and the script also validates the API `result` field and
the presence of the `rates` object.
