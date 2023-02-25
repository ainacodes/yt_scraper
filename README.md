# Youtube Scraper

## What it does?
1. Read the data from excel file `data.xlsx`.
2. Pass the search term in the search box.
3. Collect the data from the first 50 results that appear on the search page.
4. Save the results in `csv` file. The results include: 
    * Title
    * Link
    * Views
    * Duration
    * Date
    * Channel Name
   
    [Example result](https://github.com/ainacodes/yt_scraper/blob/master/video_data.csv)
    
## Setup and Installation
1. Have python and [ChromeDriver](https://chromedriver.chromium.org/) installed.
2. Clone this repository:
    ```
    git clone https://github.com/ainacodes/yt_scraper.git
    ```

3. Install the necessary packages:
    ```
    pip install requirements.txt
    ```
4. Delete  `video_data.csv` file. Can change the file name in `line 73`
5. Add any word that you wish to searh under `Search Term` from `data.xlsx` file.
6. Run the code.
