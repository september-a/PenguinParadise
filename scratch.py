import tkinter as tk 

root = tk.Tk()
def switch_to_display():
    text = entry.get()

    text_widget.insert('1.0',text)

    entry.grid_forget()

    text_widget.grid(row=0,column=0)

entry = tk.Entry(root)
entry.grid(row=0,column=0)

text_widget = tk.Text(root, height=1,width=20)

switch_button = tk.Button(root, text="Switch to Display", command=switch_to_display)
switch_button.grid(row=1, column=0)


root.mainloop()
