import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI




lt = LibreTranslateAPI("https://translate.argosopentech.com/")
# # print(lt.languages())
language_name  = [language['name'] for language in lt.languages()]
language_code =  {lang['name']:lang['code']  for lang in lt.languages()}
# # print(language_name)



app = tk.Tk()
app.title('translator app')
app.geometry('800x500')
app.config(background='white')

def translation():
   out_put =  lt.translate(input_text.get('1.0', tk.END), language_code[input_combo.get()], language_code[output_combo.get()])
   output_text.delete('1.0', tk.END)
   output_text.insert(tk.END,out_put)

def clear():
   output_text.delete('1.0', tk.END)
   input_text.delete('1.0', tk.END)
   

title = tk.Label(app, text='welcome', bg='white', font=18, width=20)
title.place(x=150,y=1)

input_label = tk.Label(app, text='enter text', bg='white', font=('bold',14))
input_label.place(x=85, y=50)

input_combo = ttk.Combobox(app, width=26, values=language_name)
input_combo.place(x=50,y=80)
input_combo.set('choose language')

input_text = tk.Text(app, width=40, height=15, bd=2)
input_text.place(x= 5, y=120)


output_label = tk.Label(app, text='enter text', bg='white', font=('bold',14))
output_label.place(x=565, y=50)

output_combo = ttk.Combobox(app, width=26, values=language_name)
output_combo.place(x=530,y=80)
output_combo.set('choose language')

output_text = tk.Text(app, width=40, height=15, bd=2)
output_text.place(x= 460, y=120)


translate_btn = tk.Button(app, text='translate',width=11, height=1, background='brown', font=12, fg='white', command=translation)
translate_btn.place(x=340, y=220)

clear_btn = tk.Button(app, text='clear',width=11, height=1, background='brown', font=12, fg='white', command=clear)
clear_btn.place(x=340, y=260)



app.mainloop()

