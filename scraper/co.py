'''import yfinance as yf
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Load the CSV file
csv_file_path = 'filtered_data.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Extract the first 600 values from the 'Tickers' column and convert them to a list of strings
tickers_list = df['Tickers'][1500:2501].tolist()

url = "https://www.refinitiv.com/en/sustainable-finance/esg-scores"  # Replace with the actual URL
esg_data = []

def get_company_names(tickers):
    try:
        stock_info = yf.Ticker(tickers)
        company_name = stock_info.info.get("longName", "N/A")
        return company_name
    except:
        print(f"Error fetching data for ", tickers)
        return None  
    


for x in tickers_list:
        
    y = get_company_names(x)
    
    if y is None:
          continue

    y = y.replace(",",'').replace(".","").replace("Company","Co").replace("Corporation","Corp").replace("Limited","Ltd")


    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    try:
            # Locate the search bar and enter the company name
            search_bar = driver.find_element(By.XPATH, '//*[@id="searchInput-1"]')
            search_bar.send_keys(y)  # Replace with the company name you want to search for

                        #search button

            ele = driver.find_element(By.XPATH, '//*[@id="esg-data-body"]/div[1]/div/div/div[1]/div/button[2]')
            driver.execute_script("arguments[0].click();", ele)
            time.sleep(5)

                        #ESG SCORE
            xpath_expression = '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/h3/strong'
            esg_score = driver.find_element(By.XPATH, xpath_expression)

                        #ENVIRONMENT DATA
            env = driver.find_element(By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]/b')
                        #emissions
            em = driver.find_element(By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/b')
                        #resource use
            res = driver.find_element(By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[3]/div[2]/b')
                        #innovation
            inn = driver.find_element(By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[4]/div[2]/b')

                        #SOCIAL DATA
            soc = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[5]/div[2]/b')
                        #human rights
            hum = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[6]/div[2]/b')
                        #product responsibility
            prod = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[7]/div[2]/b')
                        #workforce
            work = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[8]/div[2]/b')
                        #community
            comm = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[9]/div[2]/b')

                        #GOVERNANCE DATA
            gov = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[10]/div[2]/b')
                        #management
            man = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[11]/div[2]/b')
                        #shareholders
            shar = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[12]/div[2]/b')
                        #CSR strategy
            csr = driver.find_element(By.XPATH,'//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[13]/div[2]/b')


            esg_data.append([y, esg_score.text, env.text, em.text, res.text, inn.text, soc.text, hum.text, prod.text, work.text, comm.text, gov.text, man.text, shar.text, csr.text, x])

    except Exception as e:
            print("An error occurred:", y)
                        
    finally:
            driver.quit()

        
    

csv_file_path = 'esg_scores_600_2.csv'
df = pd.DataFrame(esg_data, columns=['Company', 'ESG Score' , 'E', 'Emissions', 'Resource Use', 'Innovation', 'S', 'Human Rights', 'Product Responsibility', 'Workforce', 'Community', 'G', 'Management', 'Shareholders', 'CSR Strategy','Tickers'])
df.to_csv(csv_file_path, index=False)

'''
import pandas as pd

file1 = pd.read_csv('Ref.csv')
file2 = pd.read_csv('cleaned.csv')

merged_df = pd.concat([file1, file2], ignore_index=True)
merged_df.drop_duplicates()


merged_df.to_csv('Refinitiv_2000.csv', index=False)


