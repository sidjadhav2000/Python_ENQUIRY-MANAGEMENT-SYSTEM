from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import*
from pymongo import *

def f2():
	sw.withdraw()
	mw.deiconify()
#------------------------------------------------------------------------------------------------
def f1():
	try:
		try:
			user = mw_ent_un.get()
			if user == "":
				showerror("issue", "username cannot be empty")
				return
			if not user.isalpha():
				showerror("issue", "username should be alphabet")
				return
		except Exception as e:
			showerror("issue", e)
			return
		try:
			passward = mw_ent_pass.get()
			if passward == "":
				showerror("issue", "passward cannot be empty")
				return
			if not passward.isalpha():
				showerror("issue", "passward should be alphabet")
				return
		except Exception as e:
			showerror("issue", e)
			return
		try:
			if (user != "sid") and (passward != "jadhav"):
				showerror("issue", "wrong user and passward")
				return
			if (user == "sid") and (passward == "jadhav"):	
				showinfo("success", "Login Successfully")
				mw_ent_un.delete(0, END)
				mw_ent_pass.delete(0, END)
				mw.withdraw()
				sw.deiconify()
				sw_st_data.delete(1.0, END)
				con = None
				try:
					con = MongoClient("localhost", 27017)
					db = con["EMS"]
					coll = db["user"]
					data = coll.find()
					for d in data:
						sw_st_data.insert(INSERT, d)
				except Exception as e:
					showerror("issue", e)
					return
		except Exception as e:
			showerror("issue", e)
			return
	except Exception as e:
		showerror("issue", e)	
		return
#-------------------------------------------------------------------------------------------------------------------

def deletedata():
	con = None
	try:
		con = MongoClient("localhost", 27017)
		db = con["EMS"]
		coll = db["user"]
		try:
			user_name = sw_ent_name.get()
			if user_name == "":
				showerror("issue", "name cannot be empty")
				return
			if not user_name.isalpha():
				showerror("issue", "name should be alphabet")
				return
		except Exception as e:
			showerror("issue", e)
			return
		count = coll.count_documents({"NAME": user_name})
		if count == 1:
			coll.delete_one({"NAME":user_name})
			showinfo("success", "data deleted")	
		else:
			showerror("issue", "name not found")
			return
		sw_ent_name.delete(0, END)
	except Exception as e:
		showerror("issue", e)
		return
	finally:
		if con is not None:
			con.close()


#---------------------------------------------------------------------------------------------------------------
def userdata ():
	con = None
	try:
		con = MongoClient("localhost",27017)
		db = con["EMS"]
		coll = db["user"]
		try:	
			n = mw_entry_name.get()
			if n == "":
				showerror("Issue","NAME cannot be Empty")
				return

			if not n.isalpha():
				showerror("Issue","NAME should be Alphabet")
				return
			
		except Exception as e:
			showerror("Issue",e)
			return 

		try:
			p = int(mw_entry_phone.get())
			if p < 1 :
				showerror("Issue","ENTER postive Number only")
				return
			if p > 9999999999 :
				showerror("Issue","ENTER only 10 digit Phone number")
				return
		except ValueError:
			showerror("Issue","Phone number should be Integer only")
			return

		try:
			a = mw_entry_add.get()
			if a == "":
				showerror("Issue","ADDRESS cannot be Empty")
				return
		except Exception as e:
			showerror("Issue",e)	
			return
	
		product = ""
		if p1.get() ==	1:
			product += "Product 1"
		if p2.get() == 1:
			product += "Product 2"
		if p3.get() == 1:
			product += "Product 3"
		if p4.get() == 1:
			product += "Product 4"
		if p5.get() == 1:
			product += "Product 5"

		info = {"NAME":n,"PHONE NO":p,"ADDRESS":a,"PRODUCTS":product}
		coll.insert_one(info)
		showinfo("SUCCESS","DATA STORED")
		mw_entry_name.delete(0,END)
		mw_entry_phone.delete(0,END)		
		mw_entry_add.delete(0,END)
		
		mw_entry_name.focus()

	except Exception as e:
		showerror("Issue",e)
		return
	finally:
		if con is not None:
			con.close()




mw = Tk()
mw.title("EMS")
mw.configure(bg = "medium slate blue")
mw.geometry("500x680+100+50")
f = ("Algerian",20,"bold","underline")
e = ("Arial",20,"bold")
c = ("Arial",12,"bold")

mw_header = Label(mw , text="ENQUIRY MANAGEMENT SYSTEM", font=f, fg = "black",bg = "medium slate blue")
mw_header.pack(pady=10)

