# A Scraper to create a list of movies on Wikipedia and their links
### Getting the list of movie titles and links
First script, ``create_titles_list.py``, loads the this [Wikipedia page](https://en.wikipedia.org/wiki/List_of_films) using Selenium and exports the movie titles and their page links to a csv file. Csv file is name ``initial_movie_titles_links_list.csv``

Selenium driver clicks on each letter through the page and collects the info of the files listed on each page.

### Cleaning the initial list
In this step the Jupyter notebook, ``clean_up_initial_list``, is used to clean up and, in this case, remove the items with missing titles and export them to a separate list.
Result is saved in the file ``movie_titles_and_wiki_links.csv``.
