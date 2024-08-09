def add_time(start, duration, start_day=''):
    twelve_hr = {'AM':0, 'PM':12}
    min_overflow = 0
    
    # split start into number and AM/PM
    start_number, start_ampm = start.split()

    # split start number into hour/minute
    start_hr, start_min = time_str_to_int(start_number)
    
    # split duration into hour/minute
    duration_hr, duration_min = time_str_to_int(duration)

    # Minute addition with min overflow calculation
    display_min = start_min + duration_min
    if display_min >= 60:
        display_min -= 60
        min_overflow += 1
    if display_min < 10:
        display_min = f'0{display_min}'
    display_min = str(display_min)

    # Hour addition with AM/PM 12 hour adjustment and 60+ min overflow
    total_hr = (start_hr + duration_hr + twelve_hr[start_ampm] + min_overflow)

    # Calculate days and generate hours display string
    days = total_hr // 24
    display_hr = total_hr%24
    display_ampm = 'AM'
    
    if display_hr == 0:
        display_hr = '12'
    elif display_hr >= 12:
        display_ampm = 'PM'
        display_hr -= 12
        if display_hr == 0:
            display_hr = '12'
    display_hr = str(display_hr)

    # Generate days display string
    display_num_of_days = ''
    if days:
        if days == 1:
            display_num_of_days = ' (next day)'
        else:
            display_num_of_days = f' ({days} days later)'

    # Generate day of week display string
    display_weekday =''
    if start_day:
        display_weekday = f', {calc_weekday(days, start_day)}'

    full_display = (f'{display_hr}:{display_min} {display_ampm}{display_weekday}{display_num_of_days}')
    
    print(f'{full_display = }\n')

    return full_display


def time_str_to_int(time):
    hour, minute = time.split(':')
    return [int(hour), int(minute)]

def calc_weekday(num_of_days, start_day):
    weekdays = {'Sunday':0,
                'Monday':1,
                'Tuesday':2,
                'Wednesday':3,
                'Thursday':4,
                'Friday':5,
                'Saturday':6
                }
    start_day_number = weekdays[start_day.capitalize()]
    end_day_number = (start_day_number + num_of_days)%7
    end_day_name = day_name_lookup(end_day_number, weekdays)
    return end_day_name

def day_name_lookup(target_num, days_dict):
    for day_name, day_num in days_dict.items():
        if day_num == target_num:
            return day_name

add_time('6:30 PM', '205:12', '')
add_time('11:43 PM', '24:20', 'tueSday')


