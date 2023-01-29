import tkinter as tk
from tkinter import messagebox

class FIRST100NUM:
    def __init__(self,incomplete_nums):
        self.incomplete_nums=incomplete_nums
        self.complete_nums=set(range(1,101))
    def EXTRACT(self):
        missing_nums=self.complete_nums.difference(self.incomplete_nums)
        return missing_nums

def CustomMessageBox(missing_nums):
    top = tk.Toplevel(root)
    top.geometry("400x300")
    top.title("Result")

    label = tk.Label(top, text=f'''The missing numbers are:  
    
    {str(list(missing_nums))}''', font=("Arial", 12),wraplength=330)
    label.pack(pady=10)
    button = tk.Button(top, text="Close",font=("Arial",12) ,command=top.destroy)
    button.pack(pady=10)

def find_missing_number():
    entry_nums=entry.get()
    try:
        incomplete_nums=set(map(int,entry_nums.split(',')))
        for num in incomplete_nums:
            if num < 0 or num > 100:
                messagebox.showinfo("Error","los numeros no pueden ser menores o iguales a cero o mayores a 100")
    except:
        messagebox.showinfo("Error", "Input invalida, lo que ingreses debe ser numeros del 1 al 100 separados por coma")
    check=FIRST100NUM(incomplete_nums)
    missing_nums=check.EXTRACT()
    CustomMessageBox(missing_nums)
    #messagebox.showinfo("Result",f"Los numeros faltantes son:" + str(missing_nums))



root = tk.Tk()
root.title("Missing Number")
root.geometry("700x500")


numbers = [1,2,3,4]
labelTitle=tk.Label(root,text="Find the Missing ones API",font=("Arial",16,"bold"))
labelTitle.pack(pady=10)

label = tk.Label(root, text='''
Ingresa los numeros del 1 al 100 que tu quieras
    Estos deben estar separados por comas:
        ejemplo ( 1 , 3 , 5 , 6)
         ''',font=("Arial",14))
label.pack(pady=10)

entry = tk.Entry(root,font=("Arial", 14), width=30)
entry.pack()
entry.pack(pady=10)

button = tk.Button(root, text="Find Missing Number",font=("Arial",12), command=find_missing_number)
button.pack(pady=10)

root.mainloop()