from double_check_jsons import check_json_is_inserted
from fetch_data import get_data
from process_json import bulk_process_json
from dump_json import dump_json
from database import create_main_table
import time

if __name__ == "__main__":
    path = "data/data.db"
    raw_json = get_data()
    id = dump_json(raw_json)
    create_main_table(path)
    t0 = time.time()
    dump_json(get_data())
    
    target=check_json_is_inserted(path)
  

    #bulk_process_json(raw_json,id)
    t1 = time.time()

    print(t1-t0)    

