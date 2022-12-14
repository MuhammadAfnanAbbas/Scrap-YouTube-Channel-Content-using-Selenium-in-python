from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.youtube.com/channel/UCEvTnUBoNZn5otRTotKjDeg/videos'

driver =  webdriver.Chrome()
driver.get(url)
element = driver.find_element('xpath', '//body')
while True:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-item-renderer')
    video_list = []
    print(type(videos))
    print(len(videos))
    for video in videos:
            title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
            views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
            upload_date = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text 
            vid_item = {
                    'Title':title,
                    'Views': views,
                    'Upload Date': upload_date
                }
            video_list.append(vid_item)
            df = pd.DataFrame(video_list)
            df.to_csv('Techie World.csv', index=False)
            print(df)
    break
driver.quit()