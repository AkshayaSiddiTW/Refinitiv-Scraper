import requests 
import pandas as pd

#function to get tickers based on company name
def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    
    try:
        data = res.json()
        company_code = data['quotes'][0]['symbol']
    except:
        print(company_name)   
        return None
    
    return company_code

#path to csv file with company names
csv_file_path = 'esg_scores_600.csv'
df = pd.read_csv(csv_file_path)

tickers = []

for name in df['Company']:
    tickers.append(getTicker(name))
    
#creates a new column called Tickers
df['Tickers'] = tickers

#save it to a new csv file
df.to_csv('500.csv', index=False)

'''
import pandas as pd

# Load the first CSV file
csv_file_path1 = '2021.csv'
df1 = pd.read_csv(csv_file_path1)

# Load the second CSV file
csv_file_path2 = 'cleaned.csv'
df2 = pd.read_csv(csv_file_path2)

# Merge the two DataFrames based on the 'Tickers' column
merged_df = df1.merge(df2, on='Tickers', how='inner')
merged_df = merged_df.drop_duplicates(subset=['Tickers'])

# Save the merged DataFrame to a new CSV file
merged_csv_path = '2021_Companies.csv'
merged_df.to_csv(merged_csv_path, index=False)

print("Merged CSV file created successfully.")
'''
