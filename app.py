import random
import sys
import tkinter as tk
from tkinter import ttk

class App():
    WIDTH = 600
    HEIGHT = 500

    def __init__(self):
        self.operators = ['×', '/', '+', '-']

        self.root = tk.Tk()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')

        content = tk.Frame(self.root)
        content.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="c")

        self.generate = tk.Button(content, text="Vytvoř příklad", background="blue", fg="white", font=("Arial", 20), command=self.generate_numbers)
        self.generate.pack(side=tk.TOP, pady=15)

        excercise = ttk.Frame(content, width=100)
        excercise.pack(side=tk.TOP)
        
        self.numberl = ttk.Label(excercise, text='', font=("Arial", 35), width=2, relief="groove", anchor="c")
        self.numberl.pack(side=tk.LEFT)
        
        self.operator_box = ttk.Label(excercise, text='', font=("Arial", 35), width=1)
        self.operator_box.pack(side=tk.LEFT)

        self.number2 =ttk.Label(excercise, text='', font=("Arial", 35), width=2, relief="groove", anchor="c")    
        self.number2.pack(side=tk.LEFT)


        self.answer = tk.StringVar()
        self.answer_entry = ttk.Entry(content, textvariable=self.answer,font=("Arial", 35), width=5, justify='center')
        self.answer_entry.pack(side=tk.TOP, pady=15)
        self.answer_entry.bind('<KeyPress>', lambda e: self.check.configure(state=tk.NORMAL)) 

        self.check = tk.Button(content, text="Zkontroluj", background="red", font=("Arial", 20), state=tk.DISABLED ,command=self.check_result)
        self.check.pack(side=tk.TOP, pady=15)

        self.response =tk.Label(content, text='', font=("Arial", 35))
        self.response.pack(side=tk.TOP, pady=15)

        self.end = tk.Button(content, text="Konec", font=("Arial", 15), command=self.exit)
        self.end.pack(side=tk.TOP, pady=25)

        self.root.mainloop()

    def exit(self):
        self.root.destroy()
        sys.exit(0)

    def generate_numbers(self):
        self.operator = random.choice(self.operators)
        self.operator_box["text"] = self.operator
        self.response["text"]=''
        self.answer_entry["state"]=tk.NORMAL
        self.answer_entry.delete(0, 'end')
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.numberl["text"] = str(self.num1)
        self.number2["text"] = str(self.num2)
        self.generate['state'] = tk.DISABLED
    
    def check_result(self):
        try: 
            answer = round(float(self.answer.get()), 1)
        except Exception as e:
            answer = None
            print(e)
        
        match self.operator:
            case '-': result = self.num1 - self.num2
            case '+': result = self.num1 + self.num2
            case '/': result = self.num1 / self.num2
            case '×': result = self.num1 * self.num2

        if answer == round(result, 1):
            self.generate['state'] = tk.NORMAL
            self.check["state"]=tk.DISABLED
            self.answer_entry["state"]=tk.DISABLED
            self.response["text"] = "Správně :)" 
            self.response["fg"] = "green" 

        else:
            self.generate['state'] = tk.DISABLED
            self.answer_entry.delete(0, 'end')
            self.response["text"] = "Špatně :("
            self.response["fg"] = "red" 

        
if __name__ == "__main__":
    app = App()