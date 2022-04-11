from tkinter import *

from tkinter.font import *


# start

window = Tk()



# Specify a location on the page
width = window.winfo_screenwidth()
height = window.winfo_screenheight()


# Display the project on the page

window.geometry('%dx%d' % (width, height))


window.grid_columnconfigure(0, weight=2)

window.grid_columnconfigure(1, weight=3)


window.grid_rowconfigure(0, weight=1)


window.state('zoomed') # maximize

# padding
pad_x = 5
pad_y = 5

# title
window.title('نرم افزار مدیریت رستوران')


# font size

vazir_font = Font(family='Arial', size=16)



#----------Invoice frames------------------------------------------------------


# receipt_frame
receipt_frame = LabelFrame(window, text='صورت حساب', font=vazir_font, padx=pad_x, pady=pad_y)
receipt_frame.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

receipt_frame.grid_rowconfigure(1, weight=1)
receipt_frame.grid_columnconfigure(0, weight=1)

entry_order_number = Entry(receipt_frame, font=vazir_font, width=10, justify='center')
entry_order_number.grid(row=0, column=0)

list_box = Listbox(receipt_frame)
list_box.grid(row=1, column=0, sticky='nsew', padx=pad_x, pady=pad_y)


# Box list buttons
list_box_frame = LabelFrame(receipt_frame)
list_box_frame.grid(row=2, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

list_box_frame.grid_columnconfigure(0, weight=1)
list_box_frame.grid_columnconfigure(1, weight=1)
list_box_frame.grid_columnconfigure(2, weight=1)
list_box_frame.grid_columnconfigure(3, weight=1)

button_delete = Button(list_box_frame, text='حذف سطر', font=vazir_font)
button_delete.grid(row=0, column=0, sticky='nsew')

button_new = Button(list_box_frame, text=' فاکتور جدید', font=vazir_font)
button_new.grid(row=0, column=1, sticky='nsew')

button_add = Button(list_box_frame, text='+', font=vazir_font)
button_add.grid(row=0, column=2, sticky='nsew')

button_minus = Button(list_box_frame, text=' -', font=vazir_font)
button_minus.grid(row=0, column=3, sticky='nsew')



# menu frame
menu_frame = LabelFrame(window, text='منو نوشیدنی و غذاها', font=vazir_font, padx=pad_x, pady=pad_y)
menu_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=2)

menu_frame.grid_rowconfigure(0, weight=1)

# Drink frame
drink_frame = LabelFrame(menu_frame, text="نوشیدنی ها", padx=pad_x, pady=pad_y)
drink_frame.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

# Food frame
food_frame = LabelFrame(menu_frame, text=" غذا ها", padx=pad_x, pady=pad_y)
food_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)


# button frame
buttons_frame = LabelFrame(window, font=vazir_font, padx=pad_x, pady=pad_y)
buttons_frame.grid(row=1, column=1, padx=pad_x, pady=pad_y)


button_exit = Button(buttons_frame, text='خروج')
button_exit.grid(row=0, column=0)

button_calculate = Button(buttons_frame, text='ماشین حساب')
button_calculate.grid(row=0, column=1)





# end

window.mainloop()