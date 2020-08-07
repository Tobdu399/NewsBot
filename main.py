import os
from selenium import webdriver
import time

news_pages = {"yle" : "https://yle.fi/",
              "aamulehti" : "https://www.aamulehti.fi/",
              "ylöjärven uutiset" : "https://ylojarvenuutiset.fi/",
              }

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    browser = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + "/chromedriver", options=chrome_options)
    
    # ------------------------------------------------
    news_file = open(os.getcwd() + "/news.txt", "w")

    cursor = 0
    for page in news_pages:
        cursor += 1
        print("Finding news... " + str(cursor) + "/" + str(len(news_pages)) + " (" + page.upper() + ")")

        browser.get(news_pages[page])
        if page == "yle":
            time.sleep(1)
            browser.find_element_by_class_name("Group__group___3hyAU").click()
            header = browser.find_element_by_xpath("//h1[@class='yle__article__heading yle__article__heading--h1']").text
            news_file.write(page.upper() + "\n" + header + "\n" + browser.current_url)

        if page == "aamulehti":
            # Had to improvize with the url!
            time.sleep(1)
            header = browser.find_element_by_xpath("//div[@id='mainpipe']/div[1]/a/div[2]/h2").text
            url = browser.find_element_by_xpath("//div[@id='mainpipe']/div[1]/a")
            news_file.write("\n\n" + page.upper() + "\n" + header + "\n" + url.get_attribute("href"))

        if page == "ylöjärven uutiset":
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='squareblocks-content-wrap']/h3/a").click()
            header = browser.find_element_by_xpath("//h1[@class='entry-title single-title']").text
            news_file.write("\n\n" + page.upper() + "\n" + header + "\n" + browser.current_url)

    print("\nNews saved at '" + os.getcwd() + "/news.txt'")
    news_file.close()
    browser.close()

    
main()