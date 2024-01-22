from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import json

options = webdriver.ChromeOptions()
# options.add_argument('window-size=1800,1000')#change window-size(chrome)\
browser = webdriver.Chrome(executable_path='../main/chromedriver', options=options)

browser.get('http://localhost:3000')

# Find the slider element (replace with the appropriate selector)
def extract_outer_img():
  image = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/img[1]')
  url = image.get_attribute('src')
  return url

def solve_captcha():
    # slider = browser.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/span/span[3]')
    # res = 123.1949/0.658188
    # print(res)
    # actions = ActionChains(browser)
    # actions.click_and_hold(slider).move_by_offset(res, 0).perform()

    with open('rotation_data.json', 'r') as file:
        json_data = json.load(file)

    outer_img_url = extract_outer_img()

    matched = False
    for entry in json_data:
        if outer_img_url == entry["url1"]:
            matched = True
            # If a match is found, calculate the movement required and move the slider
            slider = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/span/span[3]')
            deg = float(entry["deg"])
            res = deg / 0.658188
            print("deg is :", deg)
            print("res is :", res)
            print(res/10)
            actions = ActionChains(browser)
            actions.click_and_hold(slider).move_by_offset(res, 0).release().perform()#36.5353
            time.sleep(2)
            actions.click_and_hold(slider).move_by_offset(1, 0).perform()
            time.sleep(2)
            actions.click_and_hold(slider).move_by_offset(-1, 0).release().perform()
            

            break
    
    if not matched:
        print('refresh')

# Close the browser when done
solve_captcha()
time.sleep(60)
browser.quit()
