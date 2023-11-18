from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")

# Get the title of the webpage and print it
title = driver.title
print("Title of the webpage:", title)

# Find the main content element on the page
content_element = driver.find_element(By.ID, "mw-content-text")

# Get the text content of the main content element
page_content = content_element.text

# Print the extracted text
print(page_content)

# Close the browser window
driver.quit()
