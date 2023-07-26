from bs4 import BeautifulSoup
import leetcode_scraper
import codeforces_scraper

if __name__ == '__main__':
    # scrape_open_html()
    leetcode_scraper.scrape()
    codeforces_scraper.scrape();