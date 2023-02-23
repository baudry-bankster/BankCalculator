from tkinter.ttk import Treeview


def to_price(number: float):
    if number != 0:
        res = str(number).split('.')[1]
        if len(res) < 2:
            return str(number) + '0'
        else:
            return str(number)
    return str(number)


def differentiated_loan(months: int, percent: float, summ: float):
    result = []
    pays = []
    body_credit = summ / months
    for _ in range(months):
        if summ < body_credit:
            pay = round(summ + (summ * percent / 1200), 2)
            summ = 0
            pays.append(pay)
        else:
            pay = round(body_credit+(summ * percent / 1200), 2)
            summ -= body_credit
            pays.append(pay)
        result.append((_ + 1, pay, round(summ, 2)))

    return result, sum(pays)


def annuity_loan(months: int, percent: float, summ: float):
    percent = percent /1200
    ak = (percent * (1 + percent) ** months) / (((1 + percent) ** months) - 1)
    return round(summ * ak, 2), round(summ * ak * months, 2)


def insert_data_differentiated_loan(table: Treeview, months: int, percent: float, summ: float):
    data, pays = differentiated_loan(months, percent, summ)
    for i in range(months):
        table.insert(parent='', index='end', iid=i, text='', values=[data[i][0], to_price(data[i][1]), to_price(data[i][2])])

    table.insert(parent='', index='end', iid=months, text='', values=('',f'Общая сумма: {to_price(round(pays, 2))}',f'Переплата:{to_price(round(pays - summ, 2))}',''))


def insert_data_annuity_loan(table: Treeview, months: int, percent: float, summ: float):
    pay, common_summ = annuity_loan(months, percent, summ)

    table.insert(parent='', index='end', iid=months, text='', values=(f'Сумма платежа: {to_price(pay)}',f'Общая сумма:{to_price(common_summ)}',f'Переплата:{to_price(round(common_summ - summ, 2))}', ''))
