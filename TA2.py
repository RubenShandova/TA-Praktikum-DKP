import tkinter as tk
from tkinter import messagebox
import random

class MathCountingGame:
    def __init__(self):
        self.login_status = False
        self.game_running = False
        self.score = 0
        self.highest_score = self.load_highest_score()
    
    def load_highest_score(self):
        
        return 0
    
    def save_highest_score(self):
        
        pass
    
    def login(self, username, password):
       
        if username == "owner" and password == "password":
            self.login_status = True
        else:
            self.login_status = False
    
    def start_game(self):
        self.game_running = True
        self.score = 0
    
    def end_game(self):
        self.game_running = False
        messagebox.showinfo("Game Over", f"Score Anda: {self.score}")
        self.save_highest_score()
    
    def generate_question(self):
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*","^"])
        
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "^":
            result= operand1 ** operand2
    
        
        question = f"{operand1} {operator} {operand2}"
        return question, result
    
    def check_answer(self, answer, result):
        if int(answer) == result:
            self.score += 1
            return True
        else:
            return False

class GUI:
    def __init__(self, root):
        self.root = root
        self.game = MathCountingGame()
        
       
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 600
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        root.configure(bg="#FFFF00")
        
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_rowconfigure(3, weight=1)
        root.grid_rowconfigure(4, weight=1)
        root.grid_rowconfigure(5, weight=1)
        root.grid_rowconfigure(6, weight=1)
        root.grid_rowconfigure(7, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        
        
        self.username_label = tk.Label(root, text="Username:")
        self.username_entry = tk.Entry(root, width=30)
        self.password_label = tk.Label(root, text="Password:")
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.login_button = tk.Button(root, text="Login", command=self.login, width=30, bg="#4CAF50", fg="white")
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, width=30, bg="#4CAF50", fg="white")
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
        self.answer_entry = tk.Entry(root, width=30)
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, width=30, bg="#4CAF50", fg="white")
        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12))
        
        
        self.username_label.grid(row=0, column=0, pady=10, sticky=tk.E)
        self.username_entry.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)
        self.password_label.grid(row=1, column=0, pady=10, sticky=tk.E)
        self.password_entry.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        
        self.game.login(username, password)
        
        if self.game.login_status:
            self.login_button.config(state=tk.DISABLED)
            self.start_button.grid(row=3, column=0, columnspan=2, pady=10)
            self.question_label.grid(row=4, column=0, columnspan=2, pady=10)
            self.answer_entry.grid(row=5, column=0, columnspan=2, pady=10)
            self.submit_button.grid(row=6, column=0, columnspan=2, pady=10)
            self.score_label.grid(row=7, column=0, columnspan=2, pady=10)
            messagebox.showinfo("Info", "Login berhasil!")
        else:
            messagebox.showerror("Error", "Login gagal!")
    
    def start_game(self):
        if self.game.login_status:
            self.game.start_game()
            self.update_question()
            self.update_score()
            self.hide_login()  
        else:
            messagebox.showerror("Error", "Anda harus login terlebih dahulu!")
    
    def submit_answer(self):
        if self.game.game_running:
            answer = self.answer_entry.get()
            result = self.result
            if self.game.check_answer(answer, result):
                messagebox.showinfo("Jawaban Benar", "Anda menjawab dengan benar!")
            else:
                messagebox.showerror("Jawaban Salah", "Anda menjawab dengan salah!")
                
            self.answer_entry.delete(0, tk.END)
            self.update_score()
            if not self.game.game_running:  
                self.end_game()
            else:
                self.update_question()
        else:
            messagebox.showerror("Error", "Game belum dimulai, tekan start game dahulu")
    
    def update_question(self):
        question, result = self.game.generate_question()
        self.question_label.config(text=f"Question: {question}")
        self.result = result
    
    def update_score(self):
        self.score_label.config(text=f"Score: {self.game.score}")
    
    def show_login(self):
        self.username_label.grid(row=0, column=0, pady=10)
        self.username_entry.grid(row=0, column=1, pady=10)
        self.password_label.grid(row=1, column=0, pady=10)
        self.password_entry.grid(row=1, column=1, pady=10)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def hide_login(self):
        self.username_label.grid_forget()
        self.username_entry.grid_forget()
        self.password_label.grid_forget()
        self.password_entry.grid_forget()
        self.login_button.grid_forget()
    
    def end_game(self):
        self.start_button.grid_forget()
        self.question_label.grid_forget()
        self.answer_entry.grid_forget()
        self.submit_button.grid_forget()
        self.score_label.grid_forget()
        self.login_button.config(state=tk.NORMAL) 
        self.show_login()  

root = tk.Tk()
gui = GUI(root)
root.mainloop()