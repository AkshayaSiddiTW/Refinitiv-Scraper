'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

company_names = ['Walmart Inc', 'Amazon.com Inc', 'Apple Inc', 'CVS Health Corp', 'UnitedHealth Group Inc', 'Exxon Mobil Corp', 'Berkshire Hathaway Inc', 'Alphabet Inc', 'McKesson Corp', 'AmerisourceBergen Corp', 'Costco Wholesale Corp', 'Cigna Corp', 'AT&T Inc', 'Microsoft Corp', 'Cardinal Health Inc', 'Chevron Corp', 'Home Depot Inc', 'Walgreens Boots Alliance Inc', 'Marathon Petroleum Corp', 'Kroger Co', 'Ford Motor Co', 'Verizon Communications Inc', 'JPMorgan Chase & Co', 'General Motors Co', 'Centene Corp', 'Meta Platforms Inc', 'Comcast Corp', 'Phillips 66', 'Valero Energy Corp', 'Dell Technologies Inc', 'Target Corp', 'United Parcel Service Inc', "Lowe's Companies Inc", 'Bank of America Corp', 'Johnson & Johnson', 'Archer-Daniels-Midland Co', 'FedEx Corp', 'Humana Inc', 'Wells Fargo & Co', 'Pfizer Inc', 'Citigroup Inc', 'PepsiCo Inc', 'Intel Corp', 'Procter & Gamble Co', 'General Electric Co', 'International Business Machines Corp', 'MetLife Inc', 'Prudential Financial Inc', 'Albertsons Companies Inc', 'Walt Disney Co', 'Goldman Sachs Group Inc', 'Raytheon Technologies Corp', 'HP Inc', 'Boeing Co', 'Morgan Stanley', 'HCA Healthcare Inc', 'AbbVie Inc', 'Dow Inc', 'Tesla Inc', 'Allstate Corp', 'American International Group', 'Best Buy', 'Charter Communications', 'Sysco', 'Merck', 'New York Life Insurance', 'Caterpillar', 'Cisco Systems', 'TJX', 'Publix Super Markets', 'ConocoPhillips', 'Liberty Mutual Insurance Group Inc', 'Progressive Corp', 'Tyson Foods Inc','Bristol-Myers Squibb Co', 'Nike Inc', 'Deere & Co', 'American Express Co',  'StoneX Group Inc', 'Plains GP Holdings LP', 'Enterprise Products Partners LP', 'Oracle Corp', 'Thermo Fisher Scientific Inc', 'Coca-Cola Co', 'General Dynamics Corp', 'Northwestern Corp', 'Nucor Corp', 'Exelon Corp', 'Northrop Grumman Corp', '3M Co', 'Travelers Companies Inc', 'Arrow Electronics Inc', 'Honeywell International Inc', 'Dollar General Corp', 'Qualcomm Inc', 'Capital One Financial Corp', 'Philip Morris International Inc', 'Performance Food Group Co', 'Delta Air Lines Inc', 'American Airlines Group Inc', 'Netflix Inc', 'Paramount Global', 'US Foods Holding Corp', 'Danaher Corp', 'Jabil Inc', 'Starbucks Corp', 'Mondelez International Inc', 'Eli Lilly and Co', 'Hewlett Packard Enterprise Co', 'D.R. Horton Inc', 'Molina Healthcare Inc', 'CBRE Group Inc', 'Micron Technology Inc', 'Broadcom Inc', 'Gilead Sciences Inc', 'PBF Energy Inc', 'NRG Energy Inc', 'NVIDIA Corp', 'Occidental Petroleum Corp', 'Salesforce.Com Inc', 'Dollar Tree Inc', 'KKR & Co Inc', 'Kraft Heinz Co', 'Amgen Inc', 'AutoNation Inc', 'Penske Automotive Group Inc', 'PayPal Holdings Inc', "Macy's Inc", 'Duke Energy Corp', 'United Airlines Holdings Inc', 'Visa Inc', 'Rite Aid Corp', 'Cummins Inc', 'Paccar Inc', "McDonald's Corp", 'Southern Co', 'Truist Financial Corp', 'Applied Materials Inc', 'Freeport-McMoRan Inc', 'Lithia Motors Inc', 'Blackstone Group Inc', 'Hartford Financial Services Group Inc', 'Aflac Inc', 'Whirlpool Corp', 'Union Pacific Corp', 'International Paper Co', 'Altria Group Inc', 'CDW Corp', 'ManpowerGroup Inc', 'PG&E Corp', 'Carrier Global Corp', 'Baker Hughes Co', 'Cleveland-Cliffs Inc', 'United States Steel Corp', 'Becton Dickinson and Co', 'CarMax Inc', 'Sherwin-Williams Co', 'Builders FirstSource Inc', 'Marsh & McLennan Inc', 'PNC Financial Services Group Inc', 'Avnet Inc', 'Tenet Healthcare Corp', 'Kimberly-Clark', "Kohl's Corp", 'BlackRock Inc', 'Jones Lang LaSalle Inc', 'Lear', 'Lincoln National Corp','Charles Schwab Corp', 'Ross Stores Inc', 'Mastercard Inc', 'Genuine Parts Co', 'WestRock Co', 'EOG Resources Inc', 'Cognizant Technology Solutions Corp', 'Moderna Inc', 'Steel Dynamics Inc', 'HF Sinclair Corp', 'Texas Instruments Inc', 'Emerson Electric Co', 'WESCO International Inc', 'General Mills Inc', 'Waste Management Inc', 'Viatris Inc', 'DISH Network Corp', 'L3Harris Technologies Inc', 'DXC Technology Co', 'Goodyear Tire & Rubber Co', 'Uber Technologies Inc', 'Colgate-Palmolive Co', 'Stanley Black & Decker Inc', 'Stryker Corp', 'NextEra Energy Inc', 'Targa Resources Corp', 'Western Digital Corp', 'PPG Industries Inc', 'American Electric Power Company Inc', 'Gap Inc', 'Reinsurance Group of America Inc', 'Kinder Morgan Inc', 'ONEOK Inc', 'Expeditors International of Washington Inc', 'Advanced Micro Devices Inc', 'Fiserv Inc', 'Estée Lauder Companies Inc', 'Bank of New York Mellon Corp', 'Laboratory Corporation of America Holdings', 'Regeneron Pharmaceuticals Inc', 'Cheniere Energy Inc', 'Southwest Airlines Co', 'Adobe Inc', 'Synchrony Financial', 'Corteva Inc', 'Fidelity National Financial Inc', 'DTE Energy Co', 'Murphy Usa Inc', 'Halliburton Co', 'Automatic Data Processing Inc', 'Edison International', 'BorgWarner Inc',  'Nordstrom Inc', 'Loews Corp', 'Pioneer Natural Resources Co', 'AutoZone Inc', 'Lam Research Corp', 'Illinois Tool Works Inc', 'Parker-Hannifin Corp', 'Otis Worldwide Corp', 'Omnicom Group Inc', 'Principal Financial Inc', 'Dominion Energy Inc', 'Kellogg Co', 'Fluor Corp', 'AECOM', 'Reliance Steel & Aluminum CO', 'Jacobs Engineering Group Inc', 'Corning Inc', 'Qurate Retail Inc', 'Pultegroup Inc', 'Fidelity National Information Services Inc', 'IQVIA Holdings Inc', 'Marriott International Inc', 'Berry Global Group Inc', 'Ball Corp', 'Group 1 Automotive Inc', 'Leidos Holdings Inc', 'Wayfair Inc', 'Consolidated Edison Inc', 'Xcel Energy Inc', "O'Reilly Automotive Inc", 'Global Partners LP', 'Discover Financial Services', 'Rocket Companies Inc','LKQ Corp', 'Quanta Services Inc', 'Crown Holdings Inc', 'Fox Corp', 'Sempra Energy', 'Markel', 'Carvana', 'XPO Logistics Inc', 'Baxter International Inc', 'Ecolab Inc', 'Tractor Supply Co', 'Andersons Inc', 'Keurig Dr Pepper Inc', 'Universal Health Services Inc', 'CSX Corp', 'Henry Schein Inc', 'Sonic Automotive Inc', 'eBay Inc', 'Textron Inc', 'Community Health Systems Inc', 'Mosaic Co', 'Thor Industries Inc', "Dick's Sporting Goods Inc", 'Newmont Corporation', 'Devon Energy Corp', 'Warner Bros Discovery Inc', 'Alcoa Corp', 'Aramark', 'Vistra Corp', 'State Street Corp', 'Unum Group', 'Boston Scientific Corp', 'Westlake Chemical Corp', 'Entergy Corp', 'International Flavors & Fragrances Inc', 'DaVita Inc', 'Assurant Inc', 'Liberty Media Corp', 'Republic Services Inc', 'Mohawk Industries Inc', 'Conagra Brands Inc', 'Norfolk Southern Corp', 'AES Corp', 'AGCO Corp', 'Equitable Holdings Inc', 'Advance Auto Parts Inc', 'Biogen Inc', 'Booking Holdings Inc', 'Amphenol Corp', 'Quest Diagnostics Inc', 'FirstEnergy Corp', 'Ally Financial Inc', 'Delek US Holdings Inc', 'Williams Companies Inc', 'Newell Brands Inc', 'Eastman Chemical Co', 'Air Products & Chemicals Inc', 'Molson Coors Beverage Co', 'Interpublic Group of Companies Inc', 'Weyerhaeuser Co', 'Altice USA Inc', 'Raymond James Financial Inc', 'EMCOR Group Inc', 'Eversource Energy', 'Yum China Holdings Inc', 'Asbury Automotive Group Inc', 'Owens & Minor Inc', 'Public Service Enterprise Group Inc', 'United Rentals Inc', 'MGM Resorts International', 'Ryder System Inc', 'Intuit Inc', 'Cincinnati Financial Corp', 'Huntington Ingalls Industries Inc', 'W.R. Berkley Corp', 'Insight Enterprises Inc', 'News Corp', 'American Tower Corp', 'Old Republic International Corp', 'Burlington Stores Inc', 'Avis Budget Group Inc', 'ODP Corp', 'VF Corp', 'Bed Bath & Beyond Inc', 'Seaboard Corp', 'First American Financial Corp', 'PVH Corp', 'Apollo Global Management Inc', 'Jefferies Financial Group Inc', 'Hershey Co', 'NVR Inc', 'Foot Locker Inc', 'Dana Inc', 'SpartanNash Co', 'Olin', 'Chewy Corp', 'Jackson Financial Inc', 'Activision Blizzard Inc', 'Toll Brothers', 'Carlyle Group', 'Ovintiv Inc', 'UFP Industries Inc', 'Ulta Beauty Inc', 'Constellation Brands Inc', 'Expedia Group Inc', 'CommScope Holding Company Inc', 'Celanese Corp', 'Global Payments Inc', 'Owens Corning', 'Campbell Soup Co', 'Huntsman Corp', 'Franklin Resources Inc', 'Avery Dennison Corp', 'Masco Corp', 'CenterPoint Energy Inc', 'Fifth Third Bancorp', 'WEC Energy Group Inc', 'S&P Global INc', 'FM Global Logistics Holdings Bhd', 'Polaris Inc', 'Williams-Sonoma Inc', 'Autoliv Inc', 'Arthur J Gallagher & Co', 'Motorola Solutions Inc', 'Zillow Group Inc', 'Opendoor Technologies Inc', 'Oshkosh Corp', 'MasTec Inc', 'GXO Logistics Inc', 'APA Group ', 'Boise Cascade Co', 'Dover Corp', 'Genworth Financial Inc', 'Bath & Body Works Inc', 'Booz Allen Hamilton Holding Corp', 'Zimmer Biomet Holdings Inc', 'Westinghouse Air Brake Technologies Corp', 'Zoetis Inc', 'Packaging Corp of America', 'LPL Financial Holdings Inc', 'Fortune Brands Innovations Inc', "Caseys General Stores Inc", 'A-Mark Precious Metals Inc', 'Hess Corp', 'Vertex Pharmaceuticals Inc', 'KeyCorp', 'Chipotle Mexican Grill Inc', 'CMS Energy Corp', 'Arconic Corp (PITTSBURGH)', 'Taylor Morrison Home Corp', 'American Financial Group Inc', 'UGI Corp', 'Science Applications International Corp', 'Avantor Inc', 'Hanesbrands Inc', 'Clorox CO', 'KBR Inc', 'Hertz Global Holdings Inc', 'Analog Devices Inc', 'Darden Restaurants Inc', 'NCR Corp', 'Graphic Packaging Holding Co', 'Brighthouse Financial Inc', 'PPL Corp', 'Cintas Corp', 'Xerox Holdings Corp', 'Rockwell Automation Inc', 'Citizens Financial Group Inc', 'KLA Corp', 'Camping World Holdings Inc', 'Ingredion Inc', 'Veritiv Corp', 'Beacon Roofing Supply Inc', 'Diamondback Energy Inc', "Victoria's Secret & Co", 'Academy Sports and Outdoors Inc', 'Sanmina Corp', 'ON Semiconductor Corp', 'Commercial Metals Co', 'EnLink Midstream LLC', 'Southwestern Energy Co', 'Equinix Inc', "Dillard's Inc", 'Regions Financial Corp', 'Yum! Brands Inc', 'Landstar System Inc', 'CF Industries Holdings Inc', 'Northern Trust Corp', 'Robert Half International Inc', 'Compass Inc', 'Hasbro Inc', 'Roper Technologies Inc', 'Arko Corp.', 'Frontier Communications Parent Inc', 'Ameren Corp','American International Group Inc','Best Buy Co Inc','Charter Communications Inc','Sysco Corp','Merck & Co Inc','Caterpillar Inc','Cisco Systems Inc','TJX Companies Inc','Marsh & McLennan Companies Inc','Kimberly-Clark Corp','Kohls Corp','Lear Corp','Estee Lauder Companies Inc','Principal Financial Group Inc','Markel Corp','Carvana Co','Air Products & Chemicals Inc','W. R. Berkley Corp','Olin Corp','Chewy Inc', 'Toll Brothers Inc', 'Carlyle Group Inc', 'APA Group']






