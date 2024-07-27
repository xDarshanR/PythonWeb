from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# Project Built By Darshan R


def get_price(url, site):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode

    # Set up WebDriver service
    service = Service('/usr/local/bin/chromedriver')

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the URL
        driver.get(url)

        # Initialize price variable
        price = None

        # Determine which site we're scraping and apply the correct selector
        if site == 'amazon':
            try:
                price_element = driver.find_element(
                    By.CSS_SELECTOR, '.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay')
                price = price_element.text
            except NoSuchElementException:
                pass
        elif site == 'croma':
            try:
                price_element = driver.find_element(
                    By.CLASS_NAME, 'cp-price.main-product-price.pdp-cp-price')
                price = price_element.text
            except NoSuchElementException:
                pass
        elif site == 'reliancedigital':
            try:
                price_element = driver.find_element(
                    By.CLASS_NAME, 'pdp__priceSection__priceListText')
                price = price_element.text
            except NoSuchElementException:
                pass

        return price
    finally:
        # Clean up
        driver.quit()


# Example usage
amazon_url = 'https://www.amazon.in/Dell-Snapdragon-30-120Hz-Qualcomm-Graphite/dp/B0D8BPJSXC/ref=pd_sbs_d_sccl_1_3/259-7202136-1091960?pd_rd_w=UE7Mh&content-id=amzn1.sym.ca63db25-99cc-4f57-b23d-7e02dd5628b0&pf_rd_p=ca63db25-99cc-4f57-b23d-7e02dd5628b0&pf_rd_r=4JE0SWBX5Q3JYEF01XJH&pd_rd_wg=LVpYF&pd_rd_r=9067a6bb-a51a-4fb3-bde0-28b7eaef0700&pd_rd_i=B0D8BPJSXC&psc=1'
croma_url = 'https://www.croma.com/apple-ipad-10th-generation-wi-fi-10-9-inch-64gb-silver-2022-model-/p/264260?utm_source=google&utm_medium=ps&utm_campaign=Sok_Pmax_Tablets_iPad&gad_source=1&gclid=CjwKCAjwko21BhAPEiwAwfaQCNk_VIRAdyU1Q4H1LeO4ZPlOLKhC6hnc94Fa9uqr7cB840lfWaDBOBoCKioQAvD_BwE'  # Replace with actual Croma URL
reliancedigital_url = 'https://www.reliancedigital.in/oppo-a3-pro-5g-128-gb-8-gb-ram-starry-black-mobile-phone/p/494421584'

# Fetch prices
amazon_price = get_price(amazon_url, 'amazon')
croma_price = get_price(croma_url, 'croma')
reliancedigital_price = get_price(reliancedigital_url, 'reliancedigital')

# Print Price
print(f'The price on Amazon is: {amazon_price}')
print(f'The price on Croma is: {croma_price}')
print(f'Reliance Digital has an {reliancedigital_price}')  #
