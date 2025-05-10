from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def get_marketplace_prices():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://www.wildberries.ru/catalog/elektronika/noutbuki")
        time.sleep(3)

        for _ in range(3):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(1)

        price_elements = driver.find_elements(
            By.CSS_SELECTOR, 
            '.price__lower-price, .price__lower-price-wallet'
        )

        prices = [el.text.replace('₽', '').replace(' ', '') for el in price_elements]
        
        print(f"Найдено {len(prices)} товаров:")
        for i, price in enumerate(prices[:10], 1):
            print(f"{i}. {price} руб.")
            
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

get_marketplace_prices()
