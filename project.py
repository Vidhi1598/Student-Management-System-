from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext 
import cx_Oracle
import socket
import requests
#splash screen

splash=Tk()
splash.overrideredirect(True)
splash.geometry("800x500+300+100")
splash.configure(background='cadet blue')
lbl= Label(splash,text="Welcome!",font=("Helvetica",20,'bold'))
lbl.pack(pady=10)
image_file = "wave.gif"
image = PhotoImage(file=image_file, format="gif")
canvas = Canvas(splash, height=400, width=1000)
canvas.create_image(403, 227, image=image)
canvas.pack()

try:
	city="Mumbai"
	socket.create_connection(("www.goggle.com",80))
	print("connected")
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=b8fe7aff02134720530f81ffccf5569b"
	api_address=a1+a2+a3
	
	res=requests.get(api_address)
	print(res)

	data=res.json()
	print(data)
	
	main=data["main"]
	print(main)
	
	temp=main['temp']
	print(temp)
	
	var1 = StringVar()
	var2 = StringVar()
	label1 = Message(splash, textvariable=var1,width=200,font=('arial',11,'bold'))
	label2 = Message(splash, textvariable=var2,width=200,font=('arial',11,'bold'))

	msg1="Temperature(Celsius):"+str(temp)
	var2.set(msg1)
	label2.pack(side=LEFT,padx=150)
	
	msg2="City:"+city
	var1.set(msg2)
	label1.pack(side=LEFT)

except OSError as e:
	print(e)
	print("check network")
def f00():
	splash.withdraw()
	root.deiconify()

root=Toplevel(splash)
root.title("Student Management System")
root.geometry("800x500+300+100")
root.configure(background="cadet blue")
root.iconbitmap('favicon.ico')
root.withdraw()

root.protocol("WM_DELETE_WINDOW",splash.destroy)






viewFrame=Toplevel(root)
viewFrame.title("View")
viewFrame.geometry("400x400+300+200")
viewFrame.withdraw()

st=scrolledtext.ScrolledText(viewFrame,width=30,height=10)
def f1():
	viewFrame.withdraw()
	st.delete('1.0',END)
	root.deiconify()
btnViewBack=Button(viewFrame,text="Back",command=f1)
st.pack()
btnViewBack.pack()










addFrame=Toplevel(root)
addFrame.title("Add")
addFrame.geometry("400x400+300+200")
addFrame.withdraw()

lblAddRno=Label(addFrame,text="Roll no")
entAddRno=Entry(addFrame,bd=5)
lblAddName=Label(addFrame,text="Name")
entAddName=Entry(addFrame,bd=5)



def f3():
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="insert into student values ('%d','%s')"
		rno=entAddRno.get()
		if len(rno)==0:
			messagebox.showerror("incomplete","rollnumber is empty")
			entAddRno.focus()
			return
		if not rno.isdigit() or int(rno)<1:
			messagebox.showerror("wrong","rollnumber should be positive numbers")
			entAddRno.delete(0,END)
			entAddRno.focus()
			return
		name=entAddName.get()
		if len(name)==0:
			messagebox.showerror("incomplete","name is empty")
			entAddName.focus()
			return
		if not name.isalpha():
			messagebox.showerror("wrong","name should be alphabet")
			entAddName.delete(0,END)
			entAddName.focus()
			return
		args=(int(rno),name)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"rows instered"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		con.rollback()
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddRno.focus()
btnAddSave=Button(addFrame,text="Save",command=f3)

def f4():
	addFrame.withdraw()
	root.deiconify()
btnAddBack=Button(addFrame,text="Back",command=f4)


lblAddRno.pack()
entAddRno.pack()
lblAddName.pack()
entAddName.pack()
btnAddSave.pack()
btnAddBack.pack()








updateFrame=Toplevel(root)
updateFrame.title("Update")
updateFrame.geometry("400x400+300+200")
updateFrame.withdraw()

lblUpdateRno=Label(updateFrame,text="Roll no")
entUpdateRno=Entry(updateFrame,bd=5)
lblUpdateName=Label(updateFrame,text="Name")
entUpdateName=Entry(updateFrame,bd=5)

def f5():
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/abc123")
		rno=entUpdateRno.get()
		name=entUpdateName.get()
		cursor=con.cursor()
		sql="update student set name='%s' where rno='%d'"
		args=(name,int(rno))
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"rows updated"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		con.rollback()
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateRno.focus()
btnUpdateSave=Button(updateFrame,text="Save",command=f5)

def f6():
	updateFrame.withdraw()
	root.deiconify()
btnUpdateBack=Button(updateFrame,text="Back",command=f6)


lblUpdateRno.pack()
entUpdateRno.pack()
lblUpdateName.pack()
entUpdateName.pack()
btnUpdateSave.pack()
btnUpdateBack.pack()





deleteFrame=Toplevel(root)
deleteFrame.title("Delete")
deleteFrame.geometry("400x400+300+200")
deleteFrame.withdraw()

lblDeleteRno=Label(deleteFrame,text="Roll no")
entDeleteRno=Entry(deleteFrame,bd=5)

def f7():
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		rno=entDeleteRno.get()
		sql="delete from student where rno='%d'"
		args=(int(rno))
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"rows deleted"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		con.rollback()
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
btnDeleteSave=Button(deleteFrame,text="Save",command=f7)

def f8():
	deleteFrame.withdraw()
	root.deiconify()
btnDeleteBack=Button(deleteFrame,text="Back",command=f8)


lblDeleteRno.pack()
entDeleteRno.pack()
btnDeleteSave.pack()
btnDeleteBack.pack()




def f9():
	root.withdraw()
	addFrame.deiconify()
btnAdd=Button(root,text="Add",font=("arial",20,'bold'),width=10,command=f9)


def f10():
	root.withdraw()
	viewFrame.deiconify()
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for i in data:
			rno=i[0]
			name=i[1]
			info=info+"Roll no:"+str(rno)+"Name:"+name+"\n"
		st.insert(INSERT,info)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
btnView=Button(root,text="View",font=("arial",20,'bold'),width=10,command=f10)

def f11():
	root.withdraw()
	updateFrame.deiconify()
btnUpdate=Button(root,text="Update",font=("arial",20,'bold'),width=10,command=f11)

def f12():
	root.withdraw()
	deleteFrame.deiconify()
btnDelete=Button(root,text="Delete",font=("arial",20,'bold'),width=10,command=f12)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)

def f2():
	viewFrame.withdraw()
	root.deiconify()
viewFrame.protocol("WM_DELETE_WINDOW",f2)

def f13():
	addFrame.withdraw()
	root.deiconify()
addFrame.protocol("WM_DELETE_WINDOW",f13)
def f14():
	updateFrame.withdraw()
	root.deiconify()
updateFrame.protocol("WM_DELETE_WINDOW",f14)
def f15():
	deleteFrame.withdraw()
	root.deiconify()
deleteFrame.protocol("WM_DELETE_WINDOW",f15)

def f01():
	return root
f01()
splash.after(5000, f00)

splash.mainloop()


















































































	 
