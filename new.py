import datetime
import re


# creates a list from "08:00" to "18:00"
def time_check():
    time_range_list = []
    for hour in range(8, 18):
        for minute in range(0, 60, 15):
            _time = f'{hour}:{minute}'
            time_range_list.append(_time)
    time_range_list.append('18:0')
    return time_range_list


def time_to_visit(some_list: list, time_visit: int):
    t = time_check()
    for i in some_list:
        start = f'{i[0][0].hour}:{i[0][0].minute}'
        end = f'{i[0][1].hour}:{i[0][1].minute}'
        index_start = t.index(start)
        index_end = t.index(end)+1
        del_data = t[index_start: index_end]
        for j in del_data:
            t.pop(t.index(j))

    pattern = r'(([0-9]|[0-2][0-3]|1[0-9]|0[0-9]):([0-5][0-9]|[0-9]))'
    new_lst = []
    for i in t:
        correct_time = re.findall(pattern, str(i))
        current = correct_time[0][1]
        next_hour = int(correct_time[0][1]) + time_visit
        j = i.replace(current, str(next_hour))
        if j in t:
            new_lst.append(i)
    print(new_lst)
    return new_lst


x = [
    [(datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0),)],
    [(datetime.datetime(2023, 8, 1, 10, 0), datetime.datetime(2023, 8, 1, 11, 0),)],
    [(datetime.datetime(2023, 8, 1, 13, 0), datetime.datetime(2023, 8, 1, 16, 0),)],
    ]
y = 1
time_to_visit(x, y)
