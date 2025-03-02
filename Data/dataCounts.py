import re
from datetime import datetime

# # Initialize variables
# transactions_per_minute = {}
# highest_hour = ""
# max_transactions = 0

# with open('serviceflow.log.2023-07-15-18.1', 'r') as file:
#     for line in file:
#         if "flow.api-settle-adsl-oa" in line and "success" in line:
           
#             timestamp_str = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}', line).group(0)
#             timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")
            
    
#             minute = timestamp.strftime("%Y-%m-%d %H:%M")  
#             hour = timestamp.strftime("%Y-%m-%dT%H")  
            
#             if minute in transactions_per_minute:
#                 transactions_per_minute[minute] += 1
#             else:
#                 transactions_per_minute[minute] = 1
            
#             if hour in transactions_per_minute:
#                 if transactions_per_minute[hour] > max_transactions:
#                     max_transactions = transactions_per_minute[hour]
#                     highest_hour = hour
#             else:
#                 transactions_per_minute[hour] = 1


# for minute, count in transactions_per_minute.items():
#     print(f"Minute: {minute}, Successful Transactions: {count}")


# print(f"Highest Hour with Successful Transactions: {highest_hour}")


def is_within_hour(timestamp_str, target_hour):
    timestamp_str = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}', line).group(0)
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")
    
    return timestamp.hour == target_hour

target_hour = 12

transactions_within_hour = []
with open('serviceflow.log.2023-07-15-18.1', 'r') as file:
    for line in file:
        if "flow.api-settle-adsl-oa" in line and "success" in line:
          
            timestamp_str = line.split()[0]
            
            if is_within_hour(timestamp_str, target_hour):
                transactions_within_hour.append(line)

for transaction in transactions_within_hour:
    print(transaction)




 
