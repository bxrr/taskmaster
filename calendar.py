# calendar logic & functions

import time

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# time data + class
cur_time = time.localtime()
display_day = cur_time.tm_mday
display_month = cur_time.tm_mon
display_year = cur_time.tm_year
display_wday = cur_time.tm_wday

def incr_month():
    global display_month
    global display_year
    global display_day
    global display_wday

    display_month += 1
    display_day = 1
    if display_month > 12:
        display_year += 1
        display_month %= 12
    print(display_month)

    for i in range(display_day + 1, MONTH_LENGTHS[display_month-2] + 1):
        display_wday = display_wday + 1
        if (display_wday == 7):
            display_wday = 0
            
def decr_month():
    global display_month
    global display_year
    global display_day
    global display_wday
    
    display_month -= 1
    display_day = 1
    if display_month < 1:
        display_year -= 1
        display_month = 12 - display_month
    print(display_month)
    

    for i in range(1, MONTH_LENGTHS[display_month-1] + 1 + display_day):
        display_wday = display_wday - 1
        if (display_wday == -1):
            display_wday = 6

def update_cur():
    cur_time = time.localtime()
    return [cur_time.tm_mday, cur_time.tm_mon, cur_time.tm_year, cur_time.tm_wday]

def get_display_date():
    print(display_wday)
    return [display_day, MONTHS[display_month-1], display_year, WEEKDAYS[display_wday], MONTH_LENGTHS[display_month-1]]

def get_first_DOW():
    w = display_wday
    for i in range(2,display_day):
        w = w - 1
        if (w == -1):
            w = 6
    return w

    

# task data + class
tasks = []
class Task:
    def __init__(self, name, date, desc=""):
        self.name = name
        self.date = date # put date in the format of 
        self.desc = desc

    def update(self, new_name="", new_date=[], new_desc=""):
        self.name = new_name if new_name != "" else self.name
        self.date = new_date if new_date != [] else self.date
        self.desc = new_desc if new_desc != "" else self.desc
    
    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc