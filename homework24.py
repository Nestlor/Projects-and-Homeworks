# 1)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# def get_currency_rates():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
#     try:
#         driver.get("https://www.cbr.ru/")
#         time.sleep(3)

#         usd_rate = driver.find_element(By.XPATH, '//div[@class="main-indicator_rate"][contains(., "USD")]').text
#         eur_rate = driver.find_element(By.XPATH, '//div[@class="main-indicator_rate"][contains(., "EUR")]').text
        
#         print(f"Курс USD: {usd_rate}")
#         print(f"Курс EUR: {eur_rate}")
        
#         return {"USD": usd_rate, "EUR": eur_rate}
        
#     except Exception as e:
#         print(f"Ошибка при получении курсов валют: {e}")
#     finally:
#         driver.quit()

# currency_rates = get_currency_rates()

# 2) я не понял как его делать. А в первом использовал сайт который нормально у меня сработал