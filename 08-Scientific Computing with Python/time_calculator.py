
def add_time(start:str, add, week=''):
    weeks = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday']

    start_item = start.replace(':', ' ').split(' ')
    add_item = add.split(':')

    tar_minute = int(start_item[0]) * 60 + int(start_item[1]) \
        + ( 60 * 12 if start_item[2]=='PM' else 0 ) \
        + int(add_item[0]) * 60 + int(add_item[1])

    tar_days = tar_minute // (60 * 24)
    tar_hours= (tar_minute % (60 * 24)) // 60
    tar_mins = tar_minute % 60
    tar_ampm = 'AM'
    if tar_hours >= 12:
        tar_ampm = 'PM'
        tar_hours -= 12
    tar_week = ''
    if week != '':
        wi = weeks.index( week[0].upper() + week[1:].lower() )
        tar_week = weeks[ (wi + tar_days) % 7 ]

    print( '# Returns: {}:{:02} {}'.format(tar_hours, tar_mins,tar_ampm ), end='' )
    if tar_week != '':
        print( ', ' + tar_week, end='' )
    if tar_days > 0:
        print( ' (next day)' if tar_days==1 else ' ({} days later)'.format(tar_days), end='' )
    print('')

if __name__=='__main__':
    add_time("3:00 PM", "3:10")
    add_time("11:30 AM", "2:32", "Monday")
    add_time("11:43 AM", "00:20")
    add_time("10:10 PM", "3:30")
    add_time("11:43 PM", "24:20", "tueSday")
    add_time("6:30 PM", "205:12")
    pass