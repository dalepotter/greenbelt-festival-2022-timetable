import re
import scrapy
from datetime import datetime, timedelta


class LineupSpider(scrapy.Spider):
    """Crawls the Greenbelt Festival 2024 lineup to extract artist appearance data."""
    name = "greenbelt_festival_2024_lineup"
    start_urls = ["https://www.greenbelt.org.uk/2024-lineup/"]

    def parse(self, response):
        self.logger.info("Starting Greenbelt 2024 timetable spider")
        all_artists = response.css("ul.listing").css("li")
        for artist in all_artists:
            artist_data = {
                "artist_name": artist.xpath("string(a)").get(),
                "href": artist.xpath("a/@href").get(),
                "tags": artist.xpath("@class").get(),
                "tags_set": set(artist.xpath("@class").get().strip().split(" "))
            }
            yield response.follow(
                artist_data["href"],
                callback=self.parse_artist,
                cb_kwargs={'artist_data': artist_data}
            )

    def parse_artist(self, response, artist_data):
        self.logger.info(f"Extracting data for artist: {artist_data['artist_name']}")
        all_events = response.xpath("//aside[contains(@class, 'shows')]")
        for event in all_events:
            # Extract date and time
            event_day_time_elem = event.xpath("h3/br[1]/following-sibling::text()[1]")
            if "Friday" in event_day_time_elem.get():
                base_date = datetime(2024, 8, 23)
            elif "Saturday" in event_day_time_elem.get():
                base_date = datetime(2024, 8, 24)
            elif "Sunday" in event_day_time_elem.get():
                base_date = datetime(2024, 8, 25)
            event_day_time_elem.re("\d\d:\d\d")[0]
            event_time = re.search(r"(?P<hours>\d\d):(?P<mins>\d\d)", event_day_time_elem.get())
            event_datetime = base_date + timedelta(
                hours=int(event_time.group("hours")),
                minutes=int(event_time.group("mins"))
            )

            yield {
                "artist_name": artist_data["artist_name"],
                "event_location": event.xpath("h3/br[1]/preceding-sibling::text()[1]").get(),
                "event_title": event.xpath("string(h4)").get(),
                "event_day": event_datetime.strftime("%A"),
                "event_start_time": event_datetime.strftime("%H:%M"),
                "event_summary": event.xpath("string(p)").get(),
                "source_url": response.url
            }
