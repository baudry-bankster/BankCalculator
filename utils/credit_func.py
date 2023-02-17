from tkinter.ttk import Treeview


def differentiated_loan(months: int, percent: float, summ: int):
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


def annuity_loan(months: int, percent: float, summ: int):
    percent = percent /1200
    ak = (percent * (1 + percent) ** months) / (((1 + percent) ** months) - 1)
    return round(summ * ak, 2), round(summ * ak * months, 2)


def insert_data_differentiated_loan(table: Treeview, months: int, percent: float, summ: int):
    data, pays = differentiated_loan(months, percent, summ)
    for i in range(months):
        table.insert(parent='', index='end', iid=i, text='', values=data[i])

    table.insert(parent='', index='end', iid=months, text='', values=('',f'Общая сумма: {round(pays, 2)}',f'Переплата:{round(pays - summ, 2)}',''))


def insert_data_annuity_loan(table: Treeview, months: int, percent: float, summ: int):
    pay, common_summ = annuity_loan(months, percent, summ)

    table.insert(parent='', index='end', iid=months, text='', values=(f'Сумма платежа: {pay}',f'Общая сумма:{common_summ}',f'Переплата:{round(common_summ - summ, 2)}', ''))


if __name__ == '__main__':
    print(f"annuity loan --- {annuity_loan(12, 12, 1_000_000)}")
    print(f"differentiated loan --- {differentiated_loan(12, 12, 1_000_000)}")