from MSearch import MSearch

def main(db_file):
    array = []
    with open(f"{db_file}.txt", "r", encoding="utf-8") as r:
        for line in r:
            array.append(line)
    MSearch(array)
            
    
