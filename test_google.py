def test_google():
    import time
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.google.com/')

    search_input = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    search_input.send_keys('facebook' +"\n")
    enter_facebook = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
    enter_facebook.click()
    phone = driver.find_element_by_xpath('//*[@id="email"]')
    phone.send_keys('+380635843742')
    password = driver.find_element_by_xpath('//*[@id="pass"]')
    password.send_keys('257992ss')
    entrance = driver.find_element_by_xpath('//*[@id="u_0_b"]')
    entrance.click()

    def button_wait(driver):
        button_spas = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/span/div')
        button_spas.click()
        return (button_spas)

    WebDriverWait(driver, 5).until(button_wait)

    def profil_wait(driver):
        acount = driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/span/span/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div[1]')
        acount.click()
        return (acount)

    WebDriverWait(driver, 5).until(profil_wait)

    foto = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/h1/div/div[1]/span/div/a')
    foto.click()

    print(None)