from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver = Chrome(options=option)
url = 'https://login.zhipin.com/?ka=header-login'
driver = webdriver.Chrome(executable_path=r'C:\Users\lenovo\Desktop\chromedriver_win32\chromedriver.exe',options=option)
driver.get(url)

def huakuai():
# id = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[5]/div[1]').get_attribute('data-nc-idx')
# print(id)
# time.sleep(0.5)
# huakuai = driver.find_element_by_xpath('//*[@id="nc_{}_n1z"]'.format(id))
# action = ActionChains(driver)
# action.click_and_hold(huakuai).perform()
# time.sleep(1)
# for i in range(12):
#     action.move_by_offset(i, 0).perform()
# action.release().perform()
# action.release(on_element=huakuai).perform()
    pass
time.sleep(5)

driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[3]/span[2]/input').click()
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[3]/span[2]/input').send_keys('你的账号')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[4]/span/input').click()
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[4]/span/input').send_keys('你的密码')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[6]/button').click()
time.sleep(2)
'''地点'''
# driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/span').click()
# from selenium.webdriver import ActionChains
# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/form/div[3]/ul/li[1]')).perform()
# driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/form/div[3]/div/ul[1]/li[5]').click()
# time.sleep(100)     #深圳

driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/form/div[1]/p/input').click()
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/form/div[1]/p/input').send_keys('python开发')

driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/form/button').click()
time.sleep(11)

time.sleep(1)
liebiao1_url = driver.current_url+'&page={}'
time.sleep(1)
for j in range(1,5):
    liebiao_url=liebiao1_url.format(j)
    print(liebiao_url)
    driver.get(liebiao_url)
    time.sleep(2)
    print(driver.current_url)
    print("==========================")
    # print("列表链接",liebiao_url)
    try:
        for i in range(1,30):
            if j==1:
                ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[3]'.format(i))).perform()
                time.sleep(0.5)
                xiangqing_url = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[1]/h3/a'.format(i)).get_attribute('href')
                # print(xiangqing_url)
            else:
                ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/ul/li[{}]/div/div[3]'.format(i))).perform()
                time.sleep(0.5)
                xiangqing_url = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/ul/li[{}]/div/div[1]/h3/a'.format(i)).get_attribute('href')

            driver.get(xiangqing_url)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div[3]/div[1]/a').click()
            time.sleep(0.5)
            print(driver.current_url)
            if 'https://www.zhipin.com/job_detail' in str(driver.current_url):
                driver.back()
                time.sleep(1.5)
            else:
                time.sleep(1.5)
                driver.back()
                time.sleep(2)
                driver.back()
                time.sleep(2)
    except:
        pass
