from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import csv

def start_browser():
    browser = webdriver.Chrome(options=Options(),
                               executable_path=r'chromedriver.exe')
    return browser

def save(items, path):
    items_ = []
    for i in range(len(items[0])):
        items_.append({'name':items[0][i],
                     'urls':items[1][i],
                     'description':items[2][i]})
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['name', 'urls', 'description'])
        for item in items_:
            writer.writerow([item['name'], item['urls'], item['description']])

def read_checked_accounts(file_num):
    with open(f'techstars_{file_num}page.csv', newline = '') as file:
        reader = csv.DictReader(file, delimiter=';')
        checked_accounts = [[row['name'],row['urls'],row['description']] for row in reader]
    return checked_accounts

companys = []
for i in range(1, 72):
    companys += read_checked_accounts(i)

companys_ = []
for i in companys:
    if i not in companys_: companys_.append(i)
    else: continue

names = [i[0] for i in companys_]
urls = [i[1] for i in companys_]
descs = [i[2] for i in companys_]

save([names, urls, descs], '_techstars.csv')

# names, urlss, descs = [], [], []
# counter_k = 0
# browser = start_browser()
# for k in range(71, 72):
#     HOST = 'https://www.techstars.com/portfolio?currentPage='
#     browser.get(HOST+str(k))
#
#     counter_k+=1
#     counter_i = 0
#     for i in range(50):
#         counter_i += 1
#         cards = [j for j in browser.find_elements(By.CLASS_NAME, 'CompanyCard')]
#         cards[i].click()
#         time.sleep(1)
#
#         modal = browser.find_element(By.CLASS_NAME, 'CompanyModal')
#         soup = bs(modal.get_attribute('innerHTML'), 'html.parser')
#
#         name = soup.find('h3', class_='jss704 jss786 jss732 jss743').text.strip().encode('utf-8').decode('utf-8')
#         urls = ', '.join([i['href'] for i in soup.find_all('a', class_='jss791')]).strip().encode('utf-8').decode('utf-8')
#         desc = modal.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/div[2]/div/p').text.strip().encode('utf-8').decode('utf-8')
#         print(counter_k, counter_i, name, '\n', urls, '\n', desc)
#         names.append(name)
#         urlss.append(urls)
#         descs.append(desc)
#         save([names, urlss, descs], f'techstars_{k}page.csv')
#
#         modal.find_element_by_xpath('//div[@class="jss596 jss597 jss598 jss615 jss632"]/*[name()="svg"][@data-testid="Close"]').click()
#         time.sleep(1)
