import os
import re
from datetime import datetime as dt, timedelta
import json
from teams_app.model.meet import Meet

DIR_PATH = '/Coding/Jala/Python/teams_app/attendance_reports'
MEETING_TITLE = "Meeting Title"
TOTAL_NUMBER_PARTICIPANTS = "Total Number of Participants"
FULL_NAME = "Full Name"
last_equal = Meet()

def get_dirs(dir_path, start_date, end_date):
    date_dir = set()
    for direc in os.listdir(dir_path):
        # if os.path.isdir(dir):
        date = dt.strptime(direc, '%m%d%Y')
        if date >= start_date and date <= end_date:
            date_dir.add(direc)
        # else:
        #     continue
    return date_dir

def process_file(file, meeting_title) -> Meet: 
    new_meeting_title = get_meeting_title(file[2])
    if new_meeting_title == meeting_title:
        duration = get_duration(file[8])
        participants = get_participants(file[1])
        # print('d, p: ',duration, participants)
        global last_equal
        last_equal = Meet(title=new_meeting_title, duration=duration, participants=participants)
        # print('a')
        
    # print(last_equal)
    return last_equal

def get_token(line, search_token):
    if search_token not in line:
        return None
    return line.strip('\n').split('\t')[1]

def get_meeting_title(line):
    return get_token(line, MEETING_TITLE)

def get_participants(line):
    total_number_participants  = get_token(line, TOTAL_NUMBER_PARTICIPANTS) or -99999
    return int(total_number_participants)

def get_duration(line):
    return re.findall('\d+[h]\s\d+[m]', line)[0]


def create_new_date(date_dir, meeting_title, start_date, end_date, option):
    info = {
        'meeting_title': meeting_title,
        'data': []
    }
    type = ''
    value = 0
    match option:
        case 1:
            type = 'participants'
            value = -9999
        case 2:
            type = 'duration'
            value = "0h 0m"
    days = (end_date - start_date).days + 1
    current_day = start_date
    for _ in range(days):
        current_day_str = current_day.strftime('%m%d%Y')
        new_date={
            'date': current_day.strftime('%m/%d/%Y'),
            type: value
        }
        if current_day_str in date_dir:
            full_path = DIR_PATH+'/'+current_day_str
            files = os.listdir(full_path)
            global last_equal
            last_equal=Meet()
            for file in files:
                full_path += '/'+file
                with open(full_path, 'r', encoding='UTF-16') as file:
                    new_meeting = process_file(list(file), meeting_title).__dict__
                # print(new_meeting)
                new_date[type] = new_meeting[type]
                # print(new_meeting[type])
                full_path = DIR_PATH+'/'+current_day_str
                # print('before: ',new_date)
            # print(new_date)
        info['data'].append(new_date)
        current_day = current_day + timedelta(days=1)
            
    return json.dumps(info, indent=4)
