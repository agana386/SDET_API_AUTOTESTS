# API Autotests

## Стек
- Python 3.10
- pytest
- requests
- pydantic
- allure
- pytest-xdist

## Паралельный запуск тестов

pytest -n auto -v

## С выводом отчетов Allure

pytest --alluredir=allure-results

allure serve allure-results

В проекте использовались:
- Python requests
- Библиотека для сериализации/десериализации pydantic
- Тестовый фреймворк pytest

## Allure Report
![Allure](./Allure_result.png)