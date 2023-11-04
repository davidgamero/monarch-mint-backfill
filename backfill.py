import csv
import sys
import datetime

def parse_date(date):
   d = datetime.datetime.strptime(date, '%B %Y')
   return d


def backfill_csv(path,account_name,max_date)-> list:
  with open(path, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      rows = []
      for row in reader:
        # Skip header
        if row[0] == 'DATES':
          rows.append(['Date','Amount','Account'])
          continue

        date = parse_date(row[0])
        month = date.month
        while date.month == month:
          date_str = date.strftime('%Y-%m-%d')
          if date_str ==  max_date:
            return rows
          rows.append([date_str, row[1][1:],account_name])
          date = date + datetime.timedelta(days=1)
  return rows

def write_csv(path, rows):
  filename = path.split('/')[-1]
  filewithoutext = filename.split('.')[0]
  with open(filewithoutext+'-backfilled.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    for row in rows:
      writer.writerow(row)
      

if __name__ == '__main__':
   if len(sys.argv) < 4:
     print('Usage: python backfill.py <csv_path> <account_name> <max-date YYYY-MM-DD>')
     sys.exit(1)
   csv_path = sys.argv[1]
   account_name = sys.argv[2]
   max_date = sys.argv[3]
   new_rows = backfill_csv(csv_path ,account_name,max_date)
   write_csv(csv_path, new_rows)
