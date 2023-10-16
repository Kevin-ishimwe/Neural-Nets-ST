import requests
import csv
import os
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stocks=["AAPL",   # Apple Inc.
  "MSFT",   # Microsoft Corporation
  "GOOGL",  # Alphabet Inc. (Google)
  "AMZN",   # Amazon.com Inc.
  "IBM",   #IBM Corporation
  "FB",     # Meta Platforms, Inc. (formerly Facebook, Inc.)
  "JPM",    # JPMorgan Chase & Co.
  "WMT",    # Walmart Inc.
  "BRK.B",  # Berkshire Hathaway Inc.
  "V",      # Visa Inc.
  "PG",     # Procter & Gamble Co.
  "UNH",    # UnitedHealth Group Incorporated
  "HD",     # The Home Depot, Inc.
  "DIS",    # The Walt Disney Company
  "NVDA",   # NVIDIA Corporation
  "TSLA",
   
    ]

path='./datasets'

if not os.path.exists:
    os.mkdir(path)
    print("datasets folder created")
for stock in stocks:
    
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+stock+"&outputsize=full&datatype=csv&apikey=B1V4C7CROIXPM8OM"
    print(url)
    try:
        r = requests.get(url)
        response = r
    except :
        print("fetch failed")

    if response.status_code == 200:
        data = response.text
        path_dt="./datasets/"+stock
        path=path_dt
        try:
         os.mkdir(path_dt)
        except:
         print("folder exists")
        output_file = "./datasets/"+stock+"/daily_stock_data.csv"
        with open(output_file, 'w',newline='') as csvfile:
            csvfile.write(data)







