import csv
import logging

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:%(message)s')
logger =logging.getLogger("Week_1_Assignment")

path ='data.csv'

try:
    with open(path, 'r', encoding='utf-8') as f:
        reader =csv.DictReader(f)
        for r in reader:
            print('Row : ',r)
except FileNotFoundError as e:
     logger.exception('file not found error')
except Exception as e:
    logger.exception('Unexcepted Error')
