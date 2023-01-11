from tkinter import *
import matplotlib.pyplot as plt

root=Tk()
root.title("Chart Marker")
root.geometry("500x600+50+50")
f=("Arial",30,"bold")

lab_name=Label(root,text="Enter name",font=f)
lab_name.pack()
ent_name=Entry(root,font=f,bd=4)
ent_name.pack()


lab_phy=Label(root,text="Enter physics marks",font=f)
lab_phy.pack()
ent_phy=Entry(root,font=f,bd=5)
ent_phy.pack()


lab_chem=Label(root,text="Enter chem marks",font=f)
lab_chem.pack()
ent_chem=Entry(root,font=f,bd=5)
ent_chem.pack()


lab_maths=Label(root,text="Enter maths marks",font=f)
lab_maths.pack()
ent_maths=Entry(root,font=f,bd=5)
ent_maths.pack()



def gc():
	name=ent_name.get()
	phy=int(ent_phy.get())
	chem=int(ent_chem.get())
	maths=int(ent_maths.get())
	subjects=["phy","chem","maths"]
	marks=[phy,chem,maths]
	plt.plot(subjects,marks,linewidth=4,marker="o",markersize=10)		
	plt.xlabel("Subjects")
	plt.ylabel("Marks")
	plt.title(name+"'s Score")
	plt.grid()
	plt.savefig(name+".png")
	plt.savefig(name+".pdf")
	plt.show()

btn_chart=Button(root,text="Generate Graph",font=f,command=gc)
btn_chart.pack()

root.mainloop()