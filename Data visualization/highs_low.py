import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = 'death_valley_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            date = current_date
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates.append(date)
            lows.append(low)
            highs.append(high)
    # for index, column_header in enumerate(header_row):
    #   print(index, column_header)
    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
