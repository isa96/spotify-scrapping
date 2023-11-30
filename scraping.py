from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import argparse

driver = webdriver.Chrome('C:/Users/ASUS/Downloads/chromedriver_win32r') #should use r in the behind of the path

def scraping(spotify_playlist_url, output_csv):
    driver.get(spotify_playlist_url)
    driver.implicitly_wait(10) # because this is a dynamic website we need to used this implicitly_wait() function
    time.sleep(3)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True: 
        
        driver.execute_script(f"window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(5)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        
        last_height = new_height

    # Now that all data is loaded, scrape it
    titles = driver.find_elements('xpath','//div[@class="Type__TypeElement-sc-goli3j-0 fZDcWX t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line"]')
    artists = driver.find_elements('xpath','//span[@class="Type__TypeElement-sc-goli3j-0 bDHxRN rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line"]')
    albums = driver.find_elements('xpath','//span[@class="Type__TypeElement-sc-goli3j-0 ieTwfQ"]')
    durations = driver.find_elements('xpath','//div[@class="Type__TypeElement-sc-goli3j-0 bDHxRN Btg2qHSuepFGBG6X0yEN"]')
    songs_img = driver.find_elements('xpath','//img[@class="mMx2LUixlnN_Fu45JpFB rkw8BWQi3miXqtlJhKg0 Yn2Ei5QZn19gria6LjZj"]')
  
    all_data = []

    for index in range(len(titles)):

        all_data.append({
            "title": titles[index].text,
            "artist": artists[index].text,
            "album": albums[index].text,
            "duration": durations[index].text,
            "album_image": songs_img[index].get_attribute('src')
        })
        
    df = pd.DataFrame(data=all_data)
    df.to_csv(output_csv, index=False)

    return f"data has been saved in {output_csv}"

# getData("https://open.spotify.com/playlist/0L39AS9Z3C8A8Pt0YZvT9p", "playlist.csv")

if __name__ == "__main__":

# Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-u", "--url", help = "file path of your dataset")
    parser.add_argument("-o", "--output", help = "output filepath")
    
    # Read arguments from command line
    args = parser.parse_args()

    scraping(args.url, args.output)