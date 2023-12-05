

from datetime import datetime, timedelta

# Define time zone offsets
pdx_offset = -8  # Pacific Time Zone UTC-8
nyc_offset = -5  # Eastern Time Zone UTC-5
lndn_offset = 0  # London Time Zone UTC+0

branch_hours = {
    'Portland': {'open': 9, 'close': 17},
    'NYC': {'open': 9, 'close': 17},
    'London': {'open': 9, 'close': 17}
}

# Find out time for each branch

current_time = datetime.utcnow()  # The UTC time

pdx_time = current_time + timedelta(hours=pdx_offset)  # Portland
nyc_time = current_time + timedelta(hours=nyc_offset)  # New York
lndn_time = current_time + timedelta(hours=lndn_offset)  # London

# Function to see if branch is open or closed
def open_close(branch, current_time):
    open_time = datetime(
        current_time.year,
        current_time.month,
        current_time.day,
        branch['open']
    )
    close_time = datetime(
        current_time.year,
        current_time.month,
        current_time.day,
        branch['close']
    )

    return open_time <= current_time <= close_time

# Checking open/closed status of each branch and printing it

for branch, hours in branch_hours.items():
    if open_close(hours, pdx_time):  # Portland O/C status
        status = "Open"
    else:
        status = "Closed"
    print(f"{branch} branch is {status}")

for branch, hours in branch_hours.items():
    if open_close(hours, nyc_time):  # New York O/C status
        status = "Open"
    else:
        status = "Closed"
   


