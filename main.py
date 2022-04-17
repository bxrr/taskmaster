# uses calendar.py module and displays windows/tasks
# task manager = 250 pixels wide
from graphics import *
from calendar import *
import ctypes

# sets taskbar icon to logo
ctypes.windll
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("icon")


redraw = True


#initialization
TEXT = color_rgb(15, 15, 15)
BASE = color_rgb(5, 102, 141)
HEADER = color_rgb(255, 255, 255)
MONTHS = color_rgb(15, 15, 15)
EVENTS = color_rgb(2, 128, 144)
OUTLINES = color_rgb(15, 15, 15)
FONT = 'montserrat'


#graphics 
win = GraphWin("Task Master", 1500,900)
win.setBackground(HEADER)

def draw_grid():
    
    shift = get_first_DOW()
    for i in range(1,6):
        for j in range(1,8):
            if ((i - 1) * 7 + j - shift > 0 and (i - 1) * 7 + j - shift <= get_display_date()[4]):
                txt = Text(Point((j*1250/7) + 1250/14, (i*144) + 64), (i - 1) * 7 + j - shift)
                txt.setTextColor(TEXT)
                txt.setSize(10)
                txt.setFace(FONT)
                txt.draw(win)
                task = Entry(Point((j*1250/7) + 160, (i*144) + 110), 15)
                task.setFill(color_rgb(240, 243, 189))
                task.draw(win)

    for i in range(1,6):
        p1 = Point(250,(i*144)+180)
        p2 = Point(1500,(i*144)+180)
        ln = Line(p1,p2)
        ln.setOutline(OUTLINES)
        ln.setWidth(3)
        ln.draw(win)
    
    for i in range(1,8):
        p1 = Point((i*1250/7)+250, 180)
        p2 = Point((i*1250/7)+250, 900)
        ln = Line(p1,p2)
        ln.setOutline(OUTLINES)
        ln.setWidth(3)
        ln.draw(win)

    rect = Rectangle(Point(250,180), Point(1499,899))
    rect.setOutline(OUTLINES)
    rect.setWidth(3)
    rect.draw(win)
     
def draw_month():
    rect = Rectangle(Point(250,180),Point(1500,0))
    rect.setFill(BASE)
    rect.draw(win)
    txt = Text(Point(875, 90), get_display_date()[1] + " " + str(get_display_date()[2]))
    txt.setTextColor(HEADER)
    txt.setSize(30)
    txt.setFace(FONT)
    txt.draw(win)


def draw_days():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    rect = Rectangle(Point(250,150),Point(1500,180))
    rect.setWidth(3)
    rect.setOutline(OUTLINES)
    rect.setFill(MONTHS)
    rect.draw(win)

    for i in range(1,8):
        day = Text(Point((i*1250/7) + 250 - 1250/14, 165),days[i-1])
        day.setTextColor(HEADER)
        day.setFace(FONT)
        day.setSize(15)
        day.draw(win)

def draw_tasks():
    rect = Rectangle(Point(0,0), Point(250, 900))
    rect.setFill(EVENTS)
    rect.setOutline(OUTLINES)
    rect.setWidth(3)
    rect.draw(win)

    title = Text(Point(125,50), "Next 30 Days")
    title.setTextColor(HEADER)
    title.setSize(25)
    title.setFace(FONT)
    title.draw(win)


    

def draw_arrows():
    arrows = Text(Point(1400, 50), "<   >")
    arrows.setTextColor(HEADER)
    arrows.setSize(25)
    arrows.draw(win)
    

def check_mouse():
    global redraw
    x_click = win.getMouse().getX()
    y_click = win.getMouse().getY()
    if (1370 <= x_click <= 1390 and 35 <= y_click <= 65):
        decr_month()
        redraw = True
        print("it got here ")
    if (1410 <= x_click <= 1430 and 35 <= y_click <= 65):
        incr_month()
        redraw = True


while(True):
    if(redraw):
        win.undraw()
        draw_grid()
        draw_month()
        draw_days()
        draw_tasks()
        draw_arrows()
        win.update()
        redraw = False
    check_mouse()
    
