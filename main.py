import sqlite3
import time

from scheduler import Scheduler
import datetime as dt

from get_api_data import get_api_data


def main():

    # Take results from get_api_data function
    results = get_api_data()

    if not results.empty:

        # Create a database connection and cursor
        connection = sqlite3.connect('santiment_db')
        cursor = connection.cursor()

        # Insert API data to the database
        results.to_sql('api_data', connection, if_exists='replace')

        # Check results
        current_data_in_database = cursor.execute('''SELECT * FROM api_data''').fetchall()
        for row in current_data_in_database:
            print(row)

    else:
        raise ValueError('Did not get any response from the API.')


if __name__ == '__main__':

    schedule = Scheduler()
    schedule.hourly(dt.time(minute=30), main, alias='GET API DATA')

    while True:
        schedule.exec_jobs()
        time.sleep(1)

        # If you want to see the timeleft dynamically until the next execution of the script, uncomment below:
        # print(schedule)
