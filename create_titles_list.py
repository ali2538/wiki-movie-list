from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv


def retrieve_titles_and_links() -> None:
    driver = webdriver.Edge()

    driver.get("https://en.wikipedia.org/wiki/List_of_films")

    time.sleep(2)

    alpha_numerical_table_items = driver.find_elements(
        By.XPATH, "//a[contains(@title, 'List of films: ')]"
    )

    initial_movie_link_list = pd.DataFrame(columns=["movie_name", "wiki_link"])
    csv_columns = ["movie_name", "wiki_link"]
    with open("initial_movie_titles_links_list.csv", "w", newline="") as csv_file:
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
            temp_list.append(movie_link.get_attribute("title"))
            temp_list.append(movie_link.get_attribute("href"))
            with open(
                "initial_movie_titles_links_list.csv", "a", newline=""
            ) as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(temp_list)
        time.sleep(5)
        driver.back()
        time.sleep(1)
    initial_movie_link_list.to_csv("test.csv")

    driver.quit()


if __name__ == "__main__":
    retrieve_titles_and_links()
