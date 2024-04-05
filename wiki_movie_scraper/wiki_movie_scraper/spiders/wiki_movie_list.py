import scrapy
import re


class WikiMovieListSpider(scrapy.Spider):
    name = "wiki_movie_list"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Accused_(2005_film)",
        "https://en.wikipedia.org/wiki/Aaja_Nachle",
        "https://en.wikipedia.org/wiki/Aabhijathyam",
        "https://en.wikipedia.org/wiki/Zodiac_(film)",
        "https://en.wikipedia.org/wiki/Godfather_(1991_film)",
        "https://en.wikipedia.org/wiki/Avengers:_Endgame",
        "https://en.wikipedia.org/wiki/Citizen_Kane",
        "https://en.wikipedia.org/wiki/The_Godfather",
        "https://en.wikipedia.org/wiki/Pulp_Fiction",
        "https://en.wikipedia.org/wiki/Anatomy_of_a_Fall",
        "https://en.wikipedia.org/wiki/The_Wages_of_Fear",
        "https://en.wikipedia.org/wiki/Downpour_(film)",
    ]

    def parse(self, response):
        def clean_up(cur_list):
            superscript = re.compile("\[[0-9]+\]")
            new_list = []
            for w in cur_list:
                if (
                    (w == "\n")
                    or (".mw-parser-output" in w)
                    or (".plainlist" in w)
                    or (":" in w)
                    or superscript.match(w)
                ):
                    pass
                else:
                    new_list.append(w)
            return new_list

        def pick_dates(cur_list):
            date_format = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")
            location_format = re.compile("[a-zA-Z ].")
            new_list = []
            for w in cur_list:
                if date_format.match(w):
                    new_list.append(w)
                if location_format.match(w):
                    new_list.append(w)

        def currency_cleanup(cur_list):
            pass

        directors = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Directed by')]/following-sibling::td//text()"
            ).extract()
        )

        writers = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Screenplay by')]/following-sibling::td//text()"
            ).extract()
        )
        if not writers:
            writers = clean_up(
                response.xpath(
                    ".//th[contains(text(), 'Written by')]/following-sibling::td//text()"
                ).extract()
            )

        story_by = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Story by')]/following-sibling::td//text()"
            ).extract()
        )

        producers = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Produced by')]/following-sibling::td//text()"
            ).extract()
        )

        starring = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Starring')]/following-sibling::td//text()"
            ).extract()
        )

        cinematography = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Cinematography')]/following-sibling::td//text()"
            ).extract()
        )

        editors = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Edited by')]/following-sibling::td//text()"
            ).extract()
        )

        music_by = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Music by')]/following-sibling::td//text()"
            ).extract()
        )

        production_companies = clean_up(
            response.xpath(
                ".//div[contains(text(), 'Production')]/../following-sibling::td//text()"
            ).extract()
        )

        distributed_by = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Distributed by')]/following-sibling::td//text()"
            ).extract()
        )

        release_dates = clean_up(
            response.xpath(
                ".//div[contains(text(), 'Release date')]/../following-sibling::td//text()"
            ).extract()
        )

        running_time = clean_up(
            response.xpath(
                ".//div[contains(text(), 'Running time')]/../following-sibling::td//text()"
            ).extract()
        )

        countries = clean_up(
            response.xpath(
                ".//th[re:match(text(), 'Countr[yies]{0,3}')]//following-sibling::td//text()"
            ).extract()
        )

        languages = clean_up(
            response.xpath(
                ".//th[re:match(text(), 'Languages?')]//following-sibling::td//text()"
            ).extract()
        )

        budget = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Budget')]/following-sibling::td//text()"
            ).extract()
        )

        box_office = clean_up(
            response.xpath(
                ".//th[contains(text(), 'Box office')]/following-sibling::td//text()"
            ).extract()
        )

        imdb_link = clean_up(
            response.xpath(
                ".//a[contains(text(), 'IMDb')]/preceding-sibling::a/@href"
            ).extract()
        )

        yield {
            "directors": directors,
            "writers": writers,
            "story_by": story_by,
            "producers": producers,
            "starring": starring,
            "cinematography": cinematography,
            "editors": editors,
            "music_by": music_by,
            "production_companies": production_companies,
            "distributed_by": distributed_by,
            "release_dates": release_dates,
            "running_time": running_time,
            "countries": countries,
            "languages": languages,
            "budget": budget,
            "box_office": box_office,
            "imdb_link": imdb_link,
        }
