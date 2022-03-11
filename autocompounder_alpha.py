from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import getpass
from datetime import datetime
from selenium.webdriver.support import wait,expected_conditions as EC
import undetected_chromedriver.v2 as uc

if __name__ == "__main__":

    # datetime object containing current date and time
    def date_time():
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string


    user = getpass.getuser()
    #update your MM password below
    password = r"YOUR MM PASSWORD HERE"
    options = Options()

    #Path to your chrome profile - change if your location is in a different place
    pth = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\Profile 1"
    options = uc.ChromeOptions()
    options.add_argument('--disable-popup-blocking')
    # setting profile
    options.user_data_dir = pth

    # MAKE SURE YOU SWITCH THE VERSION OF CHROME TO YOUR VERSION , MY VERSION IS 99
    driver = uc.Chrome(options=options,version_main=99)

    wait = WebDriverWait(driver, 20)
    driver.get('https://theanimal.farm')

    driver.execute_script("window.open('');")

    # Define window handles
    af_tab = driver.window_handles[0]
    mm_tab = driver.window_handles[-1]

    # Move to MM window
    driver.switch_to.window(mm_tab)

    # Open MM Extension
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')



    #Send MM password
    pw_xpath = '//*[@id="password"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, pw_xpath)))
    time.sleep(2)
    driver.find_element_by_xpath(pw_xpath).send_keys(password, Keys.ENTER)
    time.sleep(5)

    # Go to the animal farm window and connect wallet
    connect_wallet_xpth = "//nav//div//button[contains(.,'Connect Wallet')]"
    mm_icon_xpth = "//button[@id='wallet-connect-metamask']"
    driver.switch_to.window(af_tab)
    time.sleep(1)
    mm_action = driver.find_element_by_xpath(connect_wallet_xpth)
    driver.execute_script("arguments[0].click();", mm_action)
    wait.until(EC.element_to_be_clickable((By.XPATH, mm_icon_xpth)))
    time.sleep(1.75)
    icon = driver.find_element_by_xpath(mm_icon_xpth)
    driver.execute_script("arguments[0].click();", icon)
    print('Animal Farm loaded')

    # Navigate to Drip Garden
    garden_xpth = "//a[contains(.,'Drip Garden')]"
    wait.until(EC.element_to_be_clickable((By.XPATH, garden_xpth)))
    garden = driver.find_element_by_xpath(garden_xpth)
    driver.execute_script("arguments[0].click();", garden)
    driver.refresh()


    def main():
        time.sleep(1.5)
        # Extract the data
        time.sleep(5)   # sleep until the animal farm UI is updated
        plants_grown_xpth = "//div[contains(text(),'Plants grown')]"
        wait.until(EC.element_to_be_clickable((By.XPATH, plants_grown_xpth)))

        while True:
            try:
                plants_available_xpth = "//div[contains(text(),'0d 0h ')]"
                avail_plants = driver.find_element_by_xpath(plants_available_xpth).text
                # stripping out the words
                avail_plants = avail_plants.split('(')[-1]
                avail_plants = avail_plants.split()[0]
                break
            except:
                print('No Plants Detected.... Sleeping for 1 min')
                time.sleep(60)


        print(f'You have {avail_plants} plants ready to sow now')

        # Extract the data
        # Plants Grown
        plants_grown_xpth = "//div[contains(text(),'Plants grown')]"
        plants_grown = driver.find_element_by_xpath(plants_grown_xpth).text
        plants_grown = plants_grown.split(':')[-1].strip()
        seeds_per_day = int(plants_grown) * 86400  # how many seeds 1 plant produces per day
        print(f'Plants Grown: {plants_grown}')

        # Future update will log these to a notepad or excel sheet for data tracking :)
        # LP Available
        lp_avail_xpth = "//div[contains(text(),'Available Seed Value')]"
        lp_avail = plants_grown = driver.find_element_by_xpath(lp_avail_xpth).text
        lp_avail = lp_avail.split(':')[-1]
        lps = lp_avail.split('LP')

        # VALUES
        lp_avail = lps[0].strip()
        lp_avail_usd = lps[-1].strip().replace('(', '').replace(')', '').replace('$', '')
        print(f'LP avail: {lp_avail}')
        print(f'LP USD avail: {lp_avail_usd}')

        # Click Compound..... need to replace with the javascript click instead
        compound_xpth = "//button[contains(.,'Plant seeds')]"
        compound = driver.find_element_by_xpath(compound_xpth)
        driver.execute_script("arguments[0].click();", compound)
        time.sleep(5)
        driver.switch_to.window(mm_tab)
        time.sleep(5)
        xpth = "//*[@id='app-content']//h2[contains(.,'Contract Interaction')]"
        contract_interaction = driver.find_element_by_xpath(xpth)
        driver.execute_script("arguments[0].click();", contract_interaction)

        time.sleep(5)
        xpth = "//button[contains(.,'Confirm')]"
        contract_interaction = driver.find_element_by_xpath(xpth)
        driver.execute_script("arguments[0].click();", contract_interaction)
        time.sleep(30)
        driver.switch_to.window(af_tab)
        driver.refresh()
    while True:
        main()


