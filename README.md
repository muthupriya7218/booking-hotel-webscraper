# 🏨 Booking.com Web Scraper

A Python script that scrapes hotel data from Booking.com search results pages and saves the extracted information into a CSV file.

---

## ✨ Features

- Extracts hotel information including:
  - Hotel name
  - Location
  - Price
  - Review summary
  - Rating
  - Number of reviews
  - Booking.com listing link
- Saves data to a CSV file for easy analysis.

---

## 📦 Requirements

- Python 3.x
- Libraries:
  - `beautifulsoup4`
  - `requests`
  - `lxml`

Install them using:

```bash
pip install beautifulsoup4 requests lxml

---

## How to use

Run the script and provide the booking.com search results URL and a file name to save the data.

```bash
python Bookingsdotcom.py

You will be prompted to enter:

-The booking.com URL to scrape
-The output CSV file name

## 📁 Sample Output
A sample output CSV file (db_hotels.csv) is included in this repository to show what the scraped data looks like.

##🖥️ Sample Terminal Output

Please enter url: https://www.booking.com/searchresults.html?...
Please give file name: db_hotels
Thank you for sharing the url and file name!
⏳
Starting the webscrapping
Connected to the website
Web Scrapping done

## ⚠️ Important Notes

-🧱 Website Structure May Change
This scraper depends on the HTML structure of Booking.com. If the website layout changes (which happens frequently), the scraper might stop working or return incorrect data.

If this happens:

Inspect the page using browser dev tools (Right Click > Inspect) to see if class names or tags have changed.

Update the corresponding parts of the BeautifulSoup parsing logic in the script.



