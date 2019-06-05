import csv
import re
import sys


def ping_pong_times(arr):
    result = 0
    for i in set(arr):
        result += arr.count(i)-1
    return result


def transfer_times(arr):
    return len(arr)


def get_transfer_path(revision_history):
    return re.findall(r'(?<=The group in charge changed from).*?(?=. Reason for Transfer)', revision_history)


string = "2018-07-19 14:19 Wojcik, Jacek (Nokia - PL/Wroclaw) The group in charge changed from NIPSSHC5G to NIULSLFS. Reason for Transfer\
2018-07-19 08:53 Chen, Chuchu-Nora (NSB - CN/Hangzhou) The group in charge changed from NIHZSFHSID to NIPSSHC5G. Reason for Transfer\
2018-07-18 17:10 Diallo, Souleymane (Nokia - FR/Paris-Saclay) The group in charge changed from NIPSSHC5G to NIHZSFHSID. Reason for Transfer"

if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit()
    file_path = sys.argv[1]
    try:
        records = csv.reader(open(file_path, 'r', encoding='UTF-8'))
    except FileNotFoundError as e:
        print(file_path+" is not be founded")
        exit()
    for record in records:
        print(get_transfer_path(record[15]))




