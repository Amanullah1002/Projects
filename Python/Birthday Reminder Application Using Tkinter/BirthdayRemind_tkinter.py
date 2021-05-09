import tkinter as tk
import time
today = time.strftime('%m%d')
def record():
    a=open('record.txt','a')
    flag='1'
    while flag == '0':
        nm=input("enter name ")
        em=input("enter data as month/day ")
        a.write(' '+nm+' ; ')
        a.write(str(em)+'\n')
        flag=str(input("Press 1 to enter more "))
    a.close()
b=open('record.txt','r')
flag1=2
for line in b: 
    if today in line:
        field=line.split(';')
        nm1=field[0]
        r=tk.Tk()
        r.title("   Birthday Reminder  ")
        r.geometry("500x100")
        msg=tk.Message(r,text="Today is "+nm1+"'s birthday",width='500',fg="white",font=('times',24,'bold'),bg='blue')
        msg.pack()
        button=tk.Button(r,text='OK',command=r.destroy,font=('times',11,'bold'))
        button.pack()
        r.mainloop()
        flag1=1
        break
if flag1==2:
    r=tk.Tk()
    r.title("   Birthday Reminder  ")
    r.geometry("400x100")
    msg=tk.Message(r,text="There is no birthday today",width='500',font=('times',24,'bold'),bg='blue',fg='white')
    msg.pack()
    button=tk.Button(r,text='OK',font=('times',11,'bold'),command=r.destroy)
    button.pack()
    r.mainloop()     
b.close()
record()
