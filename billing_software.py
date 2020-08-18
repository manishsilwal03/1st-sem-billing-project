from tkinter import *
import math, random
import os
from tkinter import messagebox
class Billing:
    def __init__(self, manish):
        self.manish = manish
        self.manish.title("Billing Software")
        self.manish.geometry("1355x710+50+30")
        self.manish.resizable(False, False)
        background ="red"
        title1 = Label(self.manish, text="Welcome To Manish Retail Billing", bd= 12, relief= GROOVE,font=("Arial", 30, "bold"),fg="white", bg=background)
        title1.place(x=3,relwidth=1)

        # creating variables call ==========================================================

        self.name = StringVar()
        self.phone = StringVar()
        self.bill = StringVar()
        m = random.randint(1000,9999)
        self.bill.set(str(m))
        self.search = StringVar()

        self.soup = IntVar()
        self.cream = IntVar()
        self.wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()

        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        self.coke = IntVar()
        self.slice = IntVar()
        self.sprite = IntVar()
        self.frooti= IntVar()
        self.maza= IntVar()
        self.litchi= IntVar()

        self.cosmetic = StringVar()
        self.grocery= StringVar()
        self.drinks = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.drinks_tax = StringVar()

        # =================================================================*======================================

        f1 = LabelFrame(self.manish, text="Customer details", bd=7, relief= GROOVE, font=("Arial", 15, "bold"),fg="yellow", bg=background)
        f1.place(x=3, y=80,relwidth=1)

        c_name = Label(f1, text= "Customer Name", font=("Arial", 15, "bold",),bg= background, fg= "white")
        c_name.grid(row=0, column=0, padx=20, pady=2)
        e_name = Entry(f1, width= 16, textvariable=self.name, font=("Arial",14), bd=7, relief= RAISED).grid(row=0, column=1, padx= 10, pady=5)

        c_phone = Label(f1, text="Phone No.", font=("Arial", 15, "bold",), bg=background, fg="white")
        c_phone.grid(row=0, column=2, padx=20, pady=2)
        e_phone = Entry(f1, width=16, textvariable=self.phone, font=("Arial", 14), bd=7, relief=RAISED).grid(row=0, column=3, padx=10, pady=5)

        c_bill = Label(f1, text="Bill Number", font=("Arial", 15, "bold",), bg=background, fg="white")
        c_bill.grid(row=0, column=4, padx=20, pady=2)
        e_bill = Entry(f1, width=16, textvariable=self.search, font=("Arial", 14), bd=7, relief=RAISED).grid(row=0, column=5, padx=10, pady=5)

        btn_bill = Button(f1, text="Search", command= self.search_bill, font=("Arial", 10,"bold"),cursor= "hand2", width= 10, bd=7)
        btn_bill.grid(row=0, column= 6, padx=15, pady=8)

        # ============================================================================================================

        f2 = LabelFrame(self.manish, text="Cosmetics", bd=9, relief=GROOVE, font=("Arial", 15, "bold"), fg="yellow", bg=background)
        f2.place(x=3, y=170, width= 325, height= 345)

        name_soup = Label(f2, text= "Soup",font=("Arial", 15, "bold"), bg=background, fg="white")
        name_soup.grid(row=0, column= 0, padx= 10, pady= 10, sticky= "w")
        entry_soup = Entry(f2, width= 15, textvariable=self.soup,font=("Arial", 12, "bold"),bd= 4, relief= SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        name_cream = Label(f2, text="Face Cream", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_cream.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_cream = Entry(f2, width=15, textvariable=self.cream, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        name_wash = Label(f2, text="Face Wash", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_wash.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry_wash = Entry(f2, width=15, textvariable=self.wash, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        name_spray = Label(f2, text="Hair Spray", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_spray.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        e_spray = Entry(f2, width=15, textvariable=self.spray, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        name_gell = Label(f2, text="Hair Gell", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_gell.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        e_gell = Entry(f2, width=15, textvariable=self.gell, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        name_lotion = Label(f2, text="Body lotion", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_lotion.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        entry_lotion = Entry(f2, width=15, textvariable=self.lotion, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ============================================================================================================

        f3 = LabelFrame(self.manish, text="Grocery", bd=9, relief=GROOVE, font=("Arial", 15, "bold"), fg="yellow", bg=background)
        f3.place(x=333, y=170, width=325, height=345)

        name_rice = Label(f3, text="Rice", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_rice.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_soup = Entry(f3, width=15, textvariable=self.rice, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        name_oil = Label(f3, text="Oil", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_oil.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_oil = Entry(f3, width=15, textvariable=self.oil, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        name_daal = Label(f3, text="Daal", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_daal.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry_daal = Entry(f3, width=15, textvariable=self.daal, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        name_wheat = Label(f3, text="Wheat", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_wheat.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        e_wheat = Entry(f3, width=15, textvariable=self.wheat, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        name_sugar = Label(f3, text="Sugar", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_sugar.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        e_sugar = Entry(f3, width=15, textvariable=self.sugar, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        name_tea = Label(f3, text="Tea", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_tea.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        entry_tea = Entry(f3, width=15, textvariable=self.tea, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ============================================================================================================

        f4 = LabelFrame(self.manish, text="Cold Drinks", bd=9, relief=GROOVE, font=("Arial", 15, "bold"), fg="yellow", bg=background)
        f4.place(x=663, y=170, width=325, height=345)

        name_coke = Label(f4, text="Coke", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_coke.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_coke = Entry(f4, width=15, textvariable=self.coke, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        name_slice = Label(f4, text="Slice", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_slice.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_slice = Entry(f4, width=15, textvariable=self.slice, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        name_sprite = Label(f4, text="Sprite", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_sprite.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry_sprite = Entry(f4, width=15, textvariable=self.sprite, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        name_frooti = Label(f4, text="Frooti", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_frooti.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        e_frooti = Entry(f4, width=15, textvariable=self.frooti, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        name_maza = Label(f4, text="Maza", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_maza.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        entry_maza = Entry(f4, width=15, textvariable=self.maza, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        name_litchi = Label(f4, text="Lichi", font=("Arial", 15, "bold"), bg=background, fg="white")
        name_litchi.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        entry_litchi = Entry(f4, width=15, textvariable=self.litchi, font=("Arial", 12, "bold"), bd=4, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)

        # ===========================bill voucher======================================================================

        f5 = LabelFrame(self.manish, bd=9, relief=GROOVE,)
        f5.place(x=1000, y=170, width=345, height=345)
        title2 = Label(f5, text="Bill Voucher", bd=12, relief=GROOVE, font=("Arial", 15, "bold"))
        title2.pack(fill= X)
        scroll_bill = Scrollbar(f5,orient = VERTICAL)
        self.txtarea = Text(f5, yscrollcommand= scroll_bill.set)
        scroll_bill.pack(side= RIGHT, fill=Y)
        scroll_bill.configure(command= self.txtarea.yview)
        self.txtarea.pack(fill= BOTH, expand= 1)

        f6 = LabelFrame(self.manish, text="Bill Menu", bd=8, relief=GROOVE, font=("Arial", 15, "bold"), fg="yellow", bg=background)
        f6.place(x=3, y=520, relwidth=1, height= 180)

        a1_label= Label(f6, text= "Total Cosmetics Price", font=("Arial", 15, "bold"),bg= background,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        a1_entry= Entry(f6, width=18, textvariable=self.cosmetic, font=("Arial", 10, "bold"), bd=4, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        a2_label = Label(f6, text="Total Grocery Price", font=("Arial", 15, "bold"), bg=background, fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        a2_entry = Entry(f6, width=18, textvariable=self.grocery, font=("Arial", 10, "bold"), bd=4, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        a3_label = Label(f6, text="Total Cold Drinks Price", font=("Arial", 15, "bold"), bg=background, fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        a3_entry = Entry(f6, width=18, textvariable=self.drinks, font=("Arial", 10, "bold"), bd=4, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        b1_label = Label(f6, text="Cosmetics Tax", font=("Arial", 15, "bold"), bg=background, fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        b1_entry = Entry(f6, width=18, textvariable=self.cosmetic_tax, font=("Arial", 10, "bold"), bd=4, relief=SUNKEN).grid(row=0, column=3, padx=10,pady=1)

        b2_label = Label(f6, text="Grocery Tax", font=("Arial", 15, "bold"), bg=background, fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        b2_entry = Entry(f6, width=18, textvariable=self.grocery_tax, font=("Arial", 10, "bold"), bd=4, relief=SUNKEN).grid(row=1, column=3, padx=10,pady=1)

        b3_label = Label(f6, text="Cold Drinks Tax", font=("Arial", 15, "bold"), bg=background,fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        b3_entry = Entry(f6, width=18, textvariable=self.drinks_tax, font=("Arial", 10, "bold"), bd=4, relief=SUNKEN).grid(row=2, column=3, padx=10 ,pady=1)

        fin_frame = Frame(f6, bd=10, relief=GROOVE, )
        fin_frame.place(x=780, y=3, width=560, height=90)

        total_button = Button(fin_frame,text= "Total", command=self.total, bg = "maroon", fg= "white", bd= 5, pady= 5,font=("Arial", 15,"bold"), width=9).grid(row=0, column=0, padx=5, pady= 5)
        total_button = Button(fin_frame,text= "Print Bill", command= self.bill_print, bg = "maroon", fg= "white", bd= 5, pady= 5,font=("Arial", 15,"bold"), width=9).grid(row=0, column=1, padx=5, pady= 5)
        total_button = Button(fin_frame,text= "Clear", command=self.clear_function, bg = "maroon", fg= "white", bd= 5, pady= 5,font=("Arial", 15,"bold"), width=9).grid(row=0, column=2, padx=5, pady= 5)
        total_button = Button(fin_frame,text= "Exit",command=self.exit_system, bg = "maroon", fg= "white", bd= 5, pady= 5,font=("Arial", 15,"bold"), width=9).grid(row=0, column=3, padx=5, pady= 5)

        info = Label(f6, text="If you have any query, please kindly mail me on lawlishsinam03@gmail.com. Thank You!!",
                     bd=8, relief=GROOVE, font=("Arial", 15, "bold"), fg="yellow", bg=background)
        info.place(y=105, relwidth=1)
        self.bill_top()     # to print always, we called inside init function.

    def total(self):
        self.c_s_p = (self.soup.get()* 30)
        self.c_c_p = (self.cream.get()* 120)
        self.c_w_p = (self.wash.get()* 50)
        self.c_sp_p = (self.spray.get()* 200)
        self.c_g_p = (self.gell.get()* 120)
        self.c_l_p = (self.lotion.get()* 160)
        self.total_cosmetic = float (self.c_s_p +
                                self.c_c_p+
                                self.c_w_p+
                                self.c_sp_p+
                                self.c_g_p +
                                self.c_l_p)


        self.cosmetic.set("Rs. " + str(self.total_cosmetic))
        self.c_tax = round((self.total_cosmetic*0.05),2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = (self.rice.get() * 75)
        self.g_o_p = (self.oil.get() * 180)
        self.g_d_p = (self.daal.get() * 60)
        self.g_w_p = (self.wheat.get() * 240)
        self.g_s_p = (self.sugar.get() * 75)
        self.g_t_p = (self.tea.get() * 150)

        self.total_grocery = float (self.g_r_p +
                                self.g_o_p+
                                self.g_d_p+
                                self.g_w_p+
                                self.g_s_p+
                                self.g_t_p)

        self.grocery.set("Rs. " + str(self.total_grocery))
        self.g_tax = round((self.total_grocery * 0.05),2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.d_c_p = (self.coke.get() * 45)
        self.d_s_p = (self.slice.get() * 50)
        self.d_sp_p = (self.sprite.get() * 45)
        self.d_f_p = (self.frooti.get() * 25)
        self.d_m_p = (self.maza.get() * 60)
        self.d_l_p = (self.litchi.get() * 35)

        self.total_drinks = float (self.d_c_p +
                                self.d_s_p+
                                self.d_sp_p+
                                self.d_f_p+
                                self.d_m_p+
                                self.d_l_p)

        self.drinks.set("Rs. " + str(self.total_drinks))
        self.d_tax = round((self.total_drinks*0.05),2)     # this is done for generating total bill in bill print.
        self.drinks_tax.set("Rs. "+ str(self.d_tax))

        self.total_bill_amount = float( self.total_cosmetic +
                                        self.total_grocery +
                                        self.total_drinks +
                                        self.c_tax+
                                        self. g_tax +
                                        self.d_tax)


    def bill_top(self):
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "\tWelcome to Manish Retails\n")
        self.txtarea.insert(END, f"\nBill Number :{self.bill.get()} ")
        self.txtarea.insert(END, f"\nCustomer Name :{self.name.get()} ")
        self.txtarea.insert(END, f"\nPhone Number : {self.phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\nProduct\t\tQuantity\t\tPrice")
        self.txtarea.insert(END, f"\n======================================")

    def bill_print(self):

        if self.name.get() =="" or self.phone.get() =="":
            messagebox.showerror("Error","Fill up Customer details")
        elif self.cosmetic.get()=="Rs. 0.0" and self.grocery.get()=="Rs. 0.0" and self.drinks.get()=="Rs. 0.0":
            messagebox.showerror("Error","Nothing is purchased.")
        else:
            # ************************** c ****************************************************************************
            self.bill_top()
            if self.soup.get()!=0:
                self.txtarea.insert(END, f"\nSoap\t\t{self.soup.get()}\t\t{self.c_s_p}")
            if self.cream.get()!=0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.cream.get()}\t\t{self.c_c_p}")
            if self.wash.get()!=0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.wash.get()}\t\t{self.c_w_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t\t{self.c_sp_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END, f"\nHair Gell\t\t{self.gell.get()}\t\t{self.c_g_p}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END, f"\nBody Lotion \t\t{self.lotion.get()}\t\t{self.c_l_p}")

            # ************************** c ****************************************************************************

            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.oil.get() != 0:
                self.txtarea.insert(END, f"\nOil\t\t{self.oil.get()}\t\t{self.g_o_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ************************** c ****************************************************************************

            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.slice.get() != 0:
                self.txtarea.insert(END, f"\nSlice\t\t{self.slice.get()}\t\t{self.d_s_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.d_sp_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\nFrooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\nMaza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.litchi.get() != 0:
                self.txtarea.insert(END, f"\nLitchi\t\t{self.litchi.get()}\t\t{self.d_l_p}")

            self.txtarea.insert(END, f"\n--------------------------------------")

            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCold Drinks Tax\t\t\t{self.drinks_tax.get()}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.txtarea.insert(END, f"\nTotal Amount: \t\t\tRs. {self.total_bill_amount}")   # final bill in scrollbar.
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.bill_record()

    def bill_record(self):
        op = messagebox.askyesno("Save Bill","Do you want to save bill?")
        if op>0:
            self.bill_data = self.txtarea.get("1.0", END)              # data variable get all data of txtarea.
            ab = open("Bills/" + str(self.bill.get()) + ".txt","w")
            ab.write(self.bill_data)
            ab.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill.get()} saved successfully.")
        else:
            return

    def search_bill(self):
        present = "no"
        for value in os.listdir("Bills/"):
            if value.split(".")[0] == self.search.get():
                ab = open(f"Bills/{value}", "r")
                self.txtarea.delete("1.0", END)
                for d in ab:
                    self.txtarea.insert(END, d)
                ab.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_function(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if op > 0:
            self.name.set("")
            self.phone.set("")
            self.bill.set("")
            m = random.randint(1000, 9999)
            self.bill.set(str(m))
            self.search.set("")

            self.soup.set(0)
            self.cream.set(0)
            self.wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            self.coke.set(0)
            self.slice.set(0)
            self.sprite.set(0)
            self.frooti.set(0)
            self.maza.set(0)
            self.litchi.set(0)

            self.cosmetic.set("")
            self.grocery.set("")
            self.drinks.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")
            self.bill_top()

    def exit_system(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.manish.destroy()


manish = Tk()
obj = Billing(manish)
manish.mainloop()