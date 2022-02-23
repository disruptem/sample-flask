
def browserStackCaller(webdriver,time,userName,accessKey):
    print("Browserstackcaller called")
    # driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
    # driver = webdriver.Remote("http://localhost:4723", desired_caps)

    # driver.switchTo().alert().accept();


    # search_element = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Allow While Using App"))
    # )

    desired_caps = {
        "build": "browser_sample2",
        "name": "test 15",
        "device": "iPhone 12 Pro",
        "os_version": "14",
        "app": "bs://2ac0f7ef2d9f793923bdc53ed56d4db4ac404e95",
        # "browserstack.appium_version" : "1.21.0",
        # "browserstack.acceptInsecureCerts" : "true",
        # 'autoDissmissAlerts': 'true',
        "autoAcceptAlerts": "true",
        # "autoGrantPermissions": "true",
        # "gpsEnabled" : "true",
    }

    driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub",
                              desired_caps)

    driver.find_element_by_id("Don’t Allow").click()
    time.sleep(3)
    driver.find_element_by_id("Cancel").click()
    time.sleep(3)
    driver.find_element_by_id("Delivery").click()

    # search_element = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Delivery"))
    # )
    # search_input.send_keys("kuwait")
    # search_element.click()


    # search_input = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    # )
    # search_input.send_keys("BrowserStack")
    time.sleep(5)


    search_results = driver.find_elements_by_class_name("android.widget.TextView")
    assert(len(search_results) > 0)

    driver.quit()
