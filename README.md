# subway-pos-system-using-tkinter

1.First identify the algorithms.
Ans: The POS system is basically a point of system which take items and take their quantities which were declared by the customer in input field. To calculate the total it sum up the price of all the selected items and add GST and other service charges. Then it calculate the total and final price of all the items including other charges and then print them in a receipt section and print all the required details with date and time.

2.Write steps wiseAlgorithm.
Ans: Step 1: START
Step 2: declare root = Tk()
Step 3:declare objects of class Subway
Step 4:declare checkbuttons and values of Deal1, Deal2, Deal3, Deal4, Deal5, Deal6, Steak & Cheese, Italian BMT, Peri Peri Chicken, Chicken Tikka, Chicken Fajita, Turkey Breast, Oven Roasted Chicken and Bar B Q Chicken and chec  quantity and multiply Quantity with Price.
Step 5:store values of Deal1, Deal2, Deal3, Deal4, Deal5, Deal6, Steak & Cheese, Italian BMT, Peri Peri Chicken, Chicken Tikka, Chicken Fajita, Turkey Breast, Oven Roasted Chicken and Bar B Q Chicken and sum up their obtained value.
Step 6:store output in a variable SubTotal inmethods.
Step 7: declare value of items PaidGST by multiplying total with 13%.Step 8:store value of the sum total and items.PaidGST and service charges in Total Price.
Step 9:print total price, PaidGST, ServiceCharges,  Total in entry field.
Step 10:get all the required values and compile it.
Step 11:print values of Deal1, Deal2, Deal3, Deal4, Deal5, Deal6, Steak & Cheese, Italian BMT, Peri Peri Chicken, Chicken Tikka, Chicken Fajita, Turkey Breast, Oven Roasted Chicken and Bar B Q Chicken (only selected) and CostofDeals, Costof6”inchSub, SubTotal, PaidGST, ServiceCharge and TotalPrice.
Step 12:destroy root
Step 13:iExit() is used to produce a messagebox and to destroy the entire window.
Step 14:Reset() is used to reset all the values to 0 and remove the entire data.
Step 15:Reciept() is used to print all the quantities and price on a receipt.
Step 16:CostofItems() is used to calculate the total amount and to show all the values.
Step 17:END

3.Make Psuedo Code:
Ans: Main class of operation is created
Class Operation
  FUNCTION Reciept()
    It is used to print the prices and quantities and total amount in the textbox.FUNCTION iExit()It gives a messagebox to confirm exit and destroy the window.
  FUNCTION Reset()
    It reset all the set values and reset all the values to 0.
  FUNCTION CostofItems()
    It is used to print CostofDeals, Costof6’inchSubs, ServiceCharge, PaidGST, SubTotal and TotalPrice.
Now we make a child class and inherit functions on our defined buttons
Class Subway(Operation)
  FUNCTION __init__ takes 1 argument window
    We set window geometry
    We set a logo for window “logo.png”
    We set a title for a window “Subway.Pk”
    Checkbuttons are defined for deals and flavors to select and quantitywas set in the text area given ahead 
    Now we assign values to variables
    Now we declare few frames like TopFrame, MenuFrame, DealFrame, CalFrame, RecieptFrame, Rec_CalFrame, FlavorFrame etc.
    Now we define labels and entry boxes wher we print values
    Now we define different functions and connect them with the functions defined above.
    We add radiobuttons for Cash on Delivery, Card Payment and online Payment.
Now we call root = Tk()
And call the class using a variable
