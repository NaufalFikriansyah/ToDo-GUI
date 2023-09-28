import tkinter as tk
from tkinter import ttk

#BIKIN KOLOM NAMA
#BIKIN ALGORITMA EXCEL
#BIKIN SQL

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
     'Mengecek peralatan operasional'
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
    'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan'
]

# fungsi untuk membuat halaman dinas Pagi
def dinas_pagi_page():
    def add_task():
        tugas= task_entry.get()
        list_tugas_pagi.append(str(tugas))
        tugas_checkbutton = tk.Checkbutton(pagi_page, text=tugas, font=("Helvetica", 20), justify='center', fg='Blue')
        tugas_checkbutton.pack(anchor='w')
    
    pagi_page = tk.Toplevel(root)
    pagi_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    obs_name = []
    tugas_checkbuttons = []
    for tugas in list_tugas_pagi:
        tugas_checkbutton = tk.Checkbutton(pagi_page, text=tugas, font=("Helvetica", 20), justify='center')
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append(tugas_checkbutton)
    pagi_page.title("Selamat Pagi")
    submit_button = tk.Button(pagi_page, text="Submit", command=submitted, font=("Helvetica", 20),relief="raised")
    submit_button.pack()
    # Create an input field and "Add Task" button
    task_entry = tk.Entry(pagi_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')
    add_task_button = tk.Button(pagi_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')


# fungsi untuk membuat halaman dinas Siang
def dinas_siang_page():
    def add_task():
        tugas= task_entry.get()
        list_tugas_siang.append(str(tugas))
        tugas_checkbutton = tk.Checkbutton(siang_page, text=tugas, font=("Helvetica", 20), justify='center', fg='Blue')
        tugas_checkbutton.pack(anchor='w')
    siang_page = tk.Toplevel(root)
    siang_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    tugas_checkbuttons = []
    for tugas in list_tugas_siang:
        tugas_checkbutton = tk.Checkbutton(siang_page, text=tugas, font=("Helvetica", 20), justify='center')
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append(tugas_checkbutton)
    siang_page.title("Selamat Siang")
    submit_button = tk.Button(siang_page, text="Submit", command=submitted, font=("Helvetica", 20),relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(siang_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(siang_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')
    
    
# fungsi untuk membuat halaman dinas Malam
def dinas_malam1_page():
    def add_task():
        tugas= task_entry.get()
        list_tugas_malam1.append(str(tugas))
        tugas_checkbutton = tk.Checkbutton(malam1_page, text=tugas, font=("Helvetica", 20), justify='center', fg='Blue')
        tugas_checkbutton.pack(anchor='w')
    malam1_page = tk.Toplevel(root)
    malam1_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    tugas_checkbuttons = []
    for tugas in list_tugas_siang:
        tugas_checkbutton = tk.Checkbutton(malam1_page, text=tugas, font=("Helvetica", 20), justify='center')
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append(tugas_checkbutton)
    malam1_page.title("Selamat Siang")
    submit_button = tk.Button(malam1_page, text="Submit", command=submitted, font=("Helvetica", 20),relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(malam1_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(malam1_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')

def dinas_malam2_page():
    def add_task():
        tugas= task_entry.get()
        list_tugas_malam2.append(str(tugas))
        tugas_checkbutton = tk.Checkbutton(malam2_page, text=tugas, font=("Helvetica", 20), justify='center', fg='Blue')
        tugas_checkbutton.pack(anchor='w')
    malam2_page = tk.Toplevel(root)
    malam2_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    tugas_checkbuttons = []
    for tugas in list_tugas_siang:
        tugas_checkbutton = tk.Checkbutton(malam2_page, text=tugas, font=("Helvetica", 20), justify='center')
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append(tugas_checkbutton)
    malam2_page.title("Selamat Siang")
    submit_button = tk.Button(malam2_page, text="Submit", command=submitted, font=("Helvetica", 20),relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(malam2_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(malam2_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')

def submitted():
    submit_page = tk.Toplevel(root)
    submit_page.title("Tersubmit (contoh)")
    submit_label = tk.Label(submit_page, text="Tersubmit (contoh)", font=("Helvetica", 24))
    submit_label.pack(padx=10, pady=10)
    submit_page.after(3000, submit_page.destroy)

def add_task():
    addTask_page = tk.Toplevel(root)
    addTask_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    # Create an input field and "Add Task" button
    task_entry = tk.Entry(addTask_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')
    task = task_entry.get()
    tugas_checkbuttons=[]
    if task:
            new_task_checkbutton = tk.Checkbutton(selected_page, text=task, font=("Helvetica", 14))
            new_task_checkbutton.pack(anchor='w')
            tugas_checkbuttons.append(new_task_checkbutton)
            task_entry.delete(0, tk.END)  # Clear the input field
    
# Create the main application window
root = tk.Tk()
root.title("Observer To Do App")
# Set the main window size to screen size
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

root_label = tk.Label(root, text="STASIUN METEOROLOGI SULTAN MUHAMMAD SALAHUDDIN", font=("Helvetica", 34), pady=100)
root_label.pack()
root1_label = tk.Label(root, text="Pilih Jadwal Dinas", font=("Helvetica", 10), pady=50)
root1_label.pack()
# Create Morning and Night buttons
dinas_pagi_button = tk.Button(root, text="Pagi", command=dinas_pagi_page, font=("Helvetica", 20),relief="raised")
dinas_siang_button = tk.Button(root, text="Siang", command=dinas_siang_page, font=("Helvetica", 20),relief="raised")
dinas_malam1_button = tk.Button(root, text="Malam 1", command=dinas_malam1_page, font=("Helvetica", 20),relief="raised")
dinas_malam2_button = tk.Button(root, text="Malam 2", command=dinas_malam2_page, font=("Helvetica", 20),relief="raised")

# Pack the buttons in the main window
dinas_pagi_button.pack()
dinas_siang_button.pack()
dinas_malam1_button.pack()
dinas_malam2_button.pack()

# Start the Tkinter main loop
root.mainloop()