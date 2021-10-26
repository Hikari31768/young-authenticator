from selenium import webdriver
import os, muggle_ocr, time
def login( username, password, portal_url):
    # 模拟手机登录
    WIDTH = 320
    HEIGHT = 640
    PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

    # 填入用户名和密码
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(portal_url)
    time.sleep(1)
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    # 验证码识别
    code_elem = browser.find_element_by_xpath('//*[@id="image_code"]')
    code_elem.screenshot("code.png")
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
    with open("code.png","rb") as f:
        img=f.read()
    code=sdk.predict(image_bytes=img)
    browser.find_element_by_id("code").send_keys(code)
    browser.find_element_by_xpath('//*[@id="login"]/form/div[5]/div/button').click()

    # 清除临时文件
    os.remove("code.png")
    browser.quit()