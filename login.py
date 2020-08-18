from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
class login_window:
    def __init__(self,manish):
        self.manish= manish
        self.manish.title("Login Window")
        self.manish.geometry("750x450+200+90")
        self.manish.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="C:/Users/Dell/Desktop/login system project/image/login4.jpg")
        bg = Label(self.manish, image=self.bg).pack()

        title1 = Label(self.manish, text= "Login System", font= ("garamond",30, "bold"),bg= "lime green")
        title1.place(x=0, y=0, relwidth= 1)

        window_frame = Frame(self.manish, bg="white")
        window_frame.place(x=180, y=75, width=330, height=300)

        self.icon = ImageTk.PhotoImage(file="C:/Users/Dell/Desktop/login system project/image/assistant3.png")
        icon = Label(self.manish, image=self.icon).place(x=300,y=77)

        eee = Label(window_frame, text="Email Address", font=("batang", 15, "bold"), bg="white", fg="black")
        eee.place(x=50, y=100)

        ppp = Label(window_frame, text="Password", font=("batang", 15, "bold"), bg="white", fg="black")
        ppp.place(x=50, y=170)

        self.e_eee= Entry(window_frame, font=("batang", 13), bg= "lightgray", width=15)
        self.e_eee.place(x= 50, y=130,width=220)

        self.e_ppp = Entry(window_frame, font=("batang", 13), show="*****", bg="lightgray", width=15)
        self.e_ppp.place(x=50, y=200, width=220)

        btn_login = Button(window_frame, text="Login", width=7, font=("batang", 15, "bold"), command= self.login_win,bd=4,
                           bg="maroon",fg="white",cursor="hand2").place(x=50, y=240)

        btn_registers = Button(window_frame, text="Register", width=7, font=("batang", 15, "bold"), command=self.signup_window,
                           bd=4, bg="maroon", fg="white", cursor="hand2").place(x=163, y=240)

        title2 = Label(self.manish, text="Thank You !!!", font=("garamond", 30, "bold"), bg="lime green")
        title2.place(x=0, y=400, relwidth=1)

    def signup_window(self):
        self.manish.destroy()
        import signup

    def login_win(self):
        if self.e_eee.get() == "" or self.e_ppp.get() =="":
            messagebox.showerror("Error","please fill up all the information", parent=self.manish)
        else:
            try:
                con = pymysql.connect(host= "localhost", user="root", password="", database= "database_billing")
                cur=con.cursor()
                cur.execute("select * from login where email= %s and password= %s", (self.e_eee.get(), self.e_ppp.get()))
                row = cur.fetchone()
                print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid username and password.", parent=self.manish)
                else:
                    messagebox.showinfo("Successful", "WELCOME", parent=self.manish)

                    self.manish.destroy()
                    import billing_software

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.manish)










manish = Tk()
login= login_window(manish)
manish.mainloop()
