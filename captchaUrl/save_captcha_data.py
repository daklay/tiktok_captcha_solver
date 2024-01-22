from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import json
from threading import Event

# Function to extract URLs from the page
def extract_image_urls(driver):
    images = driver.find_elements(By.TAG_NAME, 'img')
    urls = [img.get_attribute('src') for img in images]
    return urls[:2]  # Assuming the first two images are the ones you're interested in

# Initialize the driver
options = webdriver.ChromeOptions()
options.add_argument('window-size=1800,1000')#change window-size(chrome)\
driver = webdriver.Chrome(executable_path='../main/chromedriver', options=options)

driver.get('http://localhost:3000')  # Replace with the URL of your React app


# Initialize an empty list to store the data
data_list = []

# Event to stop the loop when Enter is pressed
stop_event = Event()

print("Press Enter to stop the script...")

# Function to wait for Enter and then set the event
def wait_for_enter():
    input()
    stop_event.set()

# Function to save data when an alert is shown
def save_on_alert():
    while not stop_event.is_set():
        try:
            Alert(driver).accept()  # Accept the alert (if present)
            # Find the <p> element with id "deg" and extract its text
            p_element = driver.find_element(By.ID, 'deg')
            degree = p_element.text.strip()

            # Extract image URLs
            image_urls = extract_image_urls(driver)

            # Append the data to the list
            data_list.append({
                "url1": image_urls[0],
                "url2": image_urls[1],
                "deg": degree
            })

            # Save the list to a JSON file
            with open('rotation_data.json', 'w') as json_file:
                json.dump(data_list, json_file, indent=4)

            print(f"Rotation degree {degree} and URLs saved to file.")
        except Exception as e:
            pass  # No alert present or other exceptions, continue checking

# Start the thread that waits for Enter key
from threading import Thread
enter_thread = Thread(target=wait_for_enter)
enter_thread.start()

# Start the thread that saves data when an alert is shown
alert_thread = Thread(target=save_on_alert)
alert_thread.start()

try:
    while not stop_event.is_set():
        time.sleep(0.5)  # Pause the loop to prevent too frequent checks
finally:
    # Clean up, close the browser
    driver.quit()
    enter_thread.join()  # Ensure the Enter key thread is also stopped
    alert_thread.join()  # Ensure the alert thread is also stopped
