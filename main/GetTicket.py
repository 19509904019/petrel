import time
from selenium.webdriver import ActionChains
from user import account
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 浏览器设置
s = Service(r'../driver/chromedriver.exe')
driver = webdriver.Chrome(service=s)
# 绕过selenium检测，即防止反爬
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {"source": """Object.defineProperty(navigator,'webdriver',{get: () => undefined})"""})
# 登录12306
url_str = r'https://kyfw.12306.cn/otn/resources/login.html'
driver.get(url_str)
# 窗口最大化
driver.maximize_window()


def get_ticket(page, from_station, to_station, date):
    # 输入账号和密码
    driver.find_element(by=By.CSS_SELECTOR, value='#J-userName').send_keys(account.username)
    driver.find_element(by=By.CSS_SELECTOR, value='#J-password').send_keys(account.password)

    # 点击登录
    driver.find_element(by=By.CSS_SELECTOR, value='#J-login').click()
    driver.implicitly_wait(10)

    # 拖动验证滑块
    elem1 = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
    elem2 = driver.find_element(By.CSS_SELECTOR, '#nc_1__scale_text')
    time.sleep(1)
    action = ActionChains(driver)
    action.click_and_hold(elem1)
    action.move_by_offset(elem2.size.get('width') - 40, 0)
    action.release()
    action.perform()
    driver.implicitly_wait(10)

    # 取消页面提示信息
    driver.find_element(by=By.CSS_SELECTOR, value='.modal-close .icon').click()

    # 买票
    driver.find_element(by=By.CSS_SELECTOR, value='#link_for_ticket').click()

    # 始发站
    driver.find_element(by=By.CSS_SELECTOR, value='#fromStationText').send_keys(Keys.ENTER)
    driver.find_element(by=By.CSS_SELECTOR, value='#fromStationText').clear()
    driver.find_element(by=By.CSS_SELECTOR, value='#fromStationText').click()
    driver.find_element(by=By.CSS_SELECTOR, value='#fromStationText').send_keys(from_station)
    driver.find_element(by=By.CSS_SELECTOR, value='#fromStationText').send_keys(Keys.ENTER)

    # 终点站
    driver.find_element(by=By.CSS_SELECTOR, value='#toStationText').clear()
    driver.find_element(by=By.CSS_SELECTOR, value='#toStationText').click()
    driver.find_element(by=By.CSS_SELECTOR, value='#toStationText').send_keys(to_station)
    driver.find_element(by=By.CSS_SELECTOR, value='#toStationText').send_keys(Keys.ENTER)

    # 出发日期
    driver.find_element(by=By.CSS_SELECTOR, value='#train_date').clear()
    driver.find_element(by=By.CSS_SELECTOR, value='#train_date').click()
    driver.find_element(by=By.CSS_SELECTOR, value='#train_date').send_keys(date)
    driver.find_element(by=By.CSS_SELECTOR, value='#train_date').send_keys(Keys.ENTER)

    # 查询车票
    driver.find_element(by=By.CSS_SELECTOR, value='#query_ticket').click()

    # 预定车票
    driver.find_element(by=By.CSS_SELECTOR, value=f'#queryLeftTable tr:nth-child({2 * page - 1}) .btn72').click()

    # 选择乘车人
    driver.find_element(by=By.CSS_SELECTOR, value='#normalPassenger_0').click()

    # 提交订单
    driver.find_element(by=By.CSS_SELECTOR, value='#submitOrder_id').click()

    # 选座
    driver.find_element(by=By.CSS_SELECTOR, value='#erdeng1 > ul:nth-child(4) > li:nth-child(2) a').click()
    driver.implicitly_wait(10)

    # 确认订单
    time.sleep(0.1)
    driver.find_element(by=By.CSS_SELECTOR, value='#qr_submit_id').click()
