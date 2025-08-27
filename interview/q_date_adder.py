# Python
import datetime
from typing import Any


# BigO(n)
def add_days_to_date(date: Any, diapason: int, periods: int) -> list:
    converted_date = datetime.datetime.strptime(str(date), "%Y-%m-%d")
    result = [date]
    months = dict()
    months[int(date.split('-')[1])] = 1

    for item in range(periods - 1):
        added_date = converted_date + datetime.timedelta(days=diapason)
        formatted_date = added_date.strftime("%Y-%m-%d")
        current_month = int(formatted_date.split('-')[1])

        if months.get(current_month) is None:
            result.append(formatted_date)
            return result

        if months.get(current_month) < 2:
            months[current_month] = months.get(current_month) + 1
            result.append(formatted_date)
        else:
            converted_date = added_date.replace(day=1, month=(added_date.month + 1))
            result.append(converted_date.strftime("%Y-%m-%d"))
            months[int(converted_date.strftime("%Y-%m-%d").split('-')[1])] = 1

    return result


res = add_days_to_date("2024-01-01", 15, 6)
# res = add_days_to_date("2024-01-20", 15, 6)

# Additional tests
# res = add_days_to_date("2024-01-17", 15, 6)
# res = add_days_to_date("2024-01-2", 15, 6)
print(res)
