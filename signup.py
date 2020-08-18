
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk     # pip install pillow fro terminal.
import pymysql                    # pip install pymysql from terminal.
class Downloader:
    def __init__(self, manish):
        self.manish=manish
        self.manish.title("Video Downloader")
        self.manish.geometry("1250x630+100+70")
        self.manish.resizable(False, False)


        # insert bg for attraction.
        self.bg=ImageTk.PhotoImage(file="C:/Users/dell/Desktop/login system project/image/frame12.jpg")
        bg=Label(self.manish,image= self.bg).pack()

        # insert left image for new design.
        self.left=ImageTk.PhotoImage(file="C:/Users/dell/Desktop/login system project/image/frame1.png")
        left=Label(self.manish,image= self.left).place(x=90, y=70, width=450, height= 500)

        # downloader frame.================================Row1==================================
        login_frame=Frame(self.manish, bg= "white")
        login_frame.place(x= 540, y=70, width=650, height= 500)

        # accessories  for sign in frame,================================Row2===================================
        title=Label(login_frame, text= "WELCOME", width= 9, font= ("castellar", 25, "bold"), bg= "lightgreen", fg= "black")
        title.place(x= 50, y=30)

        title1 = Label(login_frame, text="Register", width=10, font=("castellar", 25, "bold"), bg="lightgreen", fg="black")
        title1.place(x=365, y=30)

        # sign up process.(name, entry box)================================Row3===================================
        var1 = StringVar()
        fname = Label(login_frame, text="First Name", font=("arial", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)
        self.e1_fname= Entry(login_frame, font=("arial", 13), textvariable=var1, bg= "lightgray", width=15)
        self.e1_fname.place(x= 50, y=130,width=220)

        var2=StringVar()
        lname = Label(login_frame, text="Last Name", font=("arial", 15, "bold"), bg="white", fg="black")
        lname.place(x=370, y=100)
        self.e1_lname = Entry(login_frame, font=("arial", 13), textvar=var2, bg="lightgray", width=15)
        self.e1_lname.place(x=370, y=130, width=220)

        # entry and label for country and contact.================================Row4===============================
        var3=StringVar()
        contact = Label(login_frame, text="Contact No.", font=("arial", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.e1_contact = Entry(login_frame, font=("arial", 13), textvar=var3, bg="lightgray", width=15)
        self.e1_contact.place(x=50, y=200, width=220)

        var4=StringVar()
        country = Label(login_frame, text="Country", font=("arial", 15, "bold"), bg="white", fg="black")
        country.place(x=370, y=170)
        self.e1_country = Entry(login_frame, font=("arial", 13), textvar=var4, bg="lightgray", width=15)
        self.e1_country.place(x=370, y=200, width=220)

        # DOB and Gender ================================Row5==========================================
        var5=StringVar()
        birth = Label(login_frame, text="DOB", font=("arial", 15, "bold"), bg="white", fg="black")
        birth.place(x=50, y=240)
        self.e1_birth = Entry(login_frame, font=("arial", 13), textvar= var5, bg="lightgray", width=15)
        self.e1_birth.place(x=50, y=270, width=220)

        gender = Label(login_frame, text="Gender", font=("arial", 15, "bold"), bg="white", fg="black")
        gender.place(x=370, y=240)
        global var6
        var6 = StringVar()
        choices = ["Select","Male","Female"]
        self.comb_gender = ttk.OptionMenu(login_frame, var6,*choices)
        var6.set("Select")
        self.comb_gender.place(x=370, y=270, width=220)

        # email and password ================================Row6==========================================
        var7=StringVar()
        var8=StringVar()
        email = Label(login_frame, text="Email", font=("arial", 15, "bold"), bg="white", fg="black").place(x=50, y=310)
        self.e1_email = Entry(login_frame, font=("arial", 13), textvar=var7, bg="lightgray", width=15)
        self.e1_email.place(x=50, y=340, width=220)
        password = Label(login_frame, text="Password", font=("arial", 15, "bold"), bg="white", fg="black").place(x=370, y=310)
        self.e1_password = Entry(login_frame, font=("arial", 13), textvar=var8, bg="lightgray",show= "*****", width=15)
        self.e1_password.place(x=370, y=340, width=220)
        # term and condition ================================Row7==========================================
        self.var9=IntVar()
        check = Checkbutton(login_frame, text= "I agree all the terms and conditions.", onvalue=1, offvalue=0, variable=self.var9, bg= "white").place(x=50, y=380)


        self.btn_image = ImageTk.PhotoImage(file="C:/Users/dell/Desktop/login system project/image/logo9.jfif")
        btn = Button(login_frame, image=self.btn_image, bd=0, cursor= "hand2", command= self.sign_in).place(x=50,y=430, width= 220, height= 53)
        # ========================left image login=================================================================
        btn_started= Button(self.manish, text= "Get Started", command=self.started_window, width= 13, font=("arial",15,"bold"), bd=0, bg="yellow" , cursor="hand2").place(x=250, y=450)

    def started_window(self):
        self.manish.destroy()
        import login

    def clear(self):
        self.e1_fname.delete(0, END)
        self.e1_lname.delete(0, END)
        self.e1_contact.delete(0, END)
        self.e1_country.delete(0, END)
        self.e1_birth.delete(0, END)
        self.var9.get()
        self.e1_email.delete(0, END)
        self.e1_password.delete(0, END)


    def sign_in(self):
        if self.e1_fname.get()=="" or self.e1_contact.get()=="" or self.e1_country.get()=="" or self.e1_birth.get()=="" or var6.get()=="Select" or self.e1_email.get()=="" or self.e1_password.get()=="":
            messagebox.showerror("Error","Please! fill up all information.", parent= self.manish)
        elif self.var9.get()==0:
            messagebox.showerror("Error", "Don't you agree the Terms and Conditions?", parent=self.manish)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root", password="", database="database_billing")
                cur=con.cursor()
                cur.execute("select * from login where email = %s",self.e1_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already logged in, Please try another email.", parent=self.manish)
                else:
                    cur.execute("insert into login(fname, lname, contact, country, birth, gender, email, password) values(%s,%s,%s,%s,%s,%s,%s,%s)",

                                    (self.e1_fname.get(),
                                    self.e1_lname.get(),
                                    self.e1_contact.get(),
                                    self.e1_country.get(),
                                    self.e1_birth.get(),
                                    self.var9.get(),
                                    self.e1_email.get(),
                                    self.e1_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Successful", "Sign Up successfully!", parent=self.manish)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.manish)




manish = Tk()                              # manish is the object for Tk.
video = Downloader(manish)                 # video is the object for class.
manish.mainloop()
