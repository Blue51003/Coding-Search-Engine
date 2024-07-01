from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time


# Setup Selenium WebDriver for Microsoft Edge
edge_driver_path = 'msedgedriver.exe'  # Replace with your EdgeDriver path
options = Options()
#options.add_argument('--headless')  # Optional: run Edge in headless mode
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

# Navigate to the page
url = 'https://codeforces.com/problemset/page/'  # Replace with the URL of the page you want to visit

def get_a_tags(url):
    driver.get(url)
    time.sleep(7)
    links = driver.find_elements(By.TAG_NAME, "a")
    ans=[]
    pattern = "/problems"
    for i in links:
        try:
            if pattern in i.get_attribute("href"):
                ans.append(i.get_attribute("href"))
        except:
            pass
    ans = list(set(ans))
    return ans

final_ans = []

for i in range(1, 97):
    final_ans += (get_a_tags(url+str(i)))

final_ans = list(set(final_ans))

with open('cf.txt', 'a') as f:
    for j in final_ans:
        f.write(j+'\n')

print(len(final_ans))

driver.quit()