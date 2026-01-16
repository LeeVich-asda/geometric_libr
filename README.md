# Документация проекта Geometric Lib

## Общее описание решения
Библиотека для вычисления площадей и периметров геометрических фигур.

## Описание функций

### circle.py
![](https://ecalc.ru/images/krug/radius.png)
#### `area(r)`
Вычисляет площадь круга.
- Параметры: `r` (радиус)
- Возвращает: площадь
- Пример: `area(3) → 28.27431`

#### `perimeter(r)`
Вычисляет длину окружности.
- Параметры: `r` (радиус)
- Возвращает: длина окружности
- Пример: `perimeter(3) → 18.84954`

### square.py
![](https://3.shkolkovo.online/st/5/v-thumb/theory_00_26_2__37ret.png)
#### `area(a)`
Вычисляет площадь квадрата.
- Параметры: `a` (сторона)
- Пример: `area(4) → 16`

#### `perimeter(a)`
Вычисляет периметр квадрата.
- Параметры: `a` (сторона)
- Пример: `perimeter(4) → 16`

### rectangle.py
![](https://ru.onlinemschool.com/pictures/area/rectangle1.png)
#### `area(a, b)`
Вычисляет площадь прямоугольника.
- Параметры: `a`, `b` (стороны)
- Пример: `area(3, 4) → 12`

#### `perimeter(a, b)`
Вычисляет периметр прямоугольника.
- Параметры: `a`, `b` (стороны)
- Пример: `perimeter(3, 4) → 14`

### triangle.py
![](https://cdn.lifehacker.ru/wp-content/uploads/2020/02/7_1580895952.jpg)
#### `area(a, h)`
Вычисляет площадь треугольника.
- Параметры: `a` (основание), `h` (высота)
- Пример: `area(6, 4) → 12.0`

#### `perimeter(a, b, c)`
Вычисляет периметр треугольника.
- Параметры: `a`, `b`, `c` (стороны)
- Пример: `perimeter(3, 4, 5) → 12`

## История изменений
82a3eb1 Fixed a bug in perimeter calculation rectangle.py
6d46ba3 Add rectangle.py
86edb1c L-05: Update Docs. Add user agreement info
438b89a L-05: Add user agreement
6adb962 L-03: Docs added
3049431 L-04: Add rectangle.py
b5b0fae L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
