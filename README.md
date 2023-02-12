# Installation Date Suggestion

This program provides a suggestion for an available installation date based on a set schedule and existing booked dates from a CSV file.

## Requirements

* Python 3
* csv library
* datetime library
* timedelta library

## Usage

1. Set the schedule start and end times in the schedule_start and schedule_end variables.
2. Provide a CSV file named booked_dates.csv in the same directory as the script, containing the already booked dates in the format of YYYY-MM-DD HH:MM:SS.
3. Run the script with the command python file_name.py

## Functions

## 'read_dates_from_csv'
This function reads dates from a CSV file and returns them as a list of datetime objects.

## 'suggest_install_date'
This function takes the booked dates, the start and end dates for the search, the schedule start and end times, and an interval as input and returns the earliest available date that fits within the schedule and isn't already booked.

## Output
The program outputs the earliest available date in the format YYYY-MM-DD HH:MM:SS if it is found, otherwise it outputs "No available dates found."



