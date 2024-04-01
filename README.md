# A Scraper to create a list of movies on Wikipedia and their details
### Get the list of movie titles and links
First script, ``create_titles_list.py``, loads the this [Wikipedia link](https://en.wikipedia.org/wiki/List_of_films) using Selenium and exports the movie titles and their page links to a csv file.

### Cleaning the initial list
In this step the Jupyter notebook, ``clean_up_initial_list``, is used to clean up and, in this case, remove the items with missing titles and export them to a separate list.