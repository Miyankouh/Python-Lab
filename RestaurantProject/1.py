from tkinter import *
from tkinter.font import *
import os

#region 
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
        self.cursor.execute("SELECT * FROM table_menu WHERE is_food = ?" , is_food)
        result = self.cursor.fetchall()
        return result
    
############################################################################# End of DB
#endregion

#region عمومی
if os.path.isfile('restaurant.db') == False:
    db = Database('restaurant.db')
    db.insert(1, 'چلومرغ' , 22000, True)
    db.insert(2,'زرشک پلو ساده',17000, True)
    db.insert(3,'باقالی پلو با گوشت',67000,True)
    db.insert(4,'نوشابه قوطی',3000,False)
    db.insert(5,'نوشابه خانواده',5000,False)
    db.insert(6,'دوغ قوطی',4000,False)

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d' %(width,height))

window.grid_columnconfigure(0,weight=2)
window.grid_columnconfigure(1, weight=3)

pad_x = 5
pad_y = 5

window.grid_rowconfigure(0,weight=1)

window.state('zoomed')  # maximize
window.title('نرم افزار مدیریت رستوران')

vazir_font = Font(family='Vazir', size=16)
#endregion

#region صورتحساب
# ********************************************* فریم صورتحساب
receipt_frame = LabelFrame(window , text='صورتحساب' , font = vazir_font , padx=pad_x,pady=pad_y)
receipt_frame.grid(row=0,column=0,sticky='nsew', padx=pad_x,pady=pad_y)

receipt_frame.grid_rowconfigure(1,weight=1)
receipt_frame.grid_columnconfigure(0,weight=1)

entry_order_num = Entry(receipt_frame, font=vazir_font,width=10,justify='center')
entry_order_num.grid(row=0,column=0)

list_box = Listbox(receipt_frame)
list_box.grid(row=1,column=0,sticky='nsew', padx=pad_x,pady=pad_y)

# ------- فریم دکمه های لیست باکس
listbox_buttons_frame = LabelFrame(receipt_frame)
listbox_buttons_frame.grid(row=2,column=0,sticky='nsew',padx=pad_x,pady=pad_y)

listbox_buttons_frame.grid_columnconfigure(0,weight = 1)
listbox_buttons_frame.grid_columnconfigure(1,weight = 1)
listbox_buttons_frame.grid_columnconfigure(2,weight = 1)
listbox_buttons_frame.grid_columnconfigure(3,weight = 1)


button_delete = Button(listbox_buttons_frame,text='حذف سطر', font=vazir_font)
button_delete.grid(row=0,column=0,sticky='nsew')

button_new = Button(listbox_buttons_frame,text='فاکتور جدید', font=vazir_font)
button_new.grid(row=0,column=1,sticky='nsew')

button_add = Button(listbox_buttons_frame,text='+', font=vazir_font)
button_add.grid(row=0,column=2,sticky='nsew')


button_minus = Button(listbox_buttons_frame,text='-', font=vazir_font)
button_minus.grid(row=0,column=3,sticky='nsew')
#endregion

#region منوها
# ********************************************* فریم منو
menu_frame = LabelFrame(window , text='منو نوشیدنی وغذا'  , font=vazir_font, padx=pad_x,pady=pad_y)
menu_frame.grid(row=0,column=1,sticky='nsew', padx=pad_x,pady=pad_y)

menu_frame.grid_columnconfigure(0,weight=1)
menu_frame.grid_columnconfigure(1,weight=2)

menu_frame.grid_rowconfigure(0,weight=1)

#---- فریم نوشیدنی
drink_frame = LabelFrame(menu_frame , text='نوشیدنی ها', padx=pad_x,pady=pad_y)
drink_frame.grid(row=0,column=0,sticky='nsew', padx=pad_x,pady=pad_y)

#---- فریم غذا
food_frame = LabelFrame(menu_frame, text='غذاها', padx=pad_x,pady=pad_y)
food_frame.grid(row=0,column=1,sticky='nsew', padx=pad_x,pady=pad_y)
#endregion

#region دکمه ها
# ********************************************* فریم دکمه ها
buttons_frame = LabelFrame(window,font=vazir_font, padx=pad_x,pady=pad_y)
buttons_frame.grid(row=1,column=1, padx=pad_x,pady=pad_y)

button_exit=Button(buttons_frame,text='خروج',font=vazir_font)
button_exit.grid(row=0,column=0)

button_calculator = Button (buttons_frame,text='ماشین حساب' , font=vazir_font)
button_calculator.grid(row=0,column=1)
#endregion


window.mainloop()
