import requests
from collections import defaultdict
import threading

# Your target URL
url = "https://www-useast1a.tiktok.com/captcha/get?lang=en&app_name=&h5_sdk_version=2.32.6&h5_sdk_use_type=cdn&sdk_version=3.8.9&iid=0&did=7326160832088393221&device_id=7326160832088393221&ch=web_text&aid=1459&os_type=3&mode=whirl&tmp=1705769793022&platform=h5&webdriver=false&fp=verify_lrm2ckuw_nCtU9Z4F_H9Qp_4NVB_9s7O_dVJFhYfjyQXn&type=verify&detail=jMLGb2roLVO2REV8E-1HPxL2L2o0b9lBX47fu1aKnsmaOE5Zau4aOacNUjt8hDORKR1N7nYz7CDK7FVtnXePulse-54vz8iItKzAcZ3Mcgwh9JJf97JoKldwo34oDUCtldygy7OG4nPO5z7WP1E8f3h1ktgHjp8DvSxlPqffHUv81u95ZKaRnw0dO9acTDcMLX5HfOdcdJR5T-*AnOKZcW77ocr6FoCxkFbD0a-dVs03RlNKFpF7HmQdUTl3LIiDwvT94ka2BP51PuVJg-b2QVpINqip1v-xKVqmdh283lq-IiRpTM9WIYE8HutySdCyc1RcuGS0vzqNjnD7RzZs5FEEBTcXO3gMfqNgwzD*nZXCIZMLAcwgDxX39G5CGfTbPNOidKMKSA7L5W6dyP*liIMQGstaVhqACh*bZxqpbUCE2nBAkZ1sESjDLQLWxetJVrFT4OrCs5C04rBiZchi2hPMfM8w1*dyjUrUEOICuf6i6igubg..&server_sdk_env=%7B%22idc%22:%22maliva%22,%22region%22:%22MALIVA%22,%22server_type%22:%22passport%22%7D&subtype=whirl&challenge_code=99996&os_name=windows&h5_check_version=3.8.9&region=va&triggered_region=va&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F114.0.0.0+Safari%2F537.36+Edg%2F114.0.1823.43&msToken=sx_sT6ze9SO5QzGuTLyhn_66I7PZEB_PxZR5FdQXzC9o_xf0O24Zo5GZWYeYUgCBy18t21urQXHIroxbqGzY5C-BE911573s7fXBUk6xLTSCeJybXaEdnW0JT2ge1g==&X-Bogus=DFSzKIVLAhJANHtetiSeBz9WcBn/&_signature=_02B4Z6wo00001tXM51AAAIDC1cznUAN-huLVzuPAANDl8b"

# Number of threads and requests per thread
num_threads = 1000
requests_per_thread = 1

# Dictionary to store the count for each URL
url_counts = defaultdict(int)
lock = threading.Lock()

def make_requests(thread_num):
    for _ in range(requests_per_thread):
        response = requests.get(url)
        try:
            question_url = response.json()["data"]["question"]["url1"]
            with lock:
                url_counts[question_url] += 1
        except KeyError:
            print(f"Thread {thread_num}: Error parsing response:", response.text)

# Create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=make_requests, args=(i,))
    threads.append(thread)
    thread.start()


# Wait for all threads to finish
for thread,j in threads:
    thread.join()
    print(j)

# Save the data to a file
with open("url_counts_threaded.txt", "w") as file:
    for question_url, count in url_counts.items():
        file.write(f"{question_url} | {count}\n")

print("Data saved to url_counts_threaded.txt")
