import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import ImageTk,Image
import pandas as pd
import datetime
#from win10toast import ToastNotifier
#from plyer import notification

#Text Bottons keluarkan

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
    'Melakukan pengisian logbook METAR/SPECI, Sinop, Udara Atas, Peralatan'
]
tugas_checkbuttons_pagi = []
tugas_checkbuttons_siang = []
tugas_checkbuttons_malam1 = []
tugas_checkbuttons_malam2 = []
# Define a DataFrame to store the tasks
tasks_df = pd.DataFrame(columns=["Shift", "Task"])
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
                                           font=("Helvetica", 20), 
                                           justify='center', 
                                           fg='Black', 
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_pagi.append((tugas_checkbutton, tugas_checkbutton_var))
    pagi_page = tk.Toplevel(root)
    pagi_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    

    for tugas in list_tugas_pagi:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(pagi_page, 
                                           text=tugas, 
                                           font=("Helvetica", 20), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_pagi.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons_pagi:
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
                                           font=("Helvetica", 20), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_siang.append((tugas_checkbutton, tugas_checkbutton_var))
    siang_page = tk.Toplevel(root)
    siang_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    
    for tugas in list_tugas_siang:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(siang_page, 
                                           text=tugas, 
                                           font=("Helvetica", 20), 
                                           justify='center',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked"
                                           )
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_siang.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons_siang:
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
                                           font=("Helvetica", 20), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_malam1.append((tugas_checkbutton, tugas_checkbutton_var))
        
    malam1_page = tk.Toplevel(root)
    malam1_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    
    for tugas in list_tugas_siang:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(malam1_page, 
                                           text=tugas, 
                                           font=("Helvetica", 20), 
                                           justify='center',
                                           fg='Black',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_malam1.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons_malam1:
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
                                           font=("Helvetica", 20), 
                                           justify='center', 
                                           fg='Black',
                                           variable=tugas_checkbutton_var, 
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        tugas_checkbuttons_malam2.append((tugas_checkbutton, tugas_checkbutton_var))
    malam2_page = tk.Toplevel(root)
    malam2_page.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    def toggle_color(checkbutton, var):
        if var.get() == "checked":
            checkbutton.config(fg="red")
        else:
            checkbutton.config(fg="black")
    
    for tugas in list_tugas_siang:
        tugas_checkbutton_var = tk.StringVar(value="unchecked")
        tugas_checkbutton = tk.Checkbutton(malam2_page, 
                                           text=tugas, 
                                           font=("Helvetica", 20), 
                                           justify='center',
                                           fg='Black',
                                           variable=tugas_checkbutton_var,
                                           onvalue="checked",
                                           offvalue="unchecked")
        tugas_checkbutton.pack(anchor='w')
        #tugas_checkbuttons.append(tugas_checkbutton)
        tugas_checkbuttons_malam2.append((tugas_checkbutton, tugas_checkbutton_var))
    # Attach the toggle_color function to each checkbutton
    for checkbutton, var in tugas_checkbuttons_malam2:
        checkbutton.config(command=lambda btn=checkbutton, v=var: toggle_color(btn, v))
    malam2_page.title("Selamat Malam")
    submit_button = tk.Button(malam2_page, 
                              text="Submit", 
                              command=save_to_excel, 
                              font=("Helvetica", 20),
                              relief="raised")
    submit_button.pack()

    # Create an input field and "Add Task" button
    task_entry = tk.Entry(malam2_page, font=("Helvetica", 14))
    task_entry.pack(anchor='w')

    add_task_button = tk.Button(malam2_page, text="Add Task", command=add_task)
    add_task_button.pack(anchor='w')
def submitted():
    '''
    # Show a toast notification when the data is saved
    toast_message = f"Submitted"
    notification.notify(
        title="Task Report",
        message=toast_message,
        app_name="YourApp",
    )
    #toast_message = f"Tasks saved to '{excel_file_name}'"
    #toaster.show_toast("Task Report", toast_message, duration=10)
    '''
    submit_page = tk.Toplevel(root)
    submit_page.title("Tersubmit (contoh)")
    submit_label = tk.Label(submit_page, text="Tersubmit (contoh)", font=("Helvetica", 24))
    submit_label.pack(padx=10, pady=10)
    submit_page.after(3000, submit_page.destroy)
def handle_shift():
    selected_shift = cb1.get()
    if selected_shift == "Dinas Pagi":
        dinas_pagi_page()
    elif selected_shift == "Dinas Siang":
        dinas_siang_page()
    elif selected_shift == "Dinas Malam1":
        dinas_malam1_page()
    else: dinas_malam2_page()
    name.append(entry1)
    print(name)

def save_to_excel():
    global tasks_df
    tasks_df = pd.DataFrame(columns=["Shift","Name", "Task"])
    for checkbutton, name, var in tugas_checkbuttons_pagi:
        task = checkbutton.cget("text")
        state = var.get()
        if state == "checked":
            shift = cb1.get()
            tasks_df = tasks_df.append({"Shift": shift,"Name":name, "Task": task}, ignore_index=True)

    ## Get the current local date and time
    local_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Generate the Excel file name with the local date
    excel_file_name = f"report_{local_date}.xlsx"

    # Save the DataFrame to the Excel file
    tasks_df.to_excel(excel_file_name, index=False)
    print(f"Tasks saved to '{excel_file_name}'")
    

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

root_label = customtkinter.CTkLabel(frame, text="Stasiun Meteorologi Sultan Muhammad Salahuddin", font=("Century Gothic", 20), pady=100)
root_label.place(x=100, y=-10)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nama')
entry1.place(x=250, y=180)
name = []

shift=['Dinas Pagi','Dinas Siang','Dinas Malam1','Dinas Malam2'] # options
cb1 = customtkinter.CTkComboBox(master=frame, values=shift, width=220) # Combobox
cb1.set('Dinas Pagi') # default selected option
cb1.place(x=250, y=205)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=handle_shift, corner_radius=6)
button1.place(x=250, y=240)

# Start the Tkinter main loop
root.mainloop()