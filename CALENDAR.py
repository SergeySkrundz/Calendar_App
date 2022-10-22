from tkinter import *
import calendar
import datetime
from PIL import ImageTk

import locale
locale.setlocale(locale.LC_ALL, '')


def back():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()

def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()

def fill():
    info_label['text'] = calendar.month_name[month] + ' ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    info_label['bg'] = '#1D1E33'
    if month == 1:
        back_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        back_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]



    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = '#ffffff'
        if calendar.weekday(year, month, n+1) == 5 or calendar.weekday(year, month, n+1) == 6:
            days[n + week_day]['fg'] = '#e50036'

        if (month == 1 and days[n + week_day]['text'] == 1) or (month == 1 and days[n + week_day]['text'] == 7) or \
                (month == 3 and days[n + week_day]['text'] == 8) or (month == 5 and days[n + week_day]['text'] == 1) or \
                (month == 5 and days[n + week_day]['text'] == 9) or (month == 7 and days[n + week_day]['text'] == 3) or \
                (month == 11 and days[n + week_day]['text'] == 7) or (month == 12 and days[n + week_day]['text'] == 25):
            days[n + week_day]['fg'] = '#e50036'

        if year == now.year and month == now.month and n == now.day:
            days[n+week_day-1]['bg'] = '#00FFFF'
            days[n + week_day - 1]['fg'] = '#1D1E33'
            days[n + week_day]['bg'] = '#1D1E33'
        else:
            days[n + week_day]['bg'] = '#1D1E33'

    for n in range(week_day):
        days[week_day - n - 1]['text'] = back_month_days - n
        days[week_day - n - 1]['fg'] = '#474747'
        days[week_day - n - 1]['bg'] = '#1D1E33'

    for n in range(6 * 7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n + 1
        days[week_day + month_days + n]['fg'] = '#474747'
        days[week_day + month_days + n]['bg'] = '#1D1E33'

root = Tk()
root.geometry('406x436')
root.resizable(width=0, height=0)
root.configure(background='#1D1E33')
root.title('Календарь')
days = []
now = datetime.datetime.now()
year = now.year
month = now.month

image_back_button = ImageTk.PhotoImage(file="img\img_left.png")
back_button = Button(root, image=image_back_button, command=back, relief='flat', bg='#1D1E33', activebackground='#1D1E33')
back_button.grid(row=0, column=5, sticky=NSEW)

image_next_button = ImageTk.PhotoImage(file="img\img_right.png")
next_button = Button(root, image=image_next_button, command=next, relief='flat', bg='#1D1E33', activebackground='#1D1E33')
next_button.grid(row=0, column=6, sticky=NSEW)

info_label = Label(root, text='0', anchor='w', width=1, height=2, font='Arial 20 bold', fg='#ffffff')
info_label.grid(row=0, column=0, columnspan=5, padx=(10, 0), sticky=NSEW)

for n in range(7):
    if n == 5 or n == 6:
        lbl = Label(root, text=calendar.day_abbr[n], anchor='center', width=1, height=1, font='Arial 12 bold', fg='#e50036', bg='#1D1E33')
        lbl.grid(row=1, column=n, pady=(0, 5), sticky=NSEW)
    else:
        lbl = Label(root, text=calendar.day_abbr[n], anchor='center', width=1, height=1, font='Arial 12 bold', fg='grey', bg='#1D1E33')
        lbl.grid(row=1, column=n, pady=(0, 5), sticky=NSEW)

for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2, font='Arial 16 bold')
        lbl.grid(row=row+2, column=col, sticky=NSEW)
        days.append(lbl)

fill()

root.mainloop()