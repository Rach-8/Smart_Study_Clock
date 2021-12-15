import tkinter as Tkinter 
import tkinter as tk  
from datetime import datetime 
from tkinter import *
from typing import Counter


counter1 = 0
running1 = False
counter = 0
running = False
root = Tkinter.Tk()      
root.maxsize(width=350 , height= 900) 
root.minsize(width  = 350 , height = 550)
laps = []
L =  []
t_counter = 0
import time
t_list = [0]
r=[]
T = 0
t_list2 = []
i=0 
import tkinter.messagebox

root.title("Smart Study Clock") 

BG = '#21292e'
Font_text = ('Open Sans', 11,'bold')
Font_clock=("Montserrat", 20,'bold')
Font_buttons=('Open Sans', 10)
root['background']= BG
color = '#a3bbbf'

#__
var2 = t_counter
var3 = counter 





#main frame
main_frame= Frame(root)
#main_frame.pack(fill=BOTH , expand= 1)

#canvas 





img = PhotoImage(file="START.png")
red = PhotoImage(file="REDEEM.png")
save=PhotoImage(file="SAVE.png")
add=PhotoImage(file="ADD.png")
table = PhotoImage(file="TABLE.png")






#website blocker
def web_block(websites):
    host_path = 'C:/Windows/System32/drivers/etc/hosts'
    redirect = "127.0.0.1" 
    fileptr =  open(host_path,"r+")
    content = fileptr.read()  
    for website in websites:  
        if website in content:  
            pass  
        else:  
            fileptr.write(redirect+"    "+website+"\n")  
            fileptr.write(redirect+"    "+'www.'+website+"\n") 


#website unblocker
def web_unblock():
    host_path = 'C:/Windows/System32/drivers/etc/hosts'
    with open(host_path,'r+') as file:  
        file.truncate() 
   






# STUDY TIME TEXT
def study_time(text):
    T1 = Tkinter.Text(root, height = 1, width = 13 , highlightthickness = 0 ,borderwidth=0 ,bg=BG,font = ("Impact"),fg=color)  #
    Fact1 = text
    T1.insert(Tkinter.END, Fact1)
    T1.pack(anchor = 'w') 
    T1.configure(state="disabled")
study_time("Study Clock : ")


#CLOCK1
def counter_label1(label1 , t_counter):  #clock1
    def count1():  
        if running1:
            web_block(L)
            global t_counter
            global counter1    
            if counter1==0:              
                display1=""
            else: 
                tt1 = datetime.utcfromtimestamp(counter1) 
                
                string1 = tt1.strftime( "%H:%M:%S") 
                display1=string1  
    
            label1['text']=display1   
            label1.after(1000, count1)   
            counter1 += 1
            t_counter += 1
            return t_counter
            
    count1()

def Start1(label1):          #start button of clock 1 and stop button of clock2
    global running1 
    global running 
    running1=True
    running = False
    counter_label1(label1 , t_counter)  
    start1['state']='disabled'
    start['state']='normal'



# CLOCK1 ATTRIBUTES
label1 = Tkinter.Label(root, text="00:00:00", font = ("Agency FB",35),bg=BG,fg='#86E782')  #
label1.pack(anchor = 'w')  
f = Tkinter.Frame(root) 
start1 = Tkinter.Button(f, image=img, command=lambda:Start1(label1),bg=BG,borderwidth=0)  #
f.pack(anchor = 'w',pady=5) 
start1.pack(side="left")  



# BREAK TIME TEXT
def break_time(text):
    T = Tkinter.Text(root, height = 2, width = 13 , highlightthickness = 0 ,borderwidth=0,font = ("Impact"),bg=BG,fg=color)  
    Fact = text
    T.insert(Tkinter.END, Fact)
    T.pack(anchor = 'w')  
    T.configure(state="disabled") 
break_time("\nBreak Timer : ")


k = 0
#CLOCK2
def counter_label(label , T):    #clock2
    def count():  
        if running:  
            web_unblock()
            global counter
            i = 0   
            
            tt = datetime.utcfromtimestamp(counter+T) # T = time to be added in the timer
            string = tt.strftime("%H:%M:%S") 
            display=string  
            label['text']=display   
            label.after(1000, count)   
            if counter+T-1 >= 0:
                counter -= 1
                if counter+T<1 :
                    
                    tkinter.messagebox.showinfo('Alert!','Your earned break time is over and the websites have been blocked , please start the study clock to earn more break time.')
                    
                
 

    count()       
