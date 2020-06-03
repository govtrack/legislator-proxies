# Test the validity of the file.

import csv
import datetime

for rec in csv.DictReader(open("Remote-Proxy - Sheet1.csv")):
  # Check that the IDs are integers.
  int(rec["Remote ID"])
  int(rec["Proxy ID"])

  # Check that the dates parse.
  datetime.datetime.strptime(rec["Date Assigned"], "%m/%d/%Y")
  if rec["Date Revoked"] != "":
    datetime.datetime.strptime(rec["Date Revoked"], "%m/%d/%Y")
