from pathlib import Path
import json
import logging

import pandas as pd
import requests


API_URL = "https://open.er-api.com/v6/latest/USD"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
JSON_FILE = OUTPUT_DIR / "exchange_rates_backup.json"
CSV_FILE = OUTPUT_DIR / "exchange_rates.csv"
XLSX_FILE = OUTPUT_DIR / "exchange_rates.xlsx"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    logging.info("Requesting exchange rates")
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("result") != "success":
        raise RuntimeError(f"API returned an error: {data}")

    rates = data.get("rates")
    if not isinstance(rates, dict) or not rates:
        raise ValueError("The API response does not contain exchange rates")

    with JSON_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    rows = []
    for currency, rate in rates.items():
        if rate:
            rows.append(
                {
                    "Currency": currency,
                    "Rate_to_USD": 1 / rate,
                }
            )

    df = pd.DataFrame(rows).sort_values("Currency")

    df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")
    df.to_excel(XLSX_FILE, index=False)

    logging.info("JSON backup saved to %s", JSON_FILE)
    logging.info("CSV saved to %s", CSV_FILE)
    logging.info("XLSX saved to %s", XLSX_FILE)
    logging.info("Currencies received: %s", len(df))


if __name__ == "__main__":
    main()
