#!/usr/bin/env python3

import os, csv , requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_file():
    if not os.path.exists("tester.csv"):
        
        response = requests.get(FILE_URL)
        response.raise_for_status
        with open("tester.csv","w", newline="",encoding="utf-8") as f:
            writer=csv.writer(f)
            for line in response.iter_lines():
                writer.writerow(line.decode("utf-8").split(','))

    else:
        print("This exists")
        print("continuing")

def main():
    get_file()

if __name__ == "__main__":
    main()