'''
    Сорри, что на русском, просто пояснить будет проще.
    Сейчас я выдам ответ на основе знаний, полученных из Лутца 1 год назад.
Команда import выполняет скрипт и все переменные импортированного модуля видны только в нём.
Переменные из внешнего модуля можно заюзать только через его имя(если только переменные не импортированы явно
ыерез from module import или from module import *). Если ещё раз импортировать тот же модуль,
то ничего не произойдёт, даже если после первого
импорта что-то поменяется в коде.
    Запускаем модуль a. Он сначала импортирует c, где лежит x, тем самым инициализируя x.
Потом импортируем b, который импортирует c, но скрипт из с не выполняется, а только объвляет для b пространство имён c,
и изменяет x из c. Дальше выводится x из пространства имён c.
'''
