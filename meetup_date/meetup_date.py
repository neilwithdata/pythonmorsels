from datetime import date, timedelta


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=3):
    first_day = date(year, month, 1)

    days = weekday - first_day.weekday()
    if days < 0:
        days += 7

    weekdays = [first_day + timedelta(days=days)]
    while True:
        next_weekday = weekdays[-1] + timedelta(days=7)
        if next_weekday.month == month:
            weekdays.append(next_weekday)
        else:
            break

    if nth > 0:
        return weekdays[nth - 1]
    else:
        return weekdays[nth]
