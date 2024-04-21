import requests
import xml.etree.ElementTree as ET
import csv

# List of stocks within an index up to the year 2023
stocks_under_imoex_till_2023 = [
    "AFKS", "AFLT", "AGRO", "ALRS", "СВОМ", "CHMF", "ENPG", "FEES", "FIVE", "FLOT","GAZP", "GLTR", "GMKN", "HYDR", "IRAO", "LKOH", "MAGN", "MGNT", "MOEX", "MSNG","MTLR", "MTLRP", "MTSS", "NLMK", "NVTK", "OZON", "PHOR", "PIKK", "PLZL", "POLY",
    "POSI", "QIWI", "ROSN", "RTKM", "RUAL", "SBER", "SBERP", "SELG", "SGZH", "SMLT","SNGS", "SNGSP", "TATN", "TATNP", "TCSG", "TRNFP", "UPRO", "VKCO", "VTBR", "YNDX"
]

# Base URL of the MOEX API
base_url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/YNDX.xml'

# Define CSV file name
csv_file = 'trading_data.csv'

# Define parameters
params = {
    'from': '2023-01-03',  # Start date
    'till': '2023-12-29',   # End date
    'interval': '24',       # Interval (24 for daily)
}

# Open CSV file in write mode with newline='' to prevent extra newlines
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow([
        'BOARDID', 'TRADEDATE', 'SHORTNAME', 'SECID', 'NUMTRADES', 'VALUE', 'OPEN', 'LOW', 'HIGH','CLOSE', 'VOLUME'])
    
    # There were 254 trading days
    for start in range(0, 250, 100): 
        params['start'] = start
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            for row in root.findall('.//row'):
                writer.writerow([
                    row.get('BOARDID'), row.get('TRADEDATE'), row.get('SHORTNAME'), 
                    row.get('SECID'), row.get('NUMTRADES'), row.get('OPEN'), row.get('LOW'), row.get('HIGH'), row.get('CLOSE'), row.get('VALUE'), row.get('VOLUME')])

            print(f"Fetched entries from {start} to {min(start + 99, 250)}")
        else:
            print("Failed to fetch data from the URL")
            break

print("CSV file has been created successfully.")
