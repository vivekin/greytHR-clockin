import sys
import time
import logging
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("Script running ...")

# Configure the logger
datetime_object = datetime.now()
formatted_datetime = datetime_object.strftime("%Y_%m_%dT%H_%M_%S")
logging.basicConfig(
    filename=f"greythr_clock_{formatted_datetime}.log",  # Specify the log file name
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log message format
)

start_time = time.perf_counter()
logging.info(f"START - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

today = date.today()
logging.info(f"Today's date: {formatted_datetime}")
status={}

browser = webdriver.Edge()
# browser = webdriver.Firefox()

browser.get("https://xyz.greythr.com/uas/portal/auth/login")
time.sleep(5)
logging.info("Login page ...")
usrname=browser.find_element(By.XPATH, "/html/body/app-root/uas-portal/div/div/main/div/section/div[1]/o-auth/section/div/app-login/section/div/div/div/form/div[1]/div/input")
usrname.clear()
usrname.send_keys(sys.argv[1])
passw=browser.find_element(By.XPATH, "/html/body/app-root/uas-portal/div/div/main/div/section/div[1]/o-auth/section/div/app-login/section/div/div/div/form/div[2]/div/input")
passw.clear()
passw.send_keys(sys.argv[2])
submit=browser.find_element(By.XPATH, "/html/body/app-root/uas-portal/div/div/main/div/section/div[1]/o-auth/section/div/app-login/section/div/div/div/form/button")
browser.execute_script("arguments[0].click();", submit)
logging.info("Click Login, Start Sleep 15s")
time.sleep(15)
logging.info("Finish Sleep")
logging.info("Homepage ...")
clock=browser.find_element(By.XPATH, "/html/body/app/ng-component/div/div/div[2]/div/ghr-home/div[2]/div/gt-home-dashboard/div/div[2]/gt-component-loader/gt-attendance-info/div/div/div[3]/gt-button[1]")
browser.execute_script("arguments[0].click();", clock)
logging.info(f"Click {clock.text}")
time.sleep(3)
browser.delete_all_cookies()
browser.close()

logging.info(f"END - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
logging.info(f"Execution time: {elapsed_time:.2f} seconds\n")
print("Script exiting ...")

