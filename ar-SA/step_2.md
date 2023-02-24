## قم بإنشاء خلفية

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a colourful background.
</div>
<div>

! [منطقة مخرجات مع مستطيل بلون السماء فوق مستطيل بلون العشب لإنشاء الخلفية.] (images / background.png) {: "width = "300px}

</div>
</div>

### Open the starter project

--- task ---

افتح مشروع [بداية الرماية](https://trinket.io/python/eb67937f99){:target="_blank}.

إذا كان لديك حساب Trinket ، فيمكنك النقر فوق الزر **Remix** لحفظ نسخة في مكتبة `My Trinkets`.

--- /task ---

### Edit the sky

--- task ---

The starter project has some code already written for you.

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky.

![مستطيل أزرق حوله حدود سوداء وفوق مستطيل رمادي. The top left corner of the canvas is marked as x=0, y=0 this is the origin of the rectangle. The width is highlighted as 400 and the height as 250. The code rect(0, 0, 400, 250) is shown.](images/sky_stroke.png)no_stroke()   
fill(sky)   
rect(0, 0, 400, 250) #محور س, محور ص, العرض, الارتفاع

**Tip:** 💡 Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used.

--- /task ---

--- task ---

The sky has been drawn with a black border (stroke).

To turn the stroke off for all shapes add `no_stroke()` to the `setup` function:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 23
line_highlights: 25
---
def setup():
# Setup your game here
  size(400, 400) # width and height of screen frame_rate(2) no_stroke()

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لعرض الخلفية النهائية.

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png)دالة `size()` تستدعى في `setup()` يعين حجم الشاشة على 400 بكسل × 400 بكسل.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 26
---
def draw():
# Things to do in every frame
  global wood sky = color(92, 204, 206) # Red = 92, Green = 204, Blue = 206 grass = color(149, 212, 122) wood = color(145, 96, 51) outer = color(0, 120, 180)

  no_stroke()     
fill(sky)     
rect(0, 0, 400, 250) #محور س, محور ص, العرض, الارتفاع    
fill(grass)    
rect(0, 250, 400, 150)

--- /code ---

**Tip:** 💡 We have added comments to our code, like `# Set the fill color to grass`, to tell you what it does. You don't need to add these comments to your code, but they can be helpful to remind you what lines of code do.

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لعرض الخلفية النهائية.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="300px"}

--- /task ---

