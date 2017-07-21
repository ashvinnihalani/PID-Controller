import matplotlib # Platting Library
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from tkinter import * # Import the tinker module
from tkinter import ttk #Themed ttk
#Create & Configure root 
root = Tk() # Main window
root.title("PID Interface")
root.columnconfigure(0, weight=1) #Inside root: 1 col, expand to fit
root.rowconfigure(0, weight=1) #Inside root: 1 row, expand to fit

#Base Frame needs to be different then root
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=N+S+E+W) #Put in the top left cell and expand to size
mainframe.columnconfigure(0, weight=1) #Inside Mainframe:1 col, expand to fit
mainframe.rowconfigure(0, weight=1) 
mainframe.rowconfigure(1, weight=10) #Inside Mainframe:2 col, majority given to bottom
mainframe.config(bg="black")

#Variable set up
user_temp = IntVar()
measure_temp = StringVar()
proportinal_constant = StringVar()
integral_constant = StringVar()
derivative_constant = StringVar()
pid_control=StringVar()
pid_control.set("PID")
choices = { 'PID','PI','P','PD'}

#User Control Set Up
user_interface = Frame(mainframe) #Frame inside mainfraime
user_interface.config(bg="red") 
user_interface.grid(column=0, row=0, sticky=N+S+E+W) #Positon: Top,left of Mainframe, expand to fit
for x in range(13):
	user_interface.columnconfigure(x, weight=1) # Initlizes the col with a wirght of zero, usefull in dev 
user_interface.rowconfigure(0, weight=1) #one row, expand to fit

#Actual User Control
#Sub section User Temp
utemp_label = ttk.Label(user_interface,text="User Set Point:")
utemp_label.grid(column=0,row=0,sticky=E)
utemp_widget = ttk.Entry(user_interface,textvariable=user_temp)
utemp_widget.grid(column=1,row=0,sticky=E+W) #Text box for user
utemp_unit = ttk.Label(user_interface,text="C")
utemp_unit.grid(column=2,row=0,sticky=W)
def utemp_set(): #Function for setting the User temp
	if utemp_widget.get() == None :
		user_temp.set(0)
	else :
		user_temp.set(utemp_widget.get())
utem_submit = ttk.Button(user_interface,text="submit",command=utemp_set)
utem_submit.grid(column=3,row=0,sticky=W)
#K values 
kp_label= ttk.Label(user_interface,text="K\u209A:")
kp_label.grid(column=4,row=0)
kp_widget = ttk.Entry(user_interface,textvariable=proportinal_constant)
kp_widget.grid(column=5,row=0)
ki_label = ttk.Label(user_interface,text="K\u2097:")
ki_label.grid(column=6,row=0)
ki_widget = ttk.Entry(user_interface,textvariable=integral_constant)
ki_widget.grid(column=7,row=0)
kd_label = ttk.Label(user_interface,text="Kd:")
kd_label.grid(column=8,row=0)
kd_widget = ttk.Entry(user_interface,textvariable=derivative_constant)
kd_widget.grid(column=9,row=0)
manual_tune = ttk.Button(user_interface,text="Manual Tune")
manual_tune.grid(column=10,row=0)
#PID selection sub section 
pidc_label = ttk.Label(user_interface,text="PID Control:")
pidc_label.grid(column=11,row=0,sticky=E)
pidc_choice= OptionMenu(user_interface,pid_control,*choices)
pidc_choice.grid(column=12,row=0,sticky=E+W)
auto_tune = ttk.Button(user_interface,text="AutoTune")
auto_tune.grid(column=13,row=0,sticky=W)

#Function on PID Update
def change_pidc(*args):
	if(pid_control.get()=="P"):
		integral_constant.set(0)
		derivative_constant.set(0)
		ki_widget.config(state="disabled")
		kd_widget.config(state="disabled")
	elif(pid_control.get()=="PI"):
		derivative_constant.set(0)
		ki_widget.config(state="normal")
		kd_widget.config(state="disabled")
	elif(pid_control.get()=="PD"):
		integral_constant.set(0)
		ki_widget.config(state="disabled")
		kd_widget.config(state="normal")
	else:
		ki_widget.config(state="normal")
		kd_widget.config(state="normal")
pid_control.trace('w', change_pidc)

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open("sampleData.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)
root.mainloop()
