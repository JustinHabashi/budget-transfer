import csv
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
    overwrite: bool = False,
    encoding: str = "utf-8",
) -> Path:
    path = Path.cwd() / f"{month}-expenses.csv"
    if path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {path}")
    with path.open("w", newline="", encoding=encoding) as f:
        csv.writer(f)
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

    create_month_expenses_csv(month)
    process_budgets(folder)
    print("all done")
    return
    
    
def process_budgets(folder):
     for budget in folder.iterdir():
        with open(budget, 'r', newline='') as file:
             reader = csv.reader(file)
             for row in reader:
                 # TODO: make a function to add the amounts and filter by date
    
             
        
			
		

def get_month(dateString):
    month = int(dateString.split("/")[0])
    return month