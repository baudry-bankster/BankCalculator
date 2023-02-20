from tkinter.ttk import Treeview

def deposit(months: int, summ:float, percent:float):
    per_percent = percent/1200
    result = []
    for _ in range(months):
        temp  = summ
        summ = round(summ * (1 + per_percent), 2)
        income = round(summ - temp, 2)
        result.append((_ + 1, summ, income))
    return result


def insert_data_deposit(table: Treeview, months: int, summ:float, percent:float):
    data = deposit(months, summ, percent)
    for i in range(months):
        table.insert(parent='', index='end', iid=i, text='', values=data[i])
    table.insert(parent='', index='end', iid=months, text='', values=('','',f'Выгода: {round(data[-1][1] - summ, 2)}',''))


# print(deposit(12, 1000000, 12))