from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import json

#options
test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
# options.add_argument('--mute-audio')#dis audio
options.add_argument('--no-sandbox')
options.add_argument('window-size=2200,1000')
options.add_argument(f'--user-agent={test_ua}')

#credential
login = 'akawnate1@gmail.com'
password = '@Test2222'

#global variable
browser = webdriver.Chrome(options=options)

def auth():
  global browser, login, password
  loginUrl = 'https://www.tiktok.com/login/phone-or-email/email'

  browser.get(loginUrl)
  sleep(1)
  browser.find_element(By.NAME,'username').send_keys(login)
  # sleep(1)
  browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/form/div[2]/div/input').send_keys(password)
  # sleep(1)
  browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/form/button').click()
  sleep(10)
  captcha = len(browser.find_elements(By.XPATH, '//*[@id="captcha_container"]')) != 0
  print(captcha)

  
  
def extract_outer_img():
  image = browser.find_element(By.XPATH, '//*[@id="captcha_container"]/div/div[2]/img[1]')
  url = image.get_attribute('src')
  return url

def solve_captcha():
  while True:
    with open('../captchaUrl/rotation_data.json', 'r') as file:
      json_data = json.load(file)

    outer_img_url = extract_outer_img()

    matched = False
    for entry in json_data:
      # print("outer img url:", outer_img_url)
      original_url1 = entry["url1"] 
      url1_p19 = original_url1.replace("p16-", "p19-")
      url1_p16 = original_url1.replace("p19-", "p16-")
      if outer_img_url == url1_p19 or outer_img_url == url1_p16:
        matched = True
        print(url1_p19)
        print(url1_p16)
        slider = browser.find_element(By.XPATH, '//*[@id="secsdk-captcha-drag-wrapper"]/div[2]')
        deg = float(entry["deg"])
        res = deg / 0.658188
        actions = ActionChains(browser)

        actions.click_and_hold(slider).move_by_offset(res, 0).perform()#36.5353
        sleep(2)
        actions.click_and_hold(slider).move_by_offset(1, 0).perform()
        sleep(2)
        actions.click_and_hold(slider).move_by_offset(-1, 0).release().perform()
        break
    if matched:
      break
    if not matched:
      print('Refreshing captcha...')
      browser.find_element(By.XPATH, '//*[@id="captcha_container"]/div/div[4]/div/a[1]').click()#refresh button
      sleep(3)




auth()
solve_captcha()
sleep(50)
browser.quit()

