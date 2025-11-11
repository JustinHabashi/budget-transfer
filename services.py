import csv
import re
from pathlib import Path
from typing import Optional


FOLDER = Path("budgets")


def check_file_types(folder: Path) -> bool:
    for entry in folder.iterdir():
        if entry.is_file() and entry.suffix != ".csv":
            print(f"{entry.name} is not a .csv file")
            return False
    return True


def create_month_expenses_csv(
    month: int,
    overwrite: bool = True,
    encoding: str = "utf-8",
) -> Path:
    path = Path.cwd() / f"{month}-expenses.csv"
    if path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {path}")
    return path


def get_budgets(month: int, folder: Path = FOLDER) -> Optional[Path]:
    if not folder.exists() or not folder.is_dir():
        print("budgets folder is empty")
        return None

    n = sum(1 for item in folder.iterdir() if item.is_file())
    if n == 0:
        print("budgets folder is empty")
        return None

    if not check_file_types(folder):
        return None

    output_csv = create_month_expenses_csv(month)
    process_budgets(folder, month, output_csv)
    print("all done")
    return
    
    
def process_budgets(folder, month, path): 
     rows_to_add = []
     for budget in folder.iterdir():
        with open(budget, 'r', newline='') as file:
             reader = csv.reader(file)
             for row in reader:
                 if get_month(row[0]) == month and row[2]:
                     rows_to_add.append([row[1],row[2]])                      
     with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for new_row in rows_to_add:
            writer.writerow(new_row)                
                     		

def get_month(dateString):
    month = ''
    if '-' in dateString:
        month = re.split(r'[/-]',dateString)[1]
    elif '/' in dateString:
        month = re.split(r'[/-]',dateString)[0]
    return int(month)