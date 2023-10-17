from tkinter import *
import random
import time
from tkinter import messagebox

#--------------------------------------------------Functions For Buttons--------------------------------------
class Operation():
    def iExit(self):
        iExit = messagebox.askyesno("Exit Subway.Pk", "Are you sure? Your entire data will be lost.")
        if iExit > 0:
            root.destroy()
            return


    def CostofItem(self):
        Item1 = float(self.E_Deal1.get())
        Item2 = float(self.E_Deal2.get())
        Item3 = float(self.E_Deal3.get())
        Item4 = float(self.E_Deal4.get())
        Item5 = float(self.E_Deal5.get())
        Item6 = float(self.E_Deal6.get())

        Item7 = float(self.E_Flavor1.get())
        Item8 = float(self.E_Flavor2.get())
        Item9 = float(self.E_Flavor3.get())
        Item10 = float(self.E_Flavor4.get())
        Item11 = float(self.E_Flavor5.get())
        Item12 = float(self.E_Flavor6.get())
        Item13 = float(self.E_Flavor7.get())
        Item14 = float(self.E_Flavor8.get())

        PriceofDeals = (Item1 * 999) + (Item2 * 750) + (Item3 * 375) + (Item4 * 180) + (Item5 * 3500) + (Item6*180) 
        Priceof6inchSub = (Item7 * 420) + (Item8 * 420) + (Item9 * 380) + (Item10 * 310) + (Item11 * 350) + \
                            (Item12*380) + (Item13*310) + (Item14*350)

        DealsPrice = "Rs. "+ str(PriceofDeals)
        SubsPrice = "Rs. "+str(Priceof6inchSub)
        self.CostofDeals.set(DealsPrice)
        self.Cost6inchSub.set(SubsPrice)
        SC = "Rs. "+str(150)
        self.ServiceCharge.set(SC) 

        SubTotal_Items = "Rs. "+ str(PriceofDeals+Priceof6inchSub+150)
        self.SubTotal.set(SubTotal_Items)

        GST = "Rs. "+ str(((PriceofDeals+Priceof6inchSub+150)*13)/100)
        self.PaidGST.set(GST)
        TT = (((PriceofDeals+Priceof6inchSub+150)*13)/100)
        TP = "Rs. "+ str((PriceofDeals+Priceof6inchSub+150+TT))
        self.TotalPrice.set(TP)

    def chkDeal1(self):
        if (self.var1.get() == 1):
            self.txtDeal1.configure(state=NORMAL)
            self.txtDeal1.focus()
            self.txtDeal1.delete('0', END)
            self.E_Deal1.set("")
            try:
                int(self.var1.get())
            except TclError:
                messagebox.showerror("Error!", "Sorry Sir, You can only enter quantity in numbers.")
        elif (self.var1.get() == 0):
            self.txtDeal1.configure(state=DISABLED)
            self.E_Deal1.set("0")
    def chkDeal2(self):
        if (self.var2.get() == 1):
            self.txtDeal2.configure(state=NORMAL)
            self.txtDeal2.focus()
            self.txtDeal2.delete('0', END)
            self.E_Deal2.set("")
        elif (self.var2.get() == 0):
            self.txtDeal2.configure(state=DISABLED)
            self.E_Deal2.set("0")
    def chkDeal3(self):
        if (self.var3.get() == 1):
            self.txtDeal3.configure(state=NORMAL)
            self.txtDeal3.focus()
            self.txtDeal3.delete('0', END)
            self.E_Deal3.set("")
        elif (self.var3.get() == 0):
            self.txtDeal3.configure(state=DISABLED)
            self.E_Deal3.set("0")
    def chkDeal4(self):
        if (self.var4.get() == 1):
            self.txtDeal4.configure(state=NORMAL)
            self.txtDeal4.focus()
            self.txtDeal4.delete('0', END)
            self.E_Deal4.set("")
        elif (self.var4.get() == 0):
            self.txtDeal4.configure(state=DISABLED)
            self.E_Deal4.set("0")
    def chkDeal5(self):
        if (self.var5.get() == 1):
            self.txtDeal5.configure(state=NORMAL)
            self.txtDeal5.focus()
            self.txtDeal5.delete('0', END)
            self.E_Deal5.set("")
        elif (self.var5.get() == 0):
            self.txtDeal5.configure(state=DISABLED)
            self.E_Deal5.set("0")
    def chkDeal6(self):
        if (self.var6.get() == 1):
            self.txtDeal6.configure(state=NORMAL)
            self.txtDeal6.focus()
            self.txtDeal6.delete('0', END)
            self.E_Deal6.set("")
        elif (self.var6.get() == 0):
            self.txtDeal6.configure(state=DISABLED)
            self.E_Deal6.set("0")

    def chkFlavor1(self):
        if (self.var7.get() == 1):
            self.txtFlavor1.configure(state=NORMAL)
            self.txtFlavor1.focus()
            self.txtFlavor1.delete('0', END)
            self.E_Flavor1.set("")
        elif (self.var7.get() == 0):
            self.txtFlavor1.configure(state=DISABLED)
            self.E_Flavor1.set("0")
    def chkFlavor2(self):
        if (self.var8.get() == 1):
            self.txtFlavor2.configure(state=NORMAL)
            self.txtFlavor2.focus()
            self.txtFlavor2.delete('0', END)
            self.E_Flavor2.set("")
        elif (self.var8.get() == 0):
            self.txtFlavor2.configure(state=DISABLED)
            self.E_Flavor2.set("0")
    def chkFlavor3(self):
        if (self.var9.get() == 1):
            self.txtFlavor3.configure(state=NORMAL)
            self.txtFlavor3.focus()
            self.txtFlavor3.delete('0', END)
            self.E_Flavor3.set("")
        elif (self.var9.get() == 0):
            self.txtFlavor3.configure(state=DISABLED)
            self.E_Flavor3.set("0")
    def chkFlavor4(self):
        if (self.var10.get() == 1):
            self.txtFlavor4.configure(state=NORMAL)
            self.txtFlavor4.focus()
            self.txtFlavor4.delete('0', END)
            self.E_Flavor4.set("")
        elif (self.var10.get() == 0):
            self.txtFlavor4.configure(state=DISABLED)
            self.E_Flavor4.set("0")
    def chkFlavor5(self):
        if (self.var11.get() == 1):
            self.txtFlavor5.configure(state=NORMAL)
            self.txtFlavor5.focus()
            self.txtFlavor5.delete('0', END)
            self.E_Flavor5.set("")
        elif (self.var11.get() == 0):
            self.txtFlavor5.configure(state=DISABLED)
            self.E_Flavor5.set("0")
    def chkFlavor6(self):
        if (self.var12.get() == 1):
            self.txtFlavor6.configure(state=NORMAL)
            self.txtFlavor6.focus()
            self.txtFlavor6.delete('0', END)
            self.E_Flavor6.set("")
        elif (self.var12.get() == 0):
            self.txtFlavor6.configure(state=DISABLED)
            self.E_Flavor6.set("0")
    def chkFlavor7(self):
        if (self.var13.get() == 1):
            self.txtFlavor7.configure(state=NORMAL)
            self.txtFlavor7.focus()
            self.txtFlavor7.delete('0', END)
            self.E_Flavor7.set("")
        elif (self.var13.get() == 0):
            self.txtFlavor7.configure(state=DISABLED)
            self.E_Flavor7.set("0")
    def chkFlavor8(self):
        if (self.var14.get() == 1):
            self.txtFlavor8.configure(state=NORMAL)
            self.txtFlavor8.focus()
            self.txtFlavor8.delete('0', END)
            self.E_Flavor8.set("")
        elif (self.var14.get() == 0):
            self.txtFlavor8.configure(state=DISABLED)
            self.E_Flavor8.set("0")

    def Reciept(self):
        self.txtReciept.delete("1.0", END,)
        x = random.randint(1, 300)
        randomRef = str(x)
        self.Reciept_Ref.set("OrderNo.:" + randomRef)

        self.txtReciept.insert(END, "Receipt Ref:\t\t\t\t" + self.Reciept_Ref.get() + '\n')
        self.txtReciept.insert(END, "Date: " + time.strftime('%d/%b/%y\t\t\t\t%I:%M %p', time.localtime())+ '\n')
        self.txtReciept.insert(END, "Items:\t\t\t\t" 'Quantity:\n')
        if (self.var1.get() != 0):
            self.txtReciept.insert(END, f"Deal 01:\t\t\t\t\t {self.E_Deal1.get()}\n")

        if (self.var2.get() != 0):
            self.txtReciept.insert(END, f"Deal 02:\t\t\t\t\t {self.E_Deal2.get()}\n")

        if (self.var3.get() != 0):
            self.txtReciept.insert(END, f"Deal 03:\t\t\t\t\t {self.E_Deal3.get()}\n")

        if (self.var4.get() != 0):
            self.txtReciept.insert(END, f"Deal 04:\t\t\t\t\t {self.E_Deal4.get()}\n")

        if (self.var5.get() != 0):
            self.txtReciept.insert(END, f"Deal 05:\t\t\t\t\t {self.E_Deal5.get()}\n")

        if (self.var6.get() != 0):
            self.txtReciept.insert(END, f"Deal 06:\t\t\t\t\t {self.E_Deal6.get()}\n")

        if (self.var7.get() != 0):
            self.txtReciept.insert(END, f"Steack & Cheese:\t\t\t\t\t {self.E_Flavor1.get()}\n")

        if (self.var8.get() != 0):
            self.txtReciept.insert(END, f"Italian BMT:\t\t\t\t\t {self.E_Flavor2.get()}\n")

        if (self.var9.get() != 0):
            self.txtReciept.insert(END, f"Peri Peri Chicken:\t\t\t\t\t {self.E_Flavor3.get()}\n")

        if (self.var10.get() != 0):
            self.txtReciept.insert(END, f"Turkey Breast:\t\t\t\t\t {self.E_Flavor4.get()}\n")

        if (self.var11.get() != 0):
            self.txtReciept.insert(END, f"Chicken Tikka:\t\t\t\t\t {self.E_Flavor5.get()}\n")

        if (self.var12.get() != 0):
            self.txtReciept.insert(END, f"Chicken Fajita:\t\t\t\t\t {self.E_Flavor6.get()}\n")

        if (self.var13.get() != 0):
            self.txtReciept.insert(END, f"Oven Roasted Chicken:\t\t\t\t\t {self.E_Flavor7.get()}\n")

        if (self.var14.get() != 0):
            self.txtReciept.insert(END, f"Bar B. Q. Chicken:\t\t\t\t\t {self.E_Flavor8.get()}\n")
            
        self.txtReciept.insert(END, f'Cost of Deals (Added):\t\t\t\t {self.CostofDeals.get()}\nGST Paid:\t\t\t\t {self.PaidGST.get()}\n')
        self.txtReciept.insert(END, f'Cost of 6" Subs (Added):\t\t\t\t {self.Cost6inchSub.get()}\nSub Total:\t\t\t\t {str(self.SubTotal.get())}\n')
        self.txtReciept.insert(END, f'Service Charges (Added):\t\t\t\t {self.ServiceCharge.get()}\nTotal Amount:\t\t\t\t {str(self.TotalPrice.get())}\n')
        self.txtReciept.config(state=DISABLED)

    def Reset(self):
        self.txtReciept.config(state=NORMAL)
        self.txtReciept.delete("1.0", END)
        self.PaidGST.set("")
        self.SubTotal.set("")
        self.TotalPrice.set("")
        self.CostofDeals.set("")
        self.Cost6inchSub.set("")
        self.ServiceCharge.set("")

        self.E_Deal1.set("0")
        self.E_Deal2.set("0")
        self.E_Deal3.set("0")
        self.E_Deal4.set("0")
        self.E_Deal5.set("0")
        self.E_Deal6.set("0")

        self.E_Flavor1.set("0")
        self.E_Flavor2.set("0")
        self.E_Flavor3.set("0")
        self.E_Flavor4.set("0")
        self.E_Flavor5.set("0")
        self.E_Flavor6.set("0")
        self.E_Flavor7.set("0")
        self.E_Flavor8.set("0")

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        
class Subway(Operation):
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Subway.Pk")
        self.root.configure(background = "green")

 #--------------------------------------------Variables-------------------------------------------------------------       
        self.var1= IntVar()
        self.var2= IntVar()
        self.var3= IntVar()
        self.var4= IntVar()
        self.var5= IntVar()
        self.var6= IntVar()
        self.var7= IntVar()
        self.var8= IntVar()
        self.var9= IntVar()
        self.var10= IntVar()
        self.var11= IntVar()
        self.var12= IntVar()
        self.var13= IntVar()
        self.var14= IntVar()

        self.Reciept_Ref = StringVar()
        self.PaidGST = StringVar()
        self.SubTotal = StringVar()
        self.TotalPrice = StringVar()
        self.CostofDeals = StringVar()
        self.Cost6inchSub = StringVar()
        self.ServiceCharge = StringVar()

        self.text_Input = StringVar()
        self.operator = ""

        self.E_Deal1 = IntVar()
        self.E_Deal2 = IntVar()
        self.E_Deal3 = IntVar()
        self.E_Deal4 = IntVar()
        self.E_Deal5 = IntVar()
        self.E_Deal6 = IntVar()

        self.E_Flavor1 = IntVar()
        self.E_Flavor2 = IntVar()
        self.E_Flavor3 = IntVar()
        self.E_Flavor4 = IntVar()
        self.E_Flavor5 = IntVar()
        self.E_Flavor6 = IntVar()
        self.E_Flavor7 = IntVar()
        self.E_Flavor8 = IntVar()
        self.var15 = IntVar()
        

        TopFrame = Frame(self.root, bg="white", bd=20, pady=5, relief=RIDGE)
        TopFrame.pack(side=TOP)
        # Now we are using image to show logo of Subway

        lblLogo = Label(TopFrame,image=logo)
        lblLogo.pack(side=TOP,anchor="n")
        lblTitle = Label(TopFrame,font=("Arial",16,'bold'),text="DELICIOUS FLAVOUR. AMAZING VARIETY.",fg='green', 
                              justify=CENTER)
        lblTitle.pack(side=TOP,anchor="n")
        Rec_CalFrame = Frame(self.root, bg="yellow", bd=10, relief=RIDGE)
        Rec_CalFrame.pack(side=RIGHT)
        ButtonFrame = Frame(Rec_CalFrame, bg="yellow", bd=3, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        CalFrame = Frame(Rec_CalFrame, bg="yellow", bd=6, relief=RIDGE)
        CalFrame.pack(side=TOP)
        RecieptFrame = Frame(Rec_CalFrame, bg="yellow", bd=4, relief=RIDGE)
        RecieptFrame.pack(side=BOTTOM)
        MenuFrame = Frame(self.root, bg="Green", bd=10, relief=RIDGE)
        MenuFrame.pack(side=LEFT)
        DealFrame = Frame(MenuFrame, bg="Green", bd=10)
        DealFrame.pack(side=TOP)
        PriceFrame = Frame(MenuFrame, bg="Green", bd=4)
        PriceFrame.pack(side=BOTTOM)
        DealFrame = Frame(MenuFrame, bg="Yellow", bd=10, relief=RIDGE)
        DealFrame.pack(side=LEFT)
        FlavorFrame = Frame(MenuFrame, bg="Yellow", bd=10, relief=RIDGE)
        FlavorFrame.pack(side=RIGHT)

#--------------------------------------------------Deals------------------------------------------------------
        Deal1 = Checkbutton(DealFrame, text='*DEAL 01:"Treat for 3"\n Any 3 6" Subs + 3 Drinks', variable=self.var1, 
                            onvalue=1, offvalue=0, font=("Arial",14,'bold'), bg='Yellow', fg="Green", 
                            command=self.chkDeal1).grid(row=0, sticky=W)
        Deal2 = Checkbutton(DealFrame, text='*DEAL 02:"Spring It On!"\n Any 2 6" Subs + Drinks', variable=self.var2,
                            onvalue=1, offvalue=0, font=("Arial",14,'bold'), bg='Yellow', fg="Green",
                            command=self.chkDeal2).grid(row=1, sticky=W)
        Deal3 = Checkbutton(DealFrame, text='*DEAL 03:"Eat Well... Live Fresh"\n 6" Sub + Drink', variable=self.var3,
                            onvalue=1, offvalue=0,font=("Arial",14,'bold'), bg='Yellow', fg="Green",
                            command=self.chkDeal3).grid(row=2, sticky=W)
        Deal4 = Checkbutton(DealFrame, text='*DEAL 04:"Such Main Wow!\n 6" Chicken Tikka Sub', variable=self.var4,
                            onvalue=1, offvalue=0, font=("Arial",14,'bold'), bg='Yellow', fg="Green",
                            command=self.chkDeal4).grid(row=3, sticky=W)
        Deal5 = Checkbutton(DealFrame, text='*DEAL 05:"SUBWAY CATERS"\n 15 Mini Subs + 1 Coke (2.25L)', variable=self.var5,
                           onvalue=1,offvalue=0,font=("Arial",14,'bold'), bg='Yellow', fg="Green",
                            command=self.chkDeal5).grid(row=4, sticky=W)
        Deal6 = Checkbutton(DealFrame, text='*DEAL 06:"Family Feast"\n 3 Sub + 3 Cookies + 1.5L Drink', variable=self.var6,
                            onvalue=1, offvalue=0, font=("Arial",14,'bold'), bg='Yellow', fg="Green",
                            command=self.chkDeal6).grid(row=5, sticky=W)

        """Entry Box For Deals"""
        self.txtDeal1 = Entry(DealFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                        textvariable=self.E_Deal1, state=DISABLED)
        self.txtDeal1.grid(row=0, column=1)
        self.txtDeal2 = Entry(DealFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT, 
                        textvariable=self.E_Deal2, state=DISABLED)
        self.txtDeal2.grid(row=1, column=1)
        self.txtDeal3 = Entry(DealFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT, 
                        textvariable=self.E_Deal3, state=DISABLED)
        self.txtDeal3.grid(row=2, column=1)
        self.txtDeal4 = Entry(DealFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                        textvariable=self.E_Deal4, state=DISABLED)
        self.txtDeal4.grid(row=3, column=1)
        self.txtDeal5 = Entry(DealFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                        textvariable=self.E_Deal5, state=DISABLED)
        self.txtDeal5.grid(row=4, column=1)
        self.txtDeal6 = Entry(DealFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                        textvariable=self.E_Deal6, state=DISABLED)
        self.txtDeal6.grid(row=5, column=1)

        """ Flavors """
        Flavor1 = Checkbutton(FlavorFrame, text='Steak & Cheese', variable=self.var7,onvalue=1, offvalue=0, 
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor1).grid(row=0, sticky=W)
        Flavor2 = Checkbutton(FlavorFrame, text='Italian BMT', variable=self.var8,onvalue=1, offvalue=0, 
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor2).grid(row=1, sticky=W)
        Flavor3 = Checkbutton(FlavorFrame, text='Peri Peri Chicken', variable=self.var9, onvalue=1, offvalue=0,
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor3).grid(row=2, sticky=W)
        Flavor4 = Checkbutton(FlavorFrame, text='Turkey Breast', variable=self.var10,onvalue=1, offvalue=0, 
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor4).grid(row=3, sticky=W)
        Flavor5 = Checkbutton(FlavorFrame, text='Chicken Tikka', variable=self.var11, onvalue=1,offvalue=0,
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor5).grid(row=4, sticky=W)
        Flavor6 = Checkbutton(FlavorFrame, text='Chicken Fajita', variable=self.var12,onvalue=1, offvalue=0, 
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor6).grid(row=5, sticky=W)
        Flavor7 = Checkbutton(FlavorFrame, text='Oven Roasted Chicken', variable=self.var13, onvalue=1, offvalue=0, 
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor7).grid(row=6, sticky=W)
        Flavor8 = Checkbutton(FlavorFrame, text='Bar B. Q. Chicken', variable=self.var14,onvalue=1, offvalue=0, 
                            font=("Arial",14,'bold'), bg='Yellow', fg="Green", command=self.chkFlavor8).grid(row=7, sticky=W)

        """ Entry Box For Flavors"""
        self.txtFlavor1 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor1, state=DISABLED)
        self.txtFlavor1.grid(row=0, column=1)
        self.txtFlavor2 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor2, state=DISABLED)
        self.txtFlavor2.grid(row=1, column=1)
        self.txtFlavor3 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor3, state=DISABLED)
        self.txtFlavor3.grid(row=2, column=1)
        self.txtFlavor4 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor4, state=DISABLED)
        self.txtFlavor4.grid(row=3, column=1)
        self.txtFlavor5 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor5, state=DISABLED)
        self.txtFlavor5.grid(row=4, column=1)
        self.txtFlavor6 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor6, state=DISABLED)
        self.txtFlavor6.grid(row=5, column=1)
        self.txtFlavor7 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT,
                            textvariable=self.E_Flavor7, state=DISABLED)
        self.txtFlavor7.grid(row=6, column=1)
        self.txtFlavor8 = Entry(FlavorFrame, font=("Arial",14,'bold'), bd=8, width=6, justify=LEFT, 
                            textvariable=self.E_Flavor8, state=DISABLED)
        self.txtFlavor8.grid(row=7, column=1)

        #----------------------------------------Total Price-------------------------------------------------
        lblCostofDeals = Label(PriceFrame, font=("Arial",14,'bold'), text="Cost of Deals\t", bg="Green", fg="White")
        lblCostofDeals.grid(row=0, column=0, sticky=W)
        txtCostofDeals = Entry(PriceFrame, font=("Arial",14,'bold'), bd=7, bg="white", insertwidth=2, width=10,
                                justify=RIGHT, textvariable=self.CostofDeals, state=DISABLED)
        txtCostofDeals.grid(row=0, column=1)

        lblCost6inchSub = Label(PriceFrame, font=("Arial",14,'bold'), text='Cost of 6" Sub\t', bg="Green", fg="White")
        lblCost6inchSub.grid(row=1, column=0, sticky=W)
        txtCost6inchSub = Entry(PriceFrame, font=("Arial",14,'bold'), bd=7, bg="white", insertwidth=2, width=10,
                                justify=RIGHT, textvariable=self.Cost6inchSub, state=DISABLED)
        txtCost6inchSub.grid(row=1, column=1)

        lblServiceCharge = Label(PriceFrame, font=("Arial",14,'bold'), text="Service Charge\t", bg="Green", fg="White")
        lblServiceCharge.grid(row=2, column=0, sticky=W)
        txtServiceCharge = Entry(PriceFrame, font=("Arial",14,'bold'), bd=7, bg="white", insertwidth=2, width=10,
                                justify=RIGHT, textvariable = self.ServiceCharge, state=DISABLED)
        txtServiceCharge.grid(row=2, column=1)

