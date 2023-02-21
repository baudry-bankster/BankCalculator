from tkinter import messagebox


def validation_data(months: str, percent: str, summ: str):
    try:
        if months[0] == '.' or percent[0] == '.' or summ[0] == '.':
            messagebox.showwarning('Ошибка', 'Некорректные данные - поля принимают только числовые значения')
            return False
    except:
        messagebox.showwarning('Ошибка', 'Некорректные данные - поля принимают только числовые значения')
        return False
    try:
        int(months)
    except:
        messagebox.showwarning('Ошибка', 'Поле "Кол-во месяцев" - целое число')
        return False

    try:
        float(percent)
        split_percent = percent.split('.')
        if'.' in percent and len(split_percent[1]) > 2:
            messagebox.showwarning('Ошибка', 'Поле "Процентная ставка" - в форме 7.62')
            return False
    except:
        messagebox.showwarning('Ошибка', 'Поле "Процентная ставка" - в форме 7.62')
        return False


    try:
        float(summ)
        split_summ = summ.split('.')
        if'.' in summ and len(split_summ[1]) > 2:
            messagebox.showwarning('Ошибка', 'Поле "Сумма кредита" - в форме 12345.34')
            return False
    except:
        messagebox.showwarning('Ошибка', 'Поле "Сумма кредита" - в форме 12345.34')
        return False


    if float(summ) <= 0:
        messagebox.showwarning('Ошибка', 'Поле "Сумма кредита" - не может быть отрицательным или равным 0')
        return False

    if float(percent) <= 0:
        messagebox.showwarning('Ошибка', 'Поле "процентная ставка" - не может быть отрицательным')
        return False

    if int(months) <= 0:
        messagebox.showwarning('Ошибка', 'Поле "Кол-во месяцев" - целое положительное число, которое больше нуля')
        return False


    return True