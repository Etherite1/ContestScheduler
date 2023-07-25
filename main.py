from bs4 import BeautifulSoup
import leetcode_scraper

def scrape_open_html():
    with open('home.html', 'r') as html_file:
        content = html_file.read()
        bs = BeautifulSoup(content, 'lxml')
        course_cards = bs.find_all('div', class_='card')
        course_num = 1
        for card in course_cards:
            name = card.find('h5').text
            price = card.find('a').text.split(" ")[-1]
            print(f'''Course {course_num}:\n\tName: {name}\n\tPrice: {price}''')
            course_num += 1

if __name__ == '__main__':
    # scrape_open_html()
    leetcode_scraper.scrape()
