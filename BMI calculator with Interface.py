def BMIres(x):
    if x >= 30:
        res = 'Obesity : Danger'
    elif 30 > x > 25:
        res = 'Overweight : Caution'
    elif 25 > x > 18.5:
        res = 'Healthy Weight : Normal'
    else:
        res = 'Underweight : Caution'
    return res

import tkinter as tk

win = tk.Tk()
win.title('Body Mass Index Calculator : ')

canvas1 = tk.Canvas(win, width=400, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(win, text='Calculate using Weight and Height')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(win, text='Weight (KGS)  :')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 110, window=label2)

label3 = tk.Label(win, text='Height (CMS)  :')
label3.config(font=('helvetica', 10))
canvas1.create_window(100, 140, window=label3)

entry1 = tk.Entry(win)
canvas1.create_window(220, 110, window=entry1)

entry2 = tk.Entry(win)
canvas1.create_window(220, 140, window=entry2)

entry3 = tk.Entry(win)
canvas1.create_window(220,170,window=entry3)

def getBMI():

    x1 = entry1.get()
    x2 = entry2.get()

    label4 = tk.Label(win, text='The BMI is:', font=('helvetica', 10))
    canvas1.create_window(200, 230, window=label4)

    BMI = (float(x1) / float(x2) ** 2) * 10000

    label5 = tk.Label(win, text=BMI, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 250, window=label5)

    BMIstats = BMIres(BMI)

    label6 = tk.Label(win, text=BMIstats, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 280, window=label6)

button1 = tk.Button(text='     Male    ', command=getBMI, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 210, window=button1)

win.mainloop()
