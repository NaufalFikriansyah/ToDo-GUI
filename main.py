import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import ImageTk,Image


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
     'Mengecek peralatan operasional',
     'Melaksanakan pengamatan cuaca permukaan dengan alat konvensional',
     'Melaksanakan pengamatan cuaca permukaan dengan alat otomatis',
     'Melakukan pengolahan data tingkat dasar (MET REPORT, SPECI, MET REPORT, dan SPECIAL REPORT)',
     'Melaksanakan pengamatan udara atas (pibal) dengan alat theodolite pukul 06.00 UTC',
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
    'Melaksanakan pengamatan udara atas (pibal) dengan alat theodolite pukul 00.00 UTC',
    'Melaksanakan pengumpulan dan penyebaran data dengan menggunakan sistem internet/CMSS',
    'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan'
]
tugas_tambahan_pagi = []
tugas_tambahan_siang = []
tugas_tambahan_malam1 = []
tugas_tambahan_malam2 = []
# fungsi untuk membuat halaman dinas Pagi
def dinas_pagi_page():
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    def add_task():
        tugas= task_entry.get()
        list_tugas_pagi.append(str(tugas))
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(pagi_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center', 
                                           fg='Black', 
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    pagi_page = tk.Toplevel(root)
    pagi_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    

    tugas_checkbuttons = []
    for tugas in list_tugas_pagi:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(pagi_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons:
        checkbutton.config(command=lambda btn=checkbutton, v=var: toggle_color(btn, v))
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
        tugas_checkbutton_var = tk.StringVar()
        tugas_checkbutton = tk.Checkbutton(siang_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    siang_page = tk.Toplevel(root)
    siang_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    tugas_checkbuttons = []
    for tugas in list_tugas_siang:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(siang_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked"
                                           )
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons:
        checkbutton.config(command=lambda btn=checkbutton, v=var: toggle_color(btn, v))
    siang_page.title("Selamat Siang")
    submit_button = tk.Button(siang_page, text="Submit", command=submitted, font=("Helvetica", 20),relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(siang_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(siang_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')
# fungsi untuk membuat halaman dinas Malam1
def dinas_malam1_page():
    def add_task():
        tugas= task_entry.get()
        list_tugas_malam1.append(str(tugas))
        tugas_checkbutton_var = tk.StringVar()
        tugas_checkbutton = tk.Checkbutton(malam1_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
        
    malam1_page = tk.Toplevel(root)
    malam1_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    tugas_checkbuttons = []
    for tugas in list_tugas_malam1:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(malam1_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center',
                                           fg='Black',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons:
        checkbutton.config(command=lambda btn=checkbutton, v=var: toggle_color(btn, v))
    malam1_page.title("Selamat Malam")
    submit_button = tk.Button(malam1_page, text="Submit", command=submitted, font=("Helvetica", 20),relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(malam1_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(malam1_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')
# fungsi untuk membuat halaman dinas Malam2
def dinas_malam2_page():
    def add_task():
        tugas= task_entry.get()
        list_tugas_malam2.append(str(tugas))
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(malam2_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    malam2_page = tk.Toplevel(root)
    malam2_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    tugas_checkbuttons = []
    for tugas in list_tugas_malam2:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(malam2_page, 
                                           text=tugas, 
                                           font=("Helvetica", 18), 
                                           justify='center',
                                           fg='Black',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        #tugas_checkbuttons.append(tugas_checkbutton)
        tugas_checkbuttons.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons:
        checkbutton.config(command=lambda btn=checkbutton, v=var: toggle_color(btn, v))
    malam2_page.title("Selamat Malam")
    submit_button = tk.Button(malam2_page, 
                              text="Submit", 
                              command=submitted, 
                              font=("Helvetica", 20),
                              relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(malam2_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(malam2_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')
def submitted():
    submit_page = tk.Toplevel(root)
    submit_page.title("Tersubmit!")
    submit_label = tk.Label(submit_page, text="Tersubmit!", font=("Helvetica", 24))
    submit_label.pack(padx=10, pady=10)
    submit_page.after(3000, submit_page.destroy)
'''
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
            task_entry.delete(0, tk.END)  # Clear the input field'''
def handle_shift():
    selected_shift = cb2.get()
    if selected_shift == "Dinas Pagi":
        dinas_pagi_page()
    elif selected_shift == "Dinas Siang":
        dinas_siang_page()
    elif selected_shift == "Dinas Malam1":
        dinas_malam1_page()
    else: dinas_malam2_page()
    name.append(cb1)
    print(name)
    

# Create the main application window
root = customtkinter.CTk() 
root.title("Observer To Do App")
# Set the main window size to screen size
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

img1=ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
l1=customtkinter.CTkLabel(master=root,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=700, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root_label = customtkinter.CTkLabel(frame, text="Stasiun Meteorologi Sultan Muhammad Salahuddin", font=("Century Gothic", 20,"bold"), pady=100)
root_label.place(x=100, y=-10)

nama=['Idham','Jumratul Aida, S.Tr', 'Laksita Widomurti, S.Tr', 'Lavia Farareta, S.Tr','Ni Luh Jenitha Asdia Putri, S.Tr. Met','Ni Putu Andini Ganiswari, S.Tr','Suci Ainun Rimawati, S.Tr','Surya Tri Dharma Putra, S.Tr','Tri Wahyu, S.Tr. Met','Zulkurnain, S.Tr']
cb1 = customtkinter.CTkComboBox(master=frame, values=nama, width=220) # Combobox
cb1.set(' ') # default selected option
cb1.place(x=250, y=150)

shift=['Dinas Pagi','Dinas Siang','Dinas Malam1','Dinas Malam2'] # options
cb2 = customtkinter.CTkComboBox(master=frame, values=shift, width=220) # Combobox
cb2.set(' ') # default selected option
cb2.place(x=250, y=190)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=handle_shift, corner_radius=6)
button1.place(x=250, y=240)

# Start the Tkinter main loop
root.mainloop()