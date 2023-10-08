This project contains a simple Python web scraper script designed to perform searches on the WIPO Brand Database and retrieve the number of results found for a given search term.

Table of Contents
Prerequisites
Quick Start
Project Structure
Troubleshooting & Assistance

Prerequisites
Python: Ensure that Python (3.7 or later) is installed on your system. If not, download and install it from python.org.

Google Chrome: The script uses a Chrome WebDriver. Ensure Google Chrome is installed on your system.

Internet Access: Ensure you have internet access to fetch website data and utilize the proxy.

Quick Start
Install Dependencies:

Locate and double-click the setup.bat file to install the required Python packages.

Run the Script:

Execute the run.bat file by double-clicking it.
Enter your search term when prompted and press Enter.
The script will output the number of results found on the WIPO database for the entered term.

Project Structure:

main.py: The core Python script for web scraping. Takes a search term as input, interacts with the website, and returns the number of search results.

setup.bat: Batch file to install required Python packages for the script to run.

run.bat: Batch file to execute main.py, which allows you to interact with the script in a command prompt window.

get-pip.py: Script to install or upgrade pip, the Python packaging tool.

Troubleshooting & Assistance:

Web Driver Issue: Ensure Chrome is installed, and check for any updates. The web driver might face issues if the browser is not updated.

Package Installation: If encountering issues during package installation via setup.bat, try running it as administrator. Also, ensure you have proper internet access.

Script Errors: If the script does not return results as expected, ensure you are entering the search term correctly, and check your internet and proxy settings. Note that changes in the WIPO website structure can impact the script's functionality.

Dependency Versions: Although the current setup.bat does not specify versions, it is recommended to specify versions of Selenium and BeautifulSoup4 in production-grade applications to ensure compatibility and stability.

Should you encounter any issues not addressed above, please feel free to reach out, and I will be happy to assist!

