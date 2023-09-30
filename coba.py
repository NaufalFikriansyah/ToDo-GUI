import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
import pandas as pd
import datetime
list_tugas_pagi = [
     'Menyiapkan bahan dan peralatan untuk pengamatan',
     'Mengecek peralatan operasional',
     'Mengganti pias Hellman & Barograph harian',
     'Melaksanakan pengamatan cuaca permukaan dengan alat konvensional',
     'Melaksanakan pengamatan cuaca permukaan dengan alat otomatis',
     'Membuat WXREV',
     'Melakukan pengolahan data tingkat dasar (MET REPORT, SPECI, MET REPORT, dan SPECIAL REPORT)',
     'Melaksanakan pengamatan udara atas (pibal) dengan alat tehodolite pukul 06.00 UTC',
     'Melaksanakan pengumpulan dan penyebaran data dengan menggunakan sistem internet/CMSS',
     'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan',
]
list_tugas_siang = [
    'Menyiapkan bahan dan peralatan untuk pengamatan',
     'Mengecek peralatan operasional',
     'Melaksanakan pengamatan cuaca permukaan dengan alat konvensional',
     'Melaksanakan pengamatan cuaca permukaan dengan alat otomatis',
     'Melakukan pengolahan data tingkat dasar (MET REPORT, SPECI, MET REPORT, dan SPECIAL REPORT)',
     'Melaksanakan pengamatan udara atas (pibal) dengan alat tehodolite pukul 06.00 UTC',
     'Melaksanakan pengumpulan dan penyebaran data dengan menggunakan sistem internet/CMSS',
     'Mengganti pias Camble Stokes',
     'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan'
     ]
list_tugas_malam1 = [
    'Menyiapkan bahan dan peralatan untuk pengamatan',
    'Mengecek peralatan operasional',
    'Melaksanakan pengamatan cuaca permukaan dengan alat konvensional',
    'Melaksanakan pengamatan cuaca permukaan dengan alat otomatis',
    'Melakukan pengolahan data tingkat dasar (MET REPORT, SPECI)',
    'Melaksanakan pengumpulan dan penyebaran data dengan menggunakan sistem internet/CMSS',
    'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan'
]
list_tugas_malam2 = [
    'Menyiapkan bahan dan peralatan untuk pengamatan',
    'Mengecek peralatan operasional',
    'Melaksanakan pengamatan cuaca permukaan dengan alat konvensional',
    'Melaksanakan pengamatan cuaca permukaan dengan alat otomatis',
    'Melakukan pengolahan data tingkat dasar (MET REPORT, SPECI, MET REPORT, dan SPECIAL REPORT)',
    'Melaksanakan pengamatan udara atas (pibal) dengan alat tehodolite pukul 00.00 UTC',
    'Melaksanakan pengumpulan dan penyebaran data dengan menggunakan sistem internet/CMSS',
    'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan']

tugas_checkbuttons_pagi = []
tugas_checkbuttons_siang = []
tugas_checkbuttons_malam1 = []
tugas_checkbuttons_malam2 = []

shift_tasks = {
    "Dinas Pagi": list_tugas_pagi,
    "Dinas Siang": list_tugas_siang,
    "Dinas Malam1": list_tugas_malam1,
    "Dinas Malam2": list_tugas_malam2,
}

tasks_df = pd.DataFrame(columns=["Shift", "Name", "Task"])

def update_task_list(shift_name, checkbutton_list):
    for checkbutton, var in checkbutton_list:
        checkbutton.destroy()

    for task in shift_tasks[shift_name]:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(
            root,
            text=task,
            font=("Helvetica", 20),
            justify='center',
            fg='Black',
            variable=tugas_checkbutton_var,
            onvalue="checked",
            offvalue="unchecked"
        )
        tugas_checkbutton.pack(anchor='w')
        checkbutton_list.append((tugas_checkbutton, tugas_checkbutton_var))

def dinas_page(shift_name, checkbutton_list):
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")

    def add_task():
        tugas = task_entry.get()
        shift_tasks[shift_name].append(str(tugas))
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(
            dinas_window,
            text=tugas,
            font=("Helvetica", 20),
            justify='center',
            fg='Black',
            variable=tugas_checkbutton_var,
            onvalue="checked",
            offvalue="unchecked"
        )
        tugas_checkbutton.pack(anchor='w')
        checkbutton_list.append((tugas_checkbutton, tugas_checkbutton_var))

    dinas_window = tk.Toplevel(root)
    dinas_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    for tugas in shift_tasks[shift_name]:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(
            dinas_window,
            text=tugas,
            font=("Helvetica", 20),
            justify='center',
            fg='Black',
            variable=tugas_checkbutton_var,
            onvalue="checked",
            offvalue="unchecked"
        )
        tugas_checkbutton.pack(anchor='w')
        checkbutton_list.append((tugas_checkbutton, tugas_checkbutton_var))

    for checkbutton, var in checkbutton_list:
        checkbutton.config(command=lambda btn=checkbutton, v=var: toggle_color(btn, v))

    dinas_window.title(f"Selamat {shift_name}")
    submit_button = tk.Button(dinas_window, text="Submit", command=submitted, font=("Helvetica", 20), relief="raised")
    submit_button.pack()

    task_entry = tk.Entry(dinas_window, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(dinas_window, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')

def submitted():
    submit_page = tk.Toplevel(root)
    submit_page.title("Tersubmit (contoh)")
    submit_label = tk.Label(submit_page, text="Tersubmit (contoh)", font=("Helvetica", 24))
    submit_label.pack(padx=10, pady=10)
    submit_page.after(3000, submit_page.destroy)

root = tk.Tk()
root.title("Observer To Do App")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
l1 = tk.Label(master=root, image=img1)
l1.pack()

frame = tk.Frame(master=l1, width=700, height=360)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root_label = tk.Label(frame, text="Stasiun Meteorologi Sultan Muhammad Salahuddin", font=("Century Gothic", 20), pady=100)
root_label.place(x=100, y=-10)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nama')
entry1.place(x=250, y=180)

shift = ['Dinas Pagi', 'Dinas Siang', 'Dinas Malam1', 'Dinas Malam2']
cb1 = customtkinter.CTkComboBox(master=frame, values=shift, width=220)
cb1.set('Dinas Pagi')
cb1.place(x=250, y=205)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=lambda: dinas_page(cb1.get(), tugas_checkbuttons_pagi), corner_radius=6)
button1.place(x=250, y=240)

root.mainloop()
