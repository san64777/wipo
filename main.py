from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logging.basicConfig(level=logging.INFO)

def get_search_results_count(term, proxy, max_retries=3):
	# Prepare the proxy
	chrome_options = Options()
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("--log-level=3")  # Suppress logging
	chrome_options.add_argument("--disable-logging")  # Suppress logging
	chrome_options.add_argument('--ignore-certificate-errors')
	
	webdriver.DesiredCapabilities.CHROME['proxy'] = {
		"httpProxy": proxy,
		"ftpProxy": proxy,
		"sslProxy": proxy,
		"proxyType": "MANUAL",
	}

	driver = webdriver.Chrome(options=chrome_options)

	retries = 0
	while retries < max_retries:
		try:
			driver.get("https://branddb.wipo.int/en/quicksearch")
			
			search_box = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.XPATH,'//*[contains(text(),"Search by brand name")]/following-sibling::input'))
			)
			search_box.send_keys(term)
			
			search_button = WebDriverWait(driver, 10).until(
				EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Search")]'))
			)
			search_button.click()
			try:
				WebDriverWait(driver, 10).until(
					lambda driver: driver.find_element(By.XPATH, '//div[@data-test-id="resultsCount"]').text.strip() not in ["", "Loading..."]
				)
				results_text = driver.find_element(By.XPATH, '//div[@data-test-id="resultsCount"]').text

			except TimeoutException:
				print("Timed out waiting for element to appear")
				results_text = ""

			except IndexError:
				print("IndexError occurred")
				results_text = ""

			if "No results found!" in results_text:
				print("No results found for the search term.")
				return 0
			results_count = int(results_text.split('of')[1].strip().split(' ')[0])
			return results_count
			

		except NoSuchElementException as e:
			logging.error("Element not found, check your XPaths or element identifiers.")
			logging.error(str(e))

		except WebDriverException as e:
			logging.error("Browser or WebDriver issue encountered.")
			logging.error(str(e))

		except Exception as e:
			logging.error(f"An unexpected error occurred: {str(e)}")

		finally:
			driver.quit()

		retries += 1
		logging.info(f"Retry attempt {retries}/{max_retries}...")
		time.sleep(5)  # Pause before retrying to avoid hammering the site and also for transient issues to potentially resolve

	logging.error("Max retries reached. Exiting function.")
	return None
	
if __name__ == "__main__":
	term = input("Enter the search term: ")
	proxy = "194.102.39.101:12345:tbtbtb:mxVFyaOE"
	
	results_count = get_search_results_count(term, proxy)
	
	if results_count is not None:
		print(f"Number of results found: {results_count}")