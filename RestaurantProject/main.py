from tkinter import *
from tkinter.font import *
import os

import sqlite3

#region data base class
############################################################################# DB
import sqlite3

class Database:
    def __init__(self, db):
        self.__db_name = db
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS [table_menu](
                            [ID] INT PRIMARY KEY NOT NULL UNIQUE, 
                            [name] NVARCHAR(50) NOT NULL UNIQUE, 
                            [price] INT NOT NULL,
                            [is_food] BOOL NOT NULL) WITHOUT ROWID;
                            """)
        
        self.connection.commit()
        self.connection.close()
        
        
    
    def insert(self, id, name, price,is_food):
        self.connection = sqlite3.connect(self.__db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO table_menu VALUES (? , ? , ? , ?)" , (id, name, price, is_food))       
        self.connection.commit()
        self.connection.close()
        
    
    def get_menu_items(self, is_food):
        self.connection = sqlite3.connect(self.__db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM table_menu WHERE is_food = ?" , (is_food, ))
        result = self.cursor.fetchall()
        return result
    
############################################################################# End of DB
#endregion

db = Database('restaurant.db')

if os.path.isfile('restaurant.db') == False:
    db.insert(1, 'چلومرغ', 22000, True)
    db.insert(2, 'زرشک پلو ساده', 17000, True)
    db.insert(3, 'باقالی پلو با گوشت', 67000, True)
    db.insert(4, 'نوشابه قوطی', 3000, False)
    db.insert(5, 'نوشابه خانواده', 5000, False)
    db.insert(6, 'دوغ قوطی', 4000, False)


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

#region receipt
###################################################### 

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

# Delete button in list_box
button_delete = Button(list_box_frame, text='حذف سطر', font=vazir_font)
button_delete.grid(row=0, column=0, sticky='nsew')

# new button in list_box
button_new = Button(list_box_frame, text=' فاکتور جدید', font=vazir_font)
button_new.grid(row=0, column=1, sticky='nsew')

# Add button in list_box
button_add = Button(list_box_frame, text='+', font=vazir_font)
button_add.grid(row=0, column=2, sticky='nsew')

# Minus button in list_box
button_minus = Button(list_box_frame, text=' -', font=vazir_font)
button_minus.grid(row=0, column=3, sticky='nsew')
# ###################################################### 
#endregion


# Menu frame
menu_frame = LabelFrame(window, text='منو نوشیدنی و غذاها', font=vazir_font, padx=pad_x, pady=pad_y)
menu_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=2)

menu_frame.grid_rowconfigure(0, weight=1)

# Drink frame in Menu frame
drink_frame = LabelFrame(menu_frame, text="نوشیدنی ها", padx=pad_x, pady=pad_y)
drink_frame.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)
drink_frame.grid_columnconfigure(0, weight=1)
drink_frame.grid_rowconfigure(0, weight=1)


listbox_drinks = Listbox(drink_frame, font=vazir_font, exportselection=False)
listbox_drinks.grid(sticky='nsew')
listbox_drinks.configure(justify=RIGHT)

drinks = db.get_menu_items(False)

# get data
for drink in drinks:
    listbox_drinks.insert("end", drink[1])

# Food frame in Menu frame
food_frame = LabelFrame(menu_frame, text=" غذا ها", padx=pad_x, pady=pad_y)
food_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)
food_frame.grid_columnconfigure(0, weight=1)
food_frame.grid_rowconfigure(0, weight=1)

listbox_foods = Listbox(food_frame)
listbox_foods.grid(sticky='nsew')

foods = db.get_menu_items(True)
listbox_foods.configure(justify=RIGHT, font=vazir_font, exportselection=False)

for food in foods:
    listbox_foods.insert("end", food[1])

# Button frame
buttons_frame = LabelFrame(window, font=vazir_font, padx=pad_x, pady=pad_y)
buttons_frame.grid(row=1, column=1, padx=pad_x, pady=pad_y)

# Exit in Button frame
button_exit = Button(buttons_frame, text='خروج')
button_exit.grid(row=0, column=0)

# Calculate in Button frame
button_calculate = Button(buttons_frame, text='ماشین حساب')
button_calculate.grid(row=0, column=1)





# end
window.mainloop()
