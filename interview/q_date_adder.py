import datetime
from typing import Any


# BigO(n^2)
def date_adder(date: Any, diapason: int, periods: int) -> list:
    converted_date = datetime.datetime.strptime(str(date), "%Y-%m-%d")
    pre_result = [date]
    months = dict()
    months[int(date.split('-')[1])] = 1
    for i in range(periods - 1):
        added_date = converted_date + datetime.timedelta(days=diapason * (i + 1))
        formatted_date = added_date.strftime("%Y-%m-%d")
        current_iter = int(formatted_date.split('-')[1])
        tmp = months.get(current_iter) if months.get(current_iter) else 0
        months[current_iter] = 0

        for key, value in months.items():
            if key == current_iter:
                if tmp < 2:
                    months[key] = tmp + 1
                    pre_result.append(formatted_date)
                else:
                    pre_result.append(added_date.replace(day=1, month=(added_date.month + 1)).strftime("%Y-%m-%d"))
                    added_date = added_date.replace(day=1, month=(added_date.month + 1)).strftime("%Y-%m-%d")
            else:
                if tmp == 1:
                    return pre_result

    return pre_result


res = date_adder("2024-01-01", 15, 6)
# res = date_adder("2024-01-20", 15, 6)
print(res)
