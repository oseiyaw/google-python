#!/usr/bin/env python3


import csv
import datetime
import requests
import os


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
FILE_NAME = "tester.csv"


def get_start_date():
  """Interactively get the start date to query for."""

  print()
  print('Getting the first start date to query for.')
  print()
  print('The date must be greater than Jan 1st, 2018')
  year = input('Enter a value for the year: ')
  month = input('Enter a value for the month: ')
  day = input('Enter a value for the day: ')
  print()

  return datetime.datetime(int(year),int(month), int(day))

def get_file():

  filename = "tester.csv"

  if not os.path.exists("tester.csv"):
        
        response = requests.get(FILE_URL)
        response.raise_for_status()

        with open("tester.csv","w", newline="",encoding="utf-8") as f:

            writer=csv.writer(f)

            for line in response.iter_lines():

                writer.writerow(line.decode("utf-8").split(','))
        print("Download complete.")
  else:
        print(f"'{filename}' already exists. Continuing...")

  return filename
       
   

def get_file_data():

  # open local csv file
  get_file()
  data_by_date = {}

  with open(FILE_NAME, mode='r', encoding='UTF-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
      date = row['Start Date']
      name = f"{row['Name']} {row['Surname']}"

      if date not in data_by_date:
        data_by_date[date] = []
      data_by_date[date].append(name)

  return data_by_date


def list_newer(start_date, data_by_date):
    """Loops through dates and pulls from the dictionary (Instant!)"""
    while start_date < datetime.datetime.today():
        date_str = start_date.strftime('%Y-%m-%d')
        
        # Look up the date in our pre-loaded dictionary
        if date_str in data_by_date:
            employees = data_by_date[date_str]
            print(f"Started on {start_date.strftime('%b %d, %Y')}: {employees}")
        
        # Move to the next day
        start_date = start_date + datetime.timedelta(days=1)
def main():
  start_date = get_start_date()
  #get_same_or_newer(start_date)
  worker_data = get_file_data()

  list_newer(start_date, worker_data)
  


if __name__ == "__main__":
  main()
