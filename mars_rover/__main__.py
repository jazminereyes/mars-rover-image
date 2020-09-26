import dateutil.parser as parser
from datetime import datetime
from mars_rover.rover import Rover


def main():
    date_list = get_dates()

    for date in date_list:
        # Parse dates with different formats
        formatted_date = None
        try:
            formatted_date = parser.parse(date)
        except Exception:
            print('%s is an invalid date.' % date)
        
        if formatted_date:
            # Call Rover class to retrieve photo, pass date as parameter
            rover = Rover(formatted_date)
            rover.retrieve_photo()


# Get dates from text file
def get_dates():
    f = open('dates.txt', 'r')
    contents = f.read().splitlines()
    return contents


if __name__ == "__main__":
    main()