def Start(label):            #start button of clock2 and stop button of clock2
    global running 
    global running1 
    running=True
    running1 = False
    counter_label(label ,T)  
    start['state']='disabled'
    start1['state']='normal'
 


# CLOCK2 ATTRIBUTES
label = Tkinter.Label(root, text="00:00:00", font = ("Agency FB",35),bg=BG ,fg='#587DD4')  
label.pack(anchor = 'w')  
f = Tkinter.Frame(root) 
start = Tkinter.Button(f, image= red, command=lambda:Start(label),bg=BG,borderwidth=0)  
f.pack(anchor = 'w',pady=5) 
start.pack(side="left")  
t_list.append(0)
def checklist_Text(text):
    T1 = Tkinter.Text(root, height = 5, highlightthickness = 0 ,borderwidth=0,bg=BG,font = ("IMPACT"),fg=color)  
    Fact1 = text
    T1.insert(Tkinter.END, Fact1)
    T1.pack(anchor = 'w') 
    T1.configure(state="disabled")
checklist_Text("\n\nComplete Checklists to get more break time \nto browse the blocked websites :")



def add_more():
    checklists()
    checklists.Bc.pack_forget()




# CHECKLIST
def checklists():



    fc=Tkinter.Frame(root)


    var1 = Tkinter.IntVar()  
    def info1():
        n1=var1.get()
        def limit1():
            if n1==1:
                t_list.append(t_counter)
                calc_T(t_list)
        def click1():
            chk1.config(state=DISABLED)
        limit1()
        click1()
    chk1 = Tkinter.Checkbutton(fc, variable=var1, command=info1,bg='#2c8279',bd=10)
    chk1.grid(row=1,column=0,padx=0,pady=0)
    checklists.t = Tkinter.Text(fc, height=2,bg='#45baae',font=("gotham"),borderwidth=2)
    checklists.t.insert(1.0," ")
    checklists.t.grid(row =1 ,column = 1 )
    fc.pack(anchor='sw') 
    
    def readonly():
        checklists.t.configure(state='disabled') 
        Br.pack_forget()
     
    Br = tk.Button( image=save, command = readonly  ,bg=BG,fg=color,borderwidth=0)
    Br.pack(anchor='sw')
    checklists.Bc = tk.Button( image=add, command = add_more,bg=BG,fg=color,borderwidth=0)



checklists()

    


def pop_up():
    tkinter.messagebox.showinfo('Alert!','Your earned break time is over and the websites have been blocked , please start the study clock to earn more break time.')



def close_window():
    global entry
    entry = E.get()
    L.append(entry)
    



def calc_T(t_list ):
    t_list2 = []
    global T
    for i in range(1, len(t_list)): 
        t_list2.append((t_list[i] - t_list[i-1])/3) 
    for ele in range(0, len(t_list2)): 
        T = T + t_list2[ele]
    
    return T 










def Open_table():
     
    newWindow = Toplevel(root)
    newWindow.title("Activity Table")
    newWindow['background']= BG
    newWindow.maxsize(width=600 , height= 1200) 
    newWindow.minsize(width  = 600, height = 300)
    














tb = Tkinter.Button(root, image = table, 
            command = Open_table ,   bg=BG  ,   borderwidth=0)
tb.pack(side = 'bottom' ,anchor='se' )


B = Button(root, text = "Enter", command = close_window , fg='#FFFFFF',bg='#059DA8',font=Font_buttons)
B.pack(side = 'bottom' )


E = Tkinter.Entry(root , highlightthickness = 0 ,borderwidth=0,bg="#C9C9C9")
E.pack(side = 'bottom' )




checklists.Bc.pack(anchor='se', side = 'bottom')






































root.mainloop()






print(L)
print(t_counter)
print(counter)





"""to make this app usable :

fix all bugs

website blocker :
    websites should get blocked when study timer is running
    websites should get unblocked when break timer is running

GUI :
    gui should be better

Previous activity table :
    there should be a integrated table in the app which shows websites entered 
    and time studied and break time

deploy the app as an exe """