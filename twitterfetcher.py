import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up ChromeDriver
browser = webdriver.Chrome()

# Load the XLSX file
data = pd.read_excel('/Users/waytoxlsxfile/influencers.xlsx')

# Define the function to fetch the score
def fetch_score(username):
    browser.get(f"https://tweetscout.io/search?q={username}")
    
    try:
        # Wait for up to 20 seconds for the score element to be present
        score_element = WebDriverWait(browser, 7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.Counter_text_big__Xkphn'))
        )
        return score_element.text
    except:
        print(f"Couldn't retrieve score for {username}.")
        return "N/A"

# Iterate over usernames and fetch scores
scores = []

for username in data['Unnamed: 0'].tolist():
    score = fetch_score(username)
    scores.append(score)
    time.sleep(5)  # Additional delay to avoid potential rate limits

# Close the browser
browser.quit()

# Save the results back to an XLSX file
data['Scores'] = scores
data.to_excel('/Users/wheretoputresult/output_scores.xlsx', index=False)