#-----------------------------------------------------Payment Info-----------------------------------------------------
        lblGST = Label(PriceFrame, font=("Arial",14,'bold'), text="\tPaid G.S.T\t", bg="Green", fg="White")
        lblGST.grid(row=0, column=2, sticky=W)
        txtGST = Entry(PriceFrame, font=("Arial",14,'bold'), bd=7, bg="white", insertwidth=2,  width=10,
                        justify=RIGHT, textvariable=self.PaidGST, state=DISABLED)
        txtGST.grid(row=0, column=3)

        lblSubTotal = Label(PriceFrame, font=("Arial",14,'bold'), text="\tSub Total\t", bg="Green", fg="White")
        lblSubTotal.grid(row=1, column=2, sticky=W)
        txtSubTotal = Entry(PriceFrame, font=("Arial",14,'bold'), bd=7, bg="white", insertwidth=2, width=10, 
                            justify=RIGHT, textvariable=self.SubTotal, state=DISABLED)
        txtSubTotal.grid(row=1, column=3)

        lblTotalPrice = Label(PriceFrame, font=("Arial",14,'bold'), text="\tTotal Price\t", bg="Green", fg="White")
        lblTotalPrice.grid(row=2, column=2, sticky=W)
        txtTotalPrice = Entry(PriceFrame, font=("Arial",14,'bold'), bd=7, bg="white", insertwidth=2, width=10,
                            justify=RIGHT, textvariable=self.TotalPrice, state=DISABLED)
        txtTotalPrice.grid(row=2, column=3)

