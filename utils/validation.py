from tkinter import messagebox


def validation_credit_data(months: str, percent: str, summ: str):
    try:
        int(months)
    except:
        messagebox.showwarning('Ошибка', 'Поле "Кол-во месяцев"')
        return False

    try:
        float(percent)
        split_percent = percent.split('.')
        if'.' in percent and len(split_percent[1]) > 2:
            messagebox.showwarning('Ошибка', 'Поле "Процентная ставка"')
            return False
    except:
        messagebox.showwarning('Ошибка', 'Поле "Процентная ставка"')
        return False


    try:
        int(summ)
    except:
        messagebox.showwarning('Ошибка', 'Поле "Сумма кредита"')
        return False

    return True