# Mint Monarch backfill

RIP to Mint, the best free finanncial tool.

## Purpose

When migrating my data from Mint to Monarch Money, I wanted to keep my account balance data to be able to still use the "Net Worth" feature, but apparently you need data for every day, but Mint only exports data on the "trends" view for a month.

Monarch Wants:
```csv
Date,Amount,Account Name
2023-01-28,500.00,Checking
2023-01-27,300.00,Checking
2023-01-26,300.00,Checking
```

Mint Gives:
```csv
"DATES","Assets"
"July 2023","$500.00"
"August 2023","$500.00"
"September 2023","$500.00"
```

So we gotta do some wranglin'

Since mint only give monthly data, i just copied it once per day for each month to get Monarch to import it

# Usage

To get a csv for a single account to backfill, go to Assets>Over Time on Mint.

Select just one account, and "All Time"

Then at the very bottom use "export csv"

Then download backfill.py and run `python backfill.py <csv_path> <account_name> <max-date YYYY-MM-DD>`

The max-date should be the date you linked your account to Monarch to avoid gaps.

Account Name doesn't really matter just pick one and it'll get imported fine

Then go follow Monarch's [Upload account balance history](https://help.monarchmoney.com/hc/en-us/articles/14882425704212) to get the data in.