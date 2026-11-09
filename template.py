"""
RECORD CHECK  -  my version
===========================

Name  :  Ntihemuka Migambi Darren
Lane  :  AI 
Date  :  06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def parse_line(raw_line):
    """Clean and parse a messy server record into a dictionary."""
    hostname_part, rest = raw_line.split(",", 1)

    hostname = hostname_part.strip().lower()
    record = {}

    for item in rest.split(","):
        key, value = item.split("=")
        record[key.strip().lower()] = float(value.strip())

    record["hostname"] = hostname
    record["percentage"] = (record["used"] / record["total"]) * 100

    return record


def status_of(record):
    """Determine the server usage status from its percentage."""
    if record["percentage"] >= 100:
        return "OVER LIMIT"
    elif record["percentage"] >= 90:
        return "WARNING"
    else:
        return "OK"





raw_records = ["  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=95,TOTAL=100",
    "  srv-03, Used = 45 , TOTAL = 80 ",
    "Srv-04 , USED=120 , total=100",
    "  SRV-05, used = 90, total = 100  ",
    "srv-06, USED=65, TOTAL=100"]   
    




flagged = 0

for raw_record in raw_records:
    parsed = parse_line(raw_record)
    status = status_of(parsed)

    print(parsed)
    print("Status:", status)
    print("=" * 40)

    if status != "OK":
        flagged += 1

print(f"Total records: {len(raw_records)}")
print(f"Flagged records: {flagged}")
