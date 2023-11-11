Документация к модулю работы со строкой
===
Описание функции modification_str()
---
Для проверки числа на простоту используйте функцию modification_str модуля task_1. Импортируйте её в свой код.  

    >>> from task_1 import modification_str  

'Проверяем возврат строки без изменений  

    >>> modification_str('hello world')
    'hello world'

Проверка возврат строки с преобразованием регистра без потери символов  

    >>> modification_str('Hello World')
    'hello world'

'Проверка возврат строки с удалением знаков пунктуации  

    >>> modification_str('hello world!')
    'hello world'

Проверка возврат строки с удалением букв других алфавитов

    >>> modification_str('hello world_Привет_мир')
    'hello world'

Проверяем возврат строки с преобразованием регистра без потери символов, с удалением знаков пунктуации, с удалением 
букв других алфавитов

    >>> modification_str('Hello World, Привет мир!')
    'hello world  '