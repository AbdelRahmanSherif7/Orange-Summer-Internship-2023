import matplotlib.pyplot as plt
import re
from datetime import datetime

transactions_per_minute = {}
highest_hour = ""
max_transactions = 0

x_values = []  
y_values = []  

with open('serviceflow.log.2023-07-15-18.1', 'r') as file:
    for line in file:
        if "flow.api-settle-adsl-oa" in line and "success" in line:
           
            timestamp_str = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}', line).group(0)
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")
            
            minute = timestamp.strftime("%Y-%m-%d %H:%M")  
            hour = timestamp.strftime("%Y-%m-%dT%H")  
            
            if minute in transactions_per_minute:
                transactions_per_minute[minute] += 1
            else:
                transactions_per_minute[minute] = 1
            
            if transactions_per_minute[minute] > max_transactions:
                max_transactions = transactions_per_minute[minute]
                highest_hour = hour
            x_values.append(minute)  
            y_values.append(transactions_per_minute[minute])  


for minute, count in transactions_per_minute.items():
    print(f"Minute: {minute}, Successful Transactions: {count}")

print(f"Highest Hour with Successful Transactions: {highest_hour}")


plt.plot(x_values, y_values)
plt.xlabel('Minutes')
plt.ylabel('Successful Transactions')
plt.title('Successful Transactions Per Minute')
plt.xticks(rotation=45)  
plt.show()
