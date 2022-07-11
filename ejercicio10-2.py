import tkinter

windows= tkinter.Tk()

list = ['Griselda','Pia','Rufina','Beatriz','Juan Carlos','Matias','Robledo']
list_item= tkinter.StringVar(value=list)

box_list = tkinter.Listbox(windows,listvariable=list_item,bg='grey',foreground='black',selectbackground='pink')
box_list.pack(expand=True,fill='both')


windows.mainloop()

