# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
def update_global_value(**value):
    for key, value in value.items():
        if key[len(key) - 1] == 's' and len(key) > 1:
            globals()[key[:-1]] = value
            globals()[key] = None


bras = 5
left = 4
one = 1
fes = 7
s = 25

print(f'Было:  {globals()["bras"] = }      {globals().get("bra", None) = }      {globals()["left"] = } '
      f'       {globals()["one"] =  }      {globals()["fes"] = }                {globals().get("fe", None) = } '
      f'       {globals()["s"] = }')
update_global_value(**globals())
print(f'Стало: {globals()["bras"] = }      {globals()["bra"] =           }      {globals()["left"] = } '
      f'       {globals()["one"] = }       {globals()["fes"] = }                {globals()["fe"] = }'
      f'                  {globals()["s"] = }')
