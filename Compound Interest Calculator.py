from tkinter import *



root=Tk()
root.title('Compound interest calculator')
root.geometry('500x370')
my_canvas = Canvas( root, width = 500 , height = 370)
my_canvas.pack(fill="both",expand=True)

def my_click():
    inv_init =  int (e_1.get())
    nr_ani = int ( e_2.get())
    interest  = float (e_3.get())
    frecventa = e_4.get()
    Suma = inv_init
    if frecventa == 'Y' :
        while nr_ani != 0:
            Suma = Suma + interest * Suma / 100
            nr_ani =  nr_ani -1
        format_Suma = "{:.2f}".format(Suma)
     

    if frecventa == 'M' :
        nr_ani = nr_ani * 12
        interest =  interest/12
        while nr_ani != 0:
            Suma = Suma + (interest * Suma) / 100
            nr_ani =  nr_ani -1
        format_Suma = "{:.2f}".format(Suma)
    
    result_text = Label(root, text="The result is : ")
    result_text_value = Label(root,text = format_Suma)
    my_canvas.create_window( 355, 90, anchor="nw",window = result_text_value)
    my_canvas.create_window( 260, 90, anchor="nw",window = result_text)
        

button_1 = Button(root, text="Calculate",command=my_click)
button_1_window = my_canvas.create_window( 215, 250 , anchor="nw", window = button_1)

e_1 = Entry ( root, width = 20 , borderwidth = 5)
e_1.insert(0,"Initial  Investment") 
entry_1_window = my_canvas.create_window ( 10, 10, anchor="nw", window = e_1 )

e_2 = Entry ( root, width = 20 , borderwidth = 5)
e_2.insert(0,"Years to compound") 
entry_2_window = my_canvas.create_window ( 10, 70, anchor="nw", window = e_2 )

e_3 = Entry ( root, width = 20 , borderwidth = 5)
e_3.insert(0,"Estimated interest") 
entry_3_window = my_canvas.create_window ( 10, 130, anchor="nw", window = e_3 )

e_4 = Entry ( root, width = 20 , borderwidth = 5)
e_4.insert(0,"Compound Frequency ") 
entry_4_window = my_canvas.create_window ( 10, 190, anchor="nw", window = e_4 )

hint_text_1 = Label(root, text = "Introduce 'Y'  for yearly compounding, or 'M' for monthly compounding", font =("Helvetica",9) )
hint_window = my_canvas.create_window ( 25, 300, anchor="nw", window=hint_text_1 )
hint_text_2 = Label(root, text = "If the intrest is not a integer, introduce it as '2.1' NOT '2,1'", font =("Helvetica",9) )
hint_window = my_canvas.create_window ( 25, 325, anchor="nw", window=hint_text_2 )



root.mainloop()