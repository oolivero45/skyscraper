# skyscraper
Python 3 and JavaScript scripts to scrape channel images from the Sky TV Guide. Tested to work in Chrome, but should work in all modern browsers.

## Requirements
- Python 3
- [tqdm](https://github.com/tqdm/tqdm) (Used for progress bars)

## Usage
*Steps 1 to 4 can be skipped, but it is strongly recommended that you do not skip them, as they will ensure you are using the most up-to-date list of channels possible. Skipping these steps means that you will download the images for all channels as of 2019-08-28, but will not download any images for channels added to the Sky TV Guide after that date.*

1. Visit the Sky TV Guide ([https://www.sky.com/tv-guide](https://www.sky.com/tv-guide)), and open your browser's developer tools.
2. Paste the contents of `jscrawl.js` into the console, and press enter.
3. Copy the entire output given by the console. In Chrome, you can do this by simply pressing the "copy" button that appears.
4. Paste the copied JSON data into `data.json`. If the file already contained any data, remove it before pasting. (You should be pasting into an empty file.)
5. If it does not already exist, create a directory adjacent to the scripts called `Images`.
6. Run `crawl.py`.
7. Once `crawl.py` has completed, all of the channel images will be in the `Images` directory.
