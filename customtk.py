import tkinter as tk
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")  


app = customtkinter.CTk()  #creating custom tkinter window
app.geometry("600x440")
app.title("Observer")



def button_function():
    app.destroy()            # destroy current window and creating new one 
    w = customtkinter.CTk()
    w.geometry("900x400")
    w.title('My To Do List')
    l1=customtkinter.CTkLabel(master=w, text="Sta. Met. Sultan Muhammad Salahuddin To Do List",
                              font=('Times',20,'bold','underline'))
    l1.grid(row=0,column=1,padx=5,pady=10)

    f_done=('Times',16,'overstrike')
    f_normal=('Times',16,'normal')

    def my_upd(k): # k is the key of the reference dictionary 
        if(my_ref[k][1].get()==True): # checkbox is checked 
            my_ref[k][0].config(font=f_done,fg='red')
        else: # Checkbox is unchecked
            my_ref[k][0].config(font=f_normal,fg='black')
     
    my_dict={'a':'My Task No 1','b':'My Task No 2','c':'My Task No 3'}
    my_ref={} # Storing the references 
    i=2 # row number ( after using 0 row number for Label at top)

    def add_task():
            tugastambahan=task_entry.get()
            task_entry=tk.entry(font=f_normal,fg='black')
            task_entry.pack(anchor='w')
            add_task_button=tk.Button(master=w, text="Add Task", command=add_task)
            add_task_button.pack(anchor='w')
    
    for k in my_dict.keys(): # Number of checkbuttons or tasks 
        var=tk.BooleanVar() # variable connected to Checkbutton 
        ck = tk.Checkbutton(master=w, text=my_dict[k], 
        variable=var,onvalue=True,offvalue=False,font=f_normal,fg='black',
        command=lambda k=k: my_upd(k))
        ck.grid(row=i,column=0,padx=80,pady=5,sticky='e') 

        my_ref[k]=[ck,var] # to hold the references 
        i=i+1 # increase the row number


    w.mainloop()
    


img1=ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Welcome!",font=('Century Gothic',20))
l2.place(x=110, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nama')
entry1.place(x=50, y=110)

shift=['Dinas Pagi','Dinas Siang','Dinas Malam1','Dinas Malam2'] # options
cb1 = customtkinter.CTkComboBox(master=frame, values=shift, width=220) # Combobox
cb1.set('Dinas Pagi') # default selected option
cb1.place(x=50, y=165)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)



app.mainloop()