#-----------------------------------------------------Reciept-----------------------------------------------------------------
        scrollbar = Scrollbar(RecieptFrame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.txtReciept = Text(RecieptFrame, width=50, height=20, bd=4, bg="white", font=("Arial",12,'bold'))
        self.txtReciept.pack(side=RIGHT)
        self.txtReciept.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.txtReciept.yview)

#----------------------------------------Buttons----------------------------------------------------
        self.btnTotal = Button(ButtonFrame, padx=16, pady=1, bd=7, fg="White", font=("Arial",14,'bold'), width=4,
                        text="Total", bg="Green", command=self.CostofItem).grid(row=0, column=0)
        self.btnReciept = Button(ButtonFrame, padx=16, pady=1, bd=7, fg="White", font=("Arial",14,'bold'), width=8,
                        text="Print Reciept", bg="Green", command=self.Reciept).grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, padx=16, pady=1, bd=7, fg="White", font=("Arial",14,'bold'), width=4,
                        text="Reset", bg="Green", command=self.Reset).grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, padx=16, pady=1, bd=7, fg="White", font=("Arial",14,'bold'), width=4,
                        text="Exit", bg="Green", command=self.iExit).grid(row=0, column=3)

#-------------------------------------------------Radio Buttons----------------------------------------------
        radio1 = Radiobutton(CalFrame, text="\tCard Payment", padx=14, variable=self.var15, value=1, bg="Yellow", 
                            font=("Arial",12,'bold'), fg="Green")
        radio1.grid(row=0, sticky=W)
        radio2 = Radiobutton(CalFrame, text="\tOnline Payment", padx=14, variable=self.var15, value=2, bg="Yellow", 
                            font=("Arial",12,'bold'), fg="Green")
        radio2.grid(row=1, sticky=W)
        radio2 = Radiobutton(CalFrame, text="\tCash on Delivery", padx=14, variable=self.var15, value=3, bg="Yellow", 
                            font=("Arial",12,'bold'), fg="Green")
        radio2.grid(row=2, sticky=W)

try:
    root = Tk()
    logo = PhotoImage(file="logo.png")
    obj = Subway(root)
    root.mainloop()

except Exception:
    messagebox.showerror("Error!", "Oops! It seems like code doesn't work properly\n Try again please.")