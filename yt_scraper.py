import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def collect_video_data(driver, video):
    title_raw = video.find_element(By.XPATH, './/a[@id="video-title"]').text.strip()
    title_new = title_raw.encode('ascii', 'ignore')
    title = str(title_new, 'utf-8').strip()

    link = video.find_element(By.TAG_NAME, 'a').get_attribute('href')    

    duration = video.find_element(By.TAG_NAME, 'span').get_attribute('aria-label')

    details = video.find_elements(By.XPATH, './/div[@id="metadata-line"]//span[@class="inline-metadata-item style-scope ytd-video-meta-block"]')
    views = details[0].text
    date = details[1].text

    channel_name_raw = video.find_element(By.ID, 'channel-info').text
    channel_name_new = channel_name_raw.encode('ascii', 'ignore')
    channel_name = str(channel_name_new, 'utf-8').strip()

    # Return the collected data
    return {
        'Title': title,
        'Link': link,
        'Views': views,
        'Duration': duration,
        'Date': date,
        'Channel Name': channel_name
    }

def scrape_videos(driver, search_term):
    # Go to the YouTube homepage
    driver.get('https://www.youtube.com')

    # Find the search box and enter the search term
    search_input = driver.find_element(By.XPATH, '//input[@id="search"]')
    search_input.send_keys(search_term)
    search_input.submit()

    # Wait for the search results to load
    time.sleep(2)

    while len(driver.find_elements(By.CSS_SELECTOR, '#video-title')) < 50:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)


    # Find the videos
    videos = driver.find_elements(By.XPATH, '//ytd-video-renderer')

    video_data = [collect_video_data(driver, video) for video in videos[:50]]

    return video_data

# Read the data from the Excel file
data = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Set up the webdriver
driver = webdriver.Chrome()

# Scrape the videos for each search term
video_data = []
for index, row in data.iterrows():
    search_term = row['Search Term']
    video_data.extend(scrape_videos(driver, search_term))

# Convert the collected data to a pandas DataFrame
video_data = pd.DataFrame(video_data)

# Save the data to a CSV file
video_data.to_csv('video_data.csv', index=False)

# Close the webdriver
driver.close()
