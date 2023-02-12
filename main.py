"""
This program provides a suggestion for an available installation date based on a set schedule and existing booked dates that are read from a CSV file. 
The read_dates_from_csv function reads the dates from the CSV file and returns them as a list of datetime objects. 
The suggest_install_date function takes the booked dates, 
the start and end dates for the search, 
the schedule start and end times, 
and an interval as input and returns the earliest available date that fits within the schedule and isn't already booked. 
The main part of the program sets the schedule start and end times, reads the booked dates, finds the earliest available date using the suggest_install_date function, and prints the result.
"""

import csv
from datetime import datetime, timedelta

def read_dates_from_csv(file_path):
    """
    Reads dates from a CSV file and returns them as a list of datetime objects
    """
    dates = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dates.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
    return dates

def suggest_install_date(booked_dates, start_date, end_date, schedule_start, schedule_end, interval):
    """
    Suggests an available install date based on a set schedule and existing booked dates
    """
    schedule = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() >= 0 and current_date.weekday() <= 4:
            schedule.append(current_date.strftime('%Y-%m-%d %H:%M:%S'))
        current_date += timedelta(days=1)

    for date in schedule:
        dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if dt >= schedule_start and dt <= schedule_end and dt not in booked_dates:
            return dt
    return None

if __name__ == '__main__':
    # Schedule start and end times
    schedule_start = datetime.strptime('2023-02-06 08:00:00', '%Y-%m-%d %H:%M:%S')
    schedule_end = datetime.strptime('2023-02-06 16:00:00', '%Y-%m-%d %H:%M:%S')
    interval = timedelta(hours=1)

    # Read booked dates from CSV file
    booked_dates = read_dates_from_csv('booked_dates.csv')

    # Find the earliest available date
    start_date = min(booked_dates) if booked_dates else datetime.now()
    end_date = start_date + timedelta(days=365)
    suggested_date = suggest_install_date(booked_dates, start_date, end_date, schedule_start, schedule_end, interval)

    # Print the suggested date
    if suggested_date:
        print("The earliest available date is:", suggested_date.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("No available dates found.")
