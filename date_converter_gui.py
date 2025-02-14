from tkinter import *
from tkinter import messagebox
from datetime import datetime
import jdatetime
from convertdate import islamic, persian, gregorian

# Function to show current calendars
def show_calendars():
    gregorian_date = datetime.now()
    persian_date = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
    islamic_date = islamic.from_gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day)

    result = (
        f"Today: {persian_date.strftime('%A')}\n"
        f"Persian Date: {persian_date.strftime('%Y/%m/%d')}\n"
        f"Gregorian Date: {gregorian_date.strftime('%Y/%m/%d')}\n"
        f"Islamic Date: {islamic_date[0]}/{islamic_date[1]}/{islamic_date[2]}\n"
        f"Time: {persian_date.strftime('%H:%M:%S')}"
    )
    messagebox.showinfo("Current Calendars", result)

# Function to convert Solar Hijri to Gregorian
def solar_to_gregorian():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        g_date = gregorian.from_jd(persian.to_jd(year, month, day))
        result = f"Gregorian Date: {g_date[0]}-{g_date[1]:02d}-{g_date[2]:02d}"
        messagebox.showinfo("Conversion Result", result)
    except:
        messagebox.showerror("Error", "Invalid Solar Hijri Date")

# Function to convert Gregorian to Solar Hijri
def gregorian_to_solar():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        p_date = persian.from_jd(gregorian.to_jd(year, month, day))
        result = f"Solar Hijri Date: {p_date[0]}-{p_date[1]:02d}-{p_date[2]:02d}"
        messagebox.showinfo("Conversion Result", result)
    except:
        messagebox.showerror("Error", "Invalid Gregorian Date")

# Function to convert Gregorian to Islamic
def gregorian_to_islamic():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        islamic_date = islamic.from_gregorian(year, month, day)
        result = f"Islamic Date: {islamic_date[0]}/{islamic_date[1]}/{islamic_date[2]}"
        messagebox.showinfo("Conversion Result", result)
    except:
        messagebox.showerror("Error", "Invalid Gregorian Date")

# GUI Layout
root = Tk()
root.title("Date Converter - Pejman Morovat")
root.geometry("400x400")

label_title = Label(root, text="Date Converter Program", font=("Arial", 18, "bold"))
label_title.pack(pady=10)

label_author = Label(root, text="Author: Pejman Morovat", font=("Arial", 12, "italic"))
label_author.pack(pady=5)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Year:").grid(row=0, column=0, padx=5, pady=5)
entry_year = Entry(frame)
entry_year.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Month:").grid(row=1, column=0, padx=5, pady=5)
entry_month = Entry(frame)
entry_month.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Day:").grid(row=2, column=0, padx=5, pady=5)
entry_day = Entry(frame)
entry_day.grid(row=2, column=1, padx=5, pady=5)

btn_show_calendars = Button(root, text="Show Current Calendars", command=show_calendars, bg="skyblue")
btn_show_calendars.pack(pady=5)

btn_solar_to_gregorian = Button(root, text="Solar Hijri to Gregorian", command=solar_to_gregorian, bg="lightgreen")
btn_solar_to_gregorian.pack(pady=5)

btn_gregorian_to_solar = Button(root, text="Gregorian to Solar Hijri", command=gregorian_to_solar, bg="lightblue")
btn_gregorian_to_solar.pack(pady=5)

btn_gregorian_to_islamic = Button(root, text="Gregorian to Islamic", command=gregorian_to_islamic, bg="lightcoral")
btn_gregorian_to_islamic.pack(pady=5)

btn_exit = Button(root, text="Exit", command=root.quit, bg="red", fg="white")
btn_exit.pack(pady=10)

root.mainloop()