driver=webdriver.Chrome()

url = "https://www.refinitiv.com/en/sustainable-finance/esg-scores"  # Replace with the actual URL

esg_data = []

for company in company_names:
            driver=webdriver.Chrome()
            driver.get(url)
            time.sleep(5)

            try:
                    # Locate the search bar and enter the company name
                    search_bar = driver.find_element(By.XPATH, '//*[@id="searchInput-1"]')
                    search_bar.send_keys(company)  # Replace with the company name you want to search for

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


                    esg_data.append([company, esg_score.text, env.text, em.text, res.text, inn.text, soc.text, hum.text, prod.text, work.text, comm.text, gov.text, man.text, shar.text, csr.text])

            except Exception as e:
                print("An error occurred:", str(e))
                    
            finally:
                driver.quit()

        
    

csv_file_path = 'esg_scores1.csv'
df = pd.DataFrame(esg_data, columns=['Company', 'ESG Score' , 'E', 'Emissions', 'Resource Use', 'Innovation', 'S', 'Human Rights', 'Product Responsibility', 'Workforce', 'Community', 'G', 'Management', 'Shareholders', 'CSR Strategy'])
df.to_csv(csv_file_path, index=False)




#to add tickers
import requests 
import pandas as pd

def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    try:
        company_code = data['quotes'][0]['symbol']
    except:
        print(company_name)   
        return None
    
    return company_code

csv_file_path = 'esg_scores_600.csv'
df = pd.read_csv(csv_file_path)

tickers = {}

for x in company_names:
    tickers[x] = getTicker(x)

ticker_symbols = []
for name, symbol in tickers.items():

  '''

import pandas as pd

# Read the CSV files
df1 = pd.read_csv('9800.csv')
df2 = pd.read_csv('Refinitiv_2000.csv')

# Create a dictionary to map tickers to sectors
ticker_to_sector = dict(zip(df1['Tickers'], df1['Sector']))

# Add a new "sector" column to the second dataframe based on matching tickers
df2['Sector'] = df2['Tickers'].map(ticker_to_sector)

# Save the updated dataframe back to a new CSV file
df2.to_csv('updated_ref.csv', index=False)

