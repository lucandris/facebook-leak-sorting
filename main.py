from unidecode import unidecode
import pandas as pd
from tqdm import tqdm

def first(country):
    with open(f"vanilla\{country}.txt", 'r', encoding='utf-8') as file:
        entries = file.readlines()

    data = []
    with tqdm(total=len(entries), desc=f"Processing {country} entries") as pbar:
        for entry in entries:
            fields = entry.strip().split(':')
            fields = [field.lower() for field in fields]

            entry_dict = {}
            for i, field in enumerate(['PHONE','FACEBOOK','FIRST','LAST','GENDER','RESIDENCE','BIRTHPLACE','RELATIONSHIP','WORKPLACE','JOINED','EMAIL','BIRTHDATE']):
                field_value = fields[i] if i < len(fields) else None
                entry_dict[field] = unidecode(field_value) if field_value else None
            data.append(entry_dict)
            pbar.update(1)

    df = pd.DataFrame(data)
    df.to_csv(f"data\{country}.csv", index=False)

first("ireland")


    
