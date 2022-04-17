# uses calendar.py module and displays windows/tasks
# task manager = 250 pixels wide
import ctypes

from calendar import *
import pickle
from graphics import *





#initialization 
TEXT = color_rgb(15, 15, 15)
BASE = color_rgb(5, 102, 141)
HEADER = color_rgb(255, 255, 255)
MONTHS = color_rgb(15, 15, 15)
EVENTS = color_rgb(2, 128, 144)
OUTLINES = color_rgb(15, 15, 15)
FONT = 'montserrat'

# sets taskbar icon to logo
ctypes.windll
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("icon")

# globals
tasks = []
# tasks[i].get_date() -> [day, month, year]

redraw = True
# calendar imports: 
# cur_time
# display_day
# display_month
# display_year
# display_wday
# + functions

# extra stuff to add: time in .get_date(), make window size changeable, feature to scroll through tasks

#graphics & data handling ===============
win = GraphWin("Task Master", 1500, 900)
win.setBackground(HEADER)


temp_tasks = []
def draw_grid():
    global temp_tasks
    temp_tasks = []

    shift = get_first_DOW()
    count = 0
    for i in range(1,6):
        for j in range(1,8):
            if ((i - 1) * 7 + j - shift > 0 and (i - 1) * 7 + j - shift <= get_display_date()[4]):
                txt = Text(Point((j*1150/7) + 1150/14 + 130, (i*144) + 64), (i - 1) * 7 + j - shift)
                txt.setTextColor(TEXT)
                txt.setSize(10)
                txt.setFace(FONT)
                txt.draw(win)

                # text boxes
                temp_tasks.append(Entry(Point((j*1150/7) + 350 - 1140/14, (i*144) + 110), 15))
                temp_tasks[count].setFill(color_rgb(240, 243, 189))
                temp_tasks[count].draw(win)
                count += 1

    for i in range(1,6):
        p1 = Point(350,(i*144)+180)
        p2 = Point(1500,(i*144)+180)
        ln = Line(p1,p2)
        ln.setOutline(OUTLINES)
        ln.setWidth(3)
        ln.draw(win)
    
    for i in range(1,8):
        p1 = Point((i*1150/7)+350, 180)
        p2 = Point((i*1150/7)+350, 900)
        ln = Line(p1,p2)
        ln.setOutline(OUTLINES)
        ln.setWidth(3)
        ln.draw(win)

    rect = Rectangle(Point(350,180), Point(1499,899))
    rect.setOutline(OUTLINES)
    rect.setWidth(3)
    rect.draw(win)
     
def draw_month():
    rect = Rectangle(Point(350,180),Point(1500,0))
    rect.setFill(BASE)
    rect.draw(win)
    txt = Text(Point(875, 90), get_display_date()[1] + " " + str(get_display_date()[2]))
    txt.setTextColor(HEADER)
    txt.setSize(30)
    txt.setFace(FONT)
    txt.draw(win)

def draw_days():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    rect = Rectangle(Point(350,150),Point(1500,180))
    rect.setWidth(3)
    rect.setOutline(OUTLINES)
    rect.setFill(MONTHS)
    rect.draw(win)

    for i in range(1,8):
        day = Text(Point((i*1150/7) + 350 - 1150/14, 165),days[i-1])
        day.setTextColor(HEADER)
        day.setFace(FONT)
        day.setSize(15)
        day.draw(win)

def sort_date(date):
    return date[2] * 99999 + date[1] * 33 + date[0]

def sort_key(task):
    date = task.get_date()
    return sort_date(date)

def draw_tasks():
    global tasks
    rect = Rectangle(Point(0,0), Point(350, 900))
    rect.setFill(EVENTS)
    rect.setOutline(OUTLINES)
    rect.setWidth(3)
    rect.draw(win)

    title = Text(Point(175,40), "Tasks")
    title.setTextColor(HEADER)
    title.setSize(22)
    title.setFace(FONT)
    title.draw(win)
    
    # adding user input
    tasks.sort(key=sort_key)        

def draw_arrows():
    arrows = Text(Point(1400, 50), "<   >")
    arrows.setTextColor(HEADER)
    arrows.setSize(25)
    arrows.draw(win)

def check_mouse():
    global redraw
    click = win.checkMouse()
    if click != None:
        x_click = click.getX()
        y_click = click.getY()
        if (1370 <= x_click <= 1390 and 35 <= y_click <= 65):
            decr_month()
            redraw = True
        if (1410 <= x_click <= 1430 and 35 <= y_click <= 65):
            incr_month()
            redraw = True

def check_save_tasks(): 
    global redraw
    if(win.checkKey().lower() == "return"):
        for i in range(len(temp_tasks)):
            text = temp_tasks[i].getText()
            if text != "" and sort_date(update_cur()) <= sort_date([i+1, get_display_date()[5], get_display_date()[2]]):
                tasks.append(Task(text, [i+1, get_display_date()[5], get_display_date()[2]]))
        

        with open("tasks/data", "wb") as f:
            pickle.dump(tasks, f)
            
        
        redraw = True

def display_tasks():
    global tasks
    if len(tasks) != 0:
        for i in range (len(tasks)):
            txt = Text(Point(175, 75 + i*30), (str(tasks[i].get_date()[1]) + '/' + str(tasks[i].get_date()[0]) + '/' +  str(tasks[i].get_date()[2]) + ': ' + tasks[i].get_name()))
            txt.setTextColor('white')
            txt.setFace(FONT)
            txt.setSize(13)
            txt.draw(win)

def load_tasks():
    global tasks
    try:
        with open("tasks/data", "rb") as f:
            tasks = pickle.load(f)
    except:
        print("No data file found.")

# control loop 
def main():
    load_tasks()
    global redraw
    while(True):
        if(redraw):
            win.undraw()
            draw_grid()
            draw_month()
            draw_days()
            draw_tasks()
            draw_arrows()
            display_tasks()
            win.update()
            
            redraw = False
            for task in tasks:
                print(task.get_date())
        check_mouse()
        check_save_tasks()

if __name__ == "__main__":
    main()
