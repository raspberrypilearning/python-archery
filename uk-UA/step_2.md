## Створення фону

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Для твоєї гри потрібен барвистий фон.
</div>
<div>

![Область виводу з прямокутником небесного кольору, над прямокутником зеленого кольору, які створюють фон.](images/background.png){:width="300px"}

</div>
</div>

### Відкрий початковий проєкт

--- task ---

Open the [Target practice starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} project. The code editor will open in another browser tab.

Якщо у тебе є обліковий запис в Trinket, ти можеш натиснути на кнопку **Remix**, щоб зберегти копію до своєї бібліотеки **My Trinkets**.

--- /task ---

### Редагування неба

--- task ---

Стартовий проєкт вже містить деякий код, написаний для тебе.

Натисни **'Запуск'**, щоб побачити синій прямокутник, намальований з x=`0`, y=`0` (верхня частина екрана). Цей піксельний прямокутник `400` x `250` зображує небо.

![Синій прямокутник з чорною рамкою вздовж нього, над сірим прямокутником. Верхній лівий кут полотна позначено як x=0, y=0 - це початок прямокутника. Ширина позначена як 400, а висота - як 250. Показано код rect(0, 0, 400, 250).](images/sky_stroke.png){:width="400px"}

**Порада:** 💡 Координати починаються з (x=0, y=0) від лівого верхнього кута. Можливо, це буде відрізнятися від інших систем координат, які використовувались тобою раніше.

--- /task ---

--- task ---

Небо обведено чорною рамкою (обведенням).

Щоб вимкнути обведення для всіх фігур необхідно додати `no_stroke()` до функції `setup`:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 11
line_highlights: 15
---
def setup():
# Налаштуй свою гру тут

    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Run** your code again and notice 👀 that the border (stroke) has now disappeared.

**Запускай** знову свій код та зверни увагу 👀 на те, як зникла рамка (обведення).

--- /task ---

### Намалюй траву

--- task ---

**Додай** код, щоб намалювати зелений прямокутник в нижній частині екрана.

![Область виводу з прямокутником небесного кольору, над прямокутником зеленого кольору, які створюють фон. Верхній лівий кут прямокутника позначено як x=0, y=250 - це початок прямокутника. Ширина виділена як 400, а висота - як 150. Показано код rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 17
line_highlights: 27, 28
---
def draw():
# Що відбувається на кожному кадрі

    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

**Tip:** 💡 We have added comments to our code, like `# Set the fill colour for the sky to cyan`, to tell you what it does. You don't need to add comments to your code, but they are helpful to remind you what lines of code do.

--- /task ---

--- task ---

**Test:** 🔄 Run your project again to view the finished background.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---
