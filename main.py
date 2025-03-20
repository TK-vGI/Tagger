from datetime import datetime


def get_day_name():
    date_obj = datetime.utcnow()
    day_name = date_obj.strftime('%A')
    return day_name
