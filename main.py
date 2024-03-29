from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv

driver = webdriver.Edge()

driver.get("https://en.wikipedia.org/wiki/List_of_films")

time.sleep(2)

# alpha_numerical_table = driver.find_elements(
#     By.CLASS_NAME, "//table[@class='wikitable']/tbody/"
# )

alpha_numerical_table_items = driver.find_elements(
    By.XPATH, "//a[contains(@title, 'List of films: ')]"
)

initial_movie_link_list = pd.DataFrame(columns=["movie_name", "wiki_link"])
csv_columns = ["movie_name", "wiki_link"]
with open("movie_titles.csv", "a+", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_columns)

for item in alpha_numerical_table_items:
    item.click()
    all_movies_on_the_page_links_01 = driver.find_elements(
        By.XPATH, "//div[@class='div-col']/ul/li/a"
    )
    all_movies_on_the_page_links_02 = driver.find_elements(
        By.XPATH, "//div[@class='div-col']/ul/li/i/a"
    )
    all_movies_on_the_page_links = (
        all_movies_on_the_page_links_01 + all_movies_on_the_page_links_02
    )
    for movie_link in all_movies_on_the_page_links:
        temp_list = []
        print(f"movie name {movie_link.get_attribute('title')}")
        print(f'wiki link {movie_link.get_attribute("href")}')
        temp_list.append(movie_link.get_attribute("title"))
        temp_list.append(movie_link.get_attribute("href"))
        with open("movie_titles.csv", "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(temp_list)
    time.sleep(2)
    driver.back()
initial_movie_link_list.to_csv("test.csv")

driver.quit()
