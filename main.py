from datetime import datetime, time, timedelta
import math
import time


while True:
    today = datetime.now()

    year_christmas_day = (
        today.year + 1
        if today.day > 25 and today.month == 12
        else today.year
    )

    end_of_day = today.replace(hour=23, minute=59, second=59, microsecond=0)

    christmas_day = datetime.strptime(
       f"25/12/{year_christmas_day}", "%d/%m/%Y"
    )

    time_remaining = end_of_day - today

    days_left = math.ceil(
        (christmas_day - today).total_seconds() / 60 / 60 / 24
    )

    seconds_remaining = time_remaining.total_seconds()
    hours_remaining, seconds_remaining = divmod(seconds_remaining, 3600)
    minutes_remaining, seconds_remaining = divmod(seconds_remaining, 60)

    if today.date() == christmas_day.date():
        print("It's Christmas Day today. Merry Christmas!")
    else:
        print(
            f"There {'are' if days_left > 1 else 'is'} {days_left}"
            f" day{'s' if days_left > 1 else ''} {int(hours_remaining)} hours, {int(minutes_remaining)} minutes, "
            f"{int(seconds_remaining)} seconds left until Christmas",
        )
        time.sleep(1)
