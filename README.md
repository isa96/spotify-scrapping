# SCRAPPING SPOTIFY DATA

This project will scraping data from **Spotify playlist URL** using Selenium and Python. You can see the full explanation of this project through this link: [Scraping Spotify Playlist using Python and Selenium](https://medium.com/@felixpratama242/scraping-spotify-playlist-using-python-and-selenium-17e0175f2db2)

To run this project you can clone using this command:
```
git clone https://github.com/lixx21/spotify-scrapping.git
```

Then you can install the libraries that needed to run this project:
```
pip install -r requirements.txt
```

After that you can run the python script using the following command:
```
python scraping.py -u {spotify_playlist_url} -o {csv_file.csv}
```

For the example of how to run the script is like this:
```
python scraping.py -u https://open.spotify.com/playlist/0L39AS9Z3C8A8Pt0YZvT9p -o mix.csv

```

NOTE:
**To fetch more data from your playlist, you need to scroll down when the website is open through the web drive, because if you want to load all the data in spotify, you need to scroll down until the last page and we have solved this using infinite scroll**