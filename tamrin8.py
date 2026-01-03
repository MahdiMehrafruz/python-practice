import tkinter as tk
from tkinter import messagebox


def get_info ():
    try:
        bill = int (ent_bill.get())
        people = int (ent_people.get())
        
        if people <= 0:
            messagebox.showerror("Error","Pls enter a positive number! ")
            return
        
        x = int (bill / people)
        messagebox.showinfo("Result", f"Each person's share : {x} Toman ")
    
    except ValueError:
        messagebox.showerror("Error", "Pls enter number!")




root = tk.Tk()
root.title ("Dong Calculator")
root.geometry ("500x400")

lbl_bill = tk.Label (root,text="Total Bill :")
lbl_bill.grid (row=0, column=0, padx=15, pady=20)

ent_bill = tk.Entry (root)
ent_bill.grid (row=0 ,column=1)


lbl_people = tk.Label (root,text="Number of People :")
lbl_people.grid (row=1, column=0, padx=10, pady=0)

ent_people = tk.Entry (root, width=15)
ent_people.grid (row=1, column=1)


btn_calculate = tk.Button (root, text="Calculate",command=get_info)
btn_calculate.grid (row=2, column=1, columnspan=5 , pady=20 )


root.mainloop()
print ("Exit...")