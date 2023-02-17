from tkinter import *
from tkinter.ttk import Treeview
from utils.deposit import insert_data_deposit
from utils.validation import validation_data


#insert data in table
def click_btn():
    if validation_data(count_months_entry.get(), percent_entry.get(), summ_entry.get()):
        for i in data_table.get_children():
                    data_table.delete(i)
        insert_data_deposit(data_table, int(count_months_entry.get()), float(summ_entry.get()), float(percent_entry.get()))
    # if validation_credit_data(count_months_entry.get(), percent_entry.get(), summ_entry.get()):
    #     if var_loans.get() == 'Аннуитетный':
    #         for i in data_table.get_children():
    #             data_table.delete(i)
    #         insert_data_annuity_loan(data_table, int(count_months_entry.get()), float(percent_entry.get()), int(summ_entry.get()))
    #     else:
    #         for i in data_table.get_children():
    #             data_table.delete(i)
    #         insert_data_differentiated_loan(data_table, int(count_months_entry.get()), float(percent_entry.get()), int(summ_entry.get()))


#main window
win = Tk()
win.title("Bankster")
win.geometry('1280x720')

#data frame - block with user's data
data_frame = Frame(win)
data_frame.pack()


#Table block
#table frame - block with iloan information
table_frame = Frame(win)
table_frame.pack()


table_scroll = Scrollbar(table_frame)
table_scroll.pack(side=RIGHT, fill=Y)


#create table
data_table = Treeview(table_frame, yscrollcommand=table_scroll.set)
data_table.pack()
table_scroll.config(command=data_table.yview)


data_table['columns'] = ('month', 'deposit', 'income')


#create column
data_table.column("#0", width=0,  stretch=NO)
data_table.column("month",anchor=CENTER, width=300)
data_table.column("deposit",anchor=CENTER, width=300)
data_table.column("income",anchor=CENTER, width=300)


#create heading
data_table.heading("#0",text="",anchor=CENTER)
data_table.heading("month",text="Месяц",anchor=CENTER)
data_table.heading("deposit",text="Депозит",anchor=CENTER)
data_table.heading("income",text="Поступление",anchor=CENTER)


label_percent = Label(data_frame, text='Введите процентную ставку')
percent_entry = Entry(data_frame)
label_percent.pack()
percent_entry.pack()


label_months = Label(data_frame, text='Кол-во месяцев')
count_months_entry = Entry(data_frame)
label_months.pack()
count_months_entry.pack()


label_summ = Label(data_frame, text='Сумма кредита')
summ_entry = Entry(data_frame)
label_summ.pack()
summ_entry.pack()


btn_sub = Button(data_frame, text='Рассчитать', command=click_btn)
btn_sub.pack()





if __name__ == '__main__':
    win.mainloop()