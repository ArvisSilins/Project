import tkinter as tk
import os
app=tk.Tk()

def open_app():
    os.system('python daily.py')

    
app.title('Anime ko skatīties')
button = tk.Button(app, text='Sākt', width=25, command=open_app)
button.pack()
app.mainloop()
