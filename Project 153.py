from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.title("Project 153")
pass_input = Entry(root)
guess_pass = Label(root)
generated_pass = Label(root)
generated_pass.place(relx = 0.5, rely = 0.5, anchor = CENTER)
guess_pass.place(relx = 0.5, rely = 0.4, anchor = CENTER)
pass_input.place(relx = 0.5, rely = 0.2, anchor = CENTER)
array_3d = [[[10, 11, 12, 13, 14], ["apple", "pear", "pineapple"], ["@", "&", "*"]]]

def password() :
    guess_pass["text"] = "The guessed password is : " + pass_input.get()
    ran_no1 = random.randint(0,5)
    ran_no2 = random.randint(0,3)
    ran_no3 = random.randint(0,3)
    letter1 = str(array_3d[0][0][ran_no1])
    letter2 = array_3d[0][1][ran_no2]
    letter3 = array_3d[0][2][ran_no3]
    generated_pass["text"] = "The real password is : " + letter1 + letter2 + letter3
    
btn = Button(root, text = "Password", command = password)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)
root.mainloop()