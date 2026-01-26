import sys
import functools
import requests
import logging
import io

def logger(func=None, *, handle=sys.stdout):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            is_logger = isinstance(handle, logging.Logger)

            '''лог старта'''
            start_msg = f"Вызов {func.__name__} с аргументами: args={args}, kwargs={kwargs}"
            if is_logger:
                handle.info(start_msg)
            else:
                handle.write(f"INFO: {start_msg}\n")

            try:
                result = func(*args, **kwargs)
                '''лог успешного завершения'''
                end_msg = f"{func.__name__} завершена. Результат: {result}"
                if is_logger:
                    handle.info(end_msg)
                else:
                    handle.write(f"INFO: {end_msg}\n")
                return result
            except Exception as e:
                '''лог ошибки'''
                err_msg = f"Исключение в {func.__name__}: {type(e).__name__}: {e}"
                if is_logger:
                    handle.error(err_msg)
                else:
                    handle.write(f"ERROR: {err_msg}\n")
                raise

        return wrapper

    return decorator if func is None else decorator(func)


def get_currencies(currency_codes: list,
                   url: str = "https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"API недоступен: {e}")

    try:
        data = response.json()
    except ValueError as e:
        raise ValueError(f"Некорректный JSON: {e}")

    if "Valute" not in data:
        raise KeyError("Отсутствует ключ 'Valute'")

    result = {}
    for code in currency_codes:
        if code not in data["Valute"]:
            raise KeyError(f"Валюта '{code}' отсутствует в данных")

        if "Value" not in data["Valute"][code]:
            raise KeyError(f"Для валюты '{code}' отсутствует ключ 'Value'")

        val = data["Valute"][code]["Value"]
        if not isinstance(val, (int, float)):
            raise TypeError(f"Курс валюты '{code}' имеет неверный тип: {type(val).__name__}")

        result[code] = val

    return result


def demo_stringio():
    '''поток для логов'''
    log_stream = io.StringIO()
    '''декоратор'''
    @logger(handle=log_stream)
    def test_function(x, y):
        return x * y

    result = test_function(5, 7)
    print(f"Результат выполнения: {result}")

    '''получаем и выводим логи'''
    logs = log_stream.getvalue()
    print("\nСодержимое логов (io.StringIO):")
    print(logs)
