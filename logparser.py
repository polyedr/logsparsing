# Parse the log files to the years or months
import re
from datetime import datetime, date


class Logparser:
    """
    Name of the file and the time pgiteriod should be defined
    when you will create the class object,
    such as parser = Logparser("your_log_file_name", "months")
    where the time period values available are 'months' and 'years'
    """

    period = "months"

    def __init__(self, logfilename, period):
        self.logfilename = logfilename
        self.period = period

    def logparser(self):
        # Define the pattern to search with regular expression
        rpatt = re.compile("[^\t\n]+")

        with open(self.logfilename) as r:
            for line in r:
                row = rpatt.findall(line)
                # First element in row is a datetime or a date
                # Obtain the date from the datetime
                date_from_line = row[0].split()[0]
                try:
                    dtime = datetime.strptime(date_from_line, "%d.%m.%Y")
                except ValueError:
                    # For the empty date write to the year 2300
                    print("There are no valid date for some row")
                    dtime = date(day=1, year=2300, month=1)

                year = dtime.year
                month = dtime.month

                # Write the line to the file for an appropriate year or months
                if self.period == "years":
                    with open(str(year) + ".log", "a+") as f:
                        f.write(line)
                elif self.period == "months":
                    with open(str(month) + ".log", "a+") as f:
                        f.write(line)


if __name__ == "__main__":
    parser = Logparser("dispatch_2015_16_17.csv", "months")
    parser.logparser()
