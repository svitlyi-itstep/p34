import requests


def convert_currency(amount, from_currency, to_currencies):
    url = f'https://v6.exchangeratesapi.io/latest?base={from_currency}&symbols={",".join(to_currencies)}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data['rates']

        converted_results = {}
        for currency in to_currencies:
            if currency in rates:
                converted_results[currency] = amount * rates[currency]
            else:
                converted_results[currency] = None

        return converted_results
    else:
        print("Ошибка при получении курсов валют")
        return None


def main():
    try:
        from_currency = input("Введите название валюты, из которой хотите конвертировать (например, USD): ").upper()
        to_currencies = [c.strip().upper() for c in input(
            "Введите названия валют, в которые хотите конвертировать, через запятую (например, EUR, GBP, UAH): ").split(
            ",")]
        amount = float(input("Введите количество денег для конвертации: "))

        converted_results = convert_currency(amount, from_currency, to_currencies)
        if converted_results:
            print(f"Результаты конвертации:")
            for currency, converted_amount in converted_results.items():
                if converted_amount is not None:
                    print(f"{amount} {from_currency} = {converted_amount} {currency}")
                else:
                    print(f"Курс валюты {currency} не найден")
        else:
            print("Ошибка при конвертации валют")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, убедитесь, что введены корректные значения.")


if __name__ == "__main__":
    main()