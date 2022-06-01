from selenium.webdriver.common.by import By

class odamax_locators:
    pop_up = (By.XPATH, "//button[@class='mfp-close wis-mfp-close-203581']")
    cookies = (By.XPATH, "//a[contains(.,'Kapat')]")
    search_bar = (By.XPATH, "//input[@id='tb-autocomplete']")
    search_selected = (By.XPATH, "//a[contains(.,'İzmir, Ege Bölgesi Türkiye, Türkiye İzmir, Ege Bölgesi Türkiye, Türkiye')]")
    check_in = (By.XPATH, "//div[@class='check-in-wrapper']")
    check_out = (By.XPATH, "//div[@class='check-out-wrapper']")
    check_in_date = (By.XPATH, "//div[@class='drp-calendar col left']//td[contains(.,'16')]")
    check_out_date = (By.XPATH, "//div[@class='drp-calendar col left']//td[contains(.,'18')]")
    check_out_date_other_month = (By.XPATH,"//div[@class='drp-calendar col right']//td[contains(.,'14')]]" )
    search_button = (By.XPATH, "//button[contains(.,'Arama Yap')]")
    