mw_label_name = Label(mw, text="NAME", font=f, fg = "black",bg = "medium slate blue")
mw_entry_name = Entry(mw, font=e )
mw_label_name.place(x=50,y=75)
mw_entry_name.place(x=150,y=75)

mw_label_phone = Label(mw, text="PHONE", font=f, fg = "black",bg = "medium slate blue")
mw_entry_phone = Entry(mw, font=e )
mw_label_phone.place(x=30,y=150)
mw_entry_phone.place(x=150,y=150)

mw_label_add = Label(mw, text="ADD", font=f, fg = "black",bg = "medium slate blue")
mw_entry_add = Entry(mw, font=e )
mw_label_add.place(x=50,y=220)
mw_entry_add.place(x=150,y=220)

p1,p2,p3,p4,p5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
mw_label_product = Label(mw, text="PRODUCTS", font=f, fg = "black",bg = "medium slate blue")
mw_cb_p1 = Checkbutton(mw, text = "P1", font=c, variable=p1, fg = "black",bg = "medium slate blue")
mw_cb_p2 = Checkbutton(mw, text = "P2", font=c, variable=p2, fg = "black",bg = "medium slate blue")
mw_cb_p3 = Checkbutton(mw, text = "P3", font=c, variable=p3, fg = "black",bg = "medium slate blue")
mw_cb_p4 = Checkbutton(mw, text = "P4", font=c, variable=p4, fg = "black",bg = "medium slate blue")
mw_cb_p5 = Checkbutton(mw, text = "P5", font=c, variable=p5, fg = "black",bg = "medium slate blue")
mw_label_product.place(x=10,y=300)
mw_cb_p1.place(x=200,y=300)
mw_cb_p2.place(x=260,y=300)
mw_cb_p3.place(x=320,y=300)
mw_cb_p4.place(x=380,y=300)
mw_cb_p5.place(x=440,y=300)

mw_btn_submit = Button(mw, text="SUBMIT", font=f,command=userdata)
mw_btn_submit.place(x=180,y=350)

mw_header = Label(mw , text="ADMIN LOGIN", font=f, fg = "black",bg = "medium slate blue")
mw_header.place(x=150,y=420)

mw_label_un = Label(mw, text="USERNAME", font=f, fg = "black",bg = "medium slate blue")
mw_ent_un = Entry(mw,font=e ,width=12)
mw_label_un.place(x=10,y=460)
mw_ent_un.place(x=50,y=510)

mw_label_pass = Label(mw, text="PASSWORD", font=f, fg = "black",bg = "medium slate blue")
mw_ent_pass = Entry(mw,font=e ,width=12)
mw_label_pass.place(x=10,y=570)
mw_ent_pass.place(x=50,y=620)

mw_btn_login = Button(mw, text="LOGIN", font=f,command=f1)
mw_btn_login.place(x=300,y=550)


sw = Tk()
sw.title("ADMIN PAGE")
sw.configure(bg="Aquamarine")
sw.geometry("500x600+100+100")
f=("Arial", 20, "bold","underline")
c=("Arial", 20, "bold")

sw_header_adm = Label(sw, text = "ADMIN", font=f, fg="dark blue", bg="Aquamarine")
sw_header_page = Label(sw, text = "PAGE", font=f, bg="Aquamarine")
sw_header_page.place(x=250,y=10)
sw_header_adm.place(x=160,y=10)


sw_st_data = ScrolledText(sw, font=f,width=30,height=8) 
sw_st_data.place(x=10, y=80)

sw_label_name = Label(sw, text="ENTER NAME", font=f,bg="Aquamarine")
sw_ent_name = Entry(sw, font=c,width=10)
sw_label_name.place(x=20, y=380)
sw_ent_name.place(x=230, y =380)

sw_btn_delete = Button(sw, text="DELETE",font=f, command=deletedata)
sw_btn_delete.place(x=170, y=450)

sw_btn_back = Button(sw, text="BACK",font=f,command=f2)
sw_btn_back.place(x=180, y=520)
sw.withdraw()

def f4():
	if askokcancel("QUIT ", "Do you want to exit"):
		mw.destroy()
		sw.destroy()
		#vw.destroy()

mw.protocol("WM_DELETE_WINDOW", f4)
sw.protocol("WM_DELETE_WINDOW", f4)
#vw.protocol("WM_DELETE_WINDOW", f4)



mw.mainloop()
sw.mainloop()