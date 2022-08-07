from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from time import sleep
from random import choice,randint
import utils
import os
from selenium import *
from fake_useragent import UserAgent
import argparse
from colorama import Fore
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
r = Fore.RED
g = Fore.GREEN
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")
args = parser.parse_args()

def GetRandomProxyForStream():
        proxies_file = ReadFile(os.getcwd()+'/proxies.txt','r')
        return choice(proxies_file)
    
def ReadFile(filename,method):
        #f = open(filename,method)
        #try:
            #content = [line.strip('\n') for line in f]
            #return content
        #finally:    
            #f.close() 
        with open(filename,method) as f:
            content = [line.strip('\n') for line in f]
            return content

try:
        rounds = 100#int(input(f'{y}[{b}?{y}]{g} how many accounts: '))

except:
        print(f'\n{r}[{b}!{r}]{r} Type a correct integer')
        exit()
for i in range(rounds):
        ua = UserAgent()
        userAgent = ua.random
        if args.firefox:
                try:
                        firefox_driver_path = str(input(f'{y}[{b}?{y}]{g} A firefox driver path: '))

                        profile = webdriver.FirefoxProfile()
                        profile.set_preference("general.useragent.ovrride", userAgent)    
                        driver = webdriver.Firefox(firefox_profile=profile, executable_path=f'{firefox_driver_path}') # Put chrome driver path here!
                except:
                        print(f'\n{r}[{b}!{r}]{r} Set your firefox driver')
                        break
        #Chrome driver: 

        if args.chrome:
                try:
                        #chrome_driver_path = str(input(f'{y}[{b}?{y}]{g} A chrome driver path: '))
                        from selenium.webdriver.chrome.options import Options
                        options = Options()
                        options.add_argument(f'user-agent={userAgent}') 
                        
                        #For ChromeDriver version 79.0.3945.16 or over
                        #driver = webdriver.Chrome() # Put chrome driver path here!
                except:
                        print(f'\n{r}[{b}!{r}]{r} Set a valid path')
                        break       
                    
                                     
        #options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')
        options.add_argument('--lang=en')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--mute-audio")
        options.add_argument('--disable-features=UserAgentClientHint')
        options.add_argument("--disable-web-security")
        options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US,en'})
        options.add_argument('--disable-blink-features=AutomationControlled')
        while True:
            try:
                #proxy='http://{0}'.format(GetRandomProxyForStream())
                #print(proxy)
                #options.add_argument('--proxy-server=http://{0}'.format(proxy))
                driver = webdriver.Chrome(options=options)
                driver.get('https://www.instagram.com/accounts/emailsignup')  
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[1]/div/img')))      
                #                                                                       /html/body/div[3]/div/section/main/div/div/div[1]/div[1]/div/img
                break
            except:                           
                continue
            
        
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.moakt.com/en/inbox")
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/form/input[2]')))
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/form/input[2]'))).click() 
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]')))   
        mail_address = driver.find_element_by_id('email-address').text
        print(mail_address)
        while mail_address == "Please wait...":
                mail_address = driver.find_element_by_id('email-address').text
        else:
                mail_address = mail_address
        driver.switch_to.window(driver.window_handles[0])

        # Accepting cookies window
        try:
                cookie = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:
                pass
        name = utils.username()

        # Fill email
        sleep(0.5)
        email_field = driver.find_element_by_name('emailOrPhone')
        email_field.send_keys(mail_address)
        print('email: ' + mail_address)
        
        # fill full name

        fullname_field = driver.find_element_by_name('fullName')
        fullname_field.send_keys(utils.generatingName())
        print('Full name: '+ utils.generatingName())
        #fill username
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(name)


        print('username: ' + name)

        # Fill password 

        password_field = driver.find_element_by_name('password')
        sleep(0.5)
        password_field.send_keys(utils.generatePassword())  # You can determine another password here.
        sleep(0.5)
        password = utils.generatePassword()
        sumbit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
        #sleep(3)
        print('password: ' + password)


        unavail_mess = ["username"]
        sleep(1.2)
        # New username if unavailable
        try :
                unavailable_user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/p').text
                print(unavailable_user)
                if unavailable_user in unavail_mess: 

                        print('username unavailable. Generating a new username...')
                        username_clear = driver.find_element_by_name('username').clear()
                        sleep(1)
                        username_field.send_keys(name,Keys.ENTER)
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div[1]/div[2]/form/div[7]/div/button').click()
                else :

                        break
        except:

                pass
        

        # Birthdate values 
        sleep(1.2)
        print('')
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option["+str(randint(1,12))+"]"))).click()

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option["+str(randint(1,28))+"]"))).click()

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option["+str(randint(18,45))+"]"))).click()
        
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
        sleep(0.5)

        
        # Requesting the verification code

        print("Waiting for the verification code...")
        driver.switch_to.window(driver.window_handles[1])
        sleep(5)
        
        invalid_code = ['No messages in your inbox at the moment. You Can refresh the page to check again.']
        invalid_now = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td").text
        #/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]
        #print(invalid_now)
        while invalid_now in invalid_code:
                #/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a[2]/label
                invalid_now = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td").text
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a[2]/label'))).click() 
                print("Refresh Mail List")
                sleep(5)
        else:                
                code = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/a").text
                code = code[:6]
                print("Confirmation Code is: "+ code)

        driver.switch_to.window(driver.window_handles[0])

        # Security code  
        driver.find_element_by_name('email_confirmation_code').send_keys(code, Keys.ENTER)
        sleep(20)
        
        invalid_code = ['Sorry, something went wrong creating your account. Please try again soon.']
        invalid_now = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div").text
        print(invalid_now)
        
        while invalid_now in invalid_code:
                print("deneniyor")
                #/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a[2]/label
                invalid_now = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div").text
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button'))).click()                 
                sleep(5)
        else:                
                break
                
        try:
                not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
                #/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div
                if not_valid.text == 'That code isn\'t valid. You can request a new one.' :

                        sleep(1)
                        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
                        sleep(5)
                        confInput = driver.find_element_by_name('email_confirmation_code')
                        confInput.send_keys(Keys.CONTROL + "a")
                        confInput.send_keys(Keys.DELETE)
                        confInput.send_keys(code, Keys.ENTER)
                        sleep(3)
                else:
                        print('Account created information stored on a credentials.txt ')
        except:
                pass
        with open('credentials/credentials.txt','a') as f:
                f.write(f"""Email: {mail_address}\nUsername: {name}\nPassword:{password}\n  -----------""")
