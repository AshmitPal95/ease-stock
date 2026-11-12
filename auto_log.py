import datetime
import csv
import db.history_repo
import db.date_repo
from pathlib import Path 

def main():
    def log():
        log_dir = Path.home() / "ease-stock"/"logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        rows=db.history_repo.fetch_history_date(start_date,end_date)
        with open(log_dir/f"{start_date}_to_{end_date}.csv",'w',newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["HISTORY ID","INVOICE NUMBER","CATEGORY NAME","GRADE","GARDEN NAME","VENDOR NAME","GODOWN NAME","NUM OF UNITS","UNIT WT","RATE","OPERATION TYPE","TRANSACTION DATE"])
            writer.writerows(rows)

    start_date=db.date_repo.fetch_start_date()
    end_date=db.date_repo.fetch_end_date()
    today=datetime.date.today()
    if start_date is None:
        start_date=today
        end_date=start_date+datetime.timedelta(days=13)
    if today>end_date:
        while today>end_date: 
            log()
            start_date=end_date+datetime.timedelta(days=1)
            end_date=start_date+datetime.timedelta(days=13)
    db.date_repo.change_start_date(start_date)
    db.date_repo.change_end_date(end_date)
            

