'''
Система собирает информацию с датчиков, в ней есть
модуль логирования, который заносит в журнал все
обращения к датчикам.
В системе есть модуль, выполняющий обращения для
получения данных с датчиков и модуль генерации htmlпредставления.
Запуск системы осуществляется из головного модуля.


Модуль 1: сбор информации с датчиков    # data_provider
Модуль 2: логирование                   # logger
Модуль 3: UI                            # user_interface
Vjlekm 4: HTML-генератор                # html_creater
Vjlekm 5: главный модуль                # main


В рамках этих модулей опишем набор методов:

data_provider
    get_temperature, get_pressure, get_wind_speed
logger
    temperature_logger, pressure_logger, wind_speed_logger
user_interface
    temperature_view, pressure_view, wind_speed_view
html_creater
    create
main


'''
