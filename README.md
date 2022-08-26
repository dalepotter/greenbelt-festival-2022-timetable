# greenbelt-festival-2022-timetable

The official Greenbelt app (available on [Apple](https://apps.apple.com/uk/app/greenbelt-festival/id1638195123) and [Android](https://play.google.com/store/apps/details?id=com.greenbeltfestivals.boma)) contains a variety of features - including the festival timetable.  It costs £4.99.

Personally, I object to the festival's Ryanair-like pricing strategy, where a plethra of additional/essential add-ons is offered after forking out the initial ticket price. Yes, lots of other festivals operate like this (to varying degrees), but it leaves a bad taste.

Instead, this repo extracts the data freely available via the [Greenbelt 2022 lineup page](https://www.greenbelt.org.uk/2022-lineup/) (and the artist pages contained within) which can be used in place of the paid app/paper programme.

NOTE: The official paid app will likely offer data in a more usable format, but this offers purely the timetable data in 'raw' format,  If you are comfortable using spreadsheets, you can use filters to find out which events are ongoing at any point in time.

## In a hurry

The 2022 timetable (correct at Friday 26 August 9am) is available:
- In [CSV (spreadsheet) format](https://github.com/dalepotter/greenbelt-festival-2022-timetable/raw/master/timetable.csv)
- As a [public Google sheet](https://docs.google.com/spreadsheets/d/1jUHMsrpruco1IJIwpW68lJyLOvZu-2v2oWlW5cddoUs/edit?usp=sharing)

## Generate your own (up-to-date) timetable

You'll need both python3 and the pip package manager installed to your computer.

```bash
# Clone this repo
git clone {TBC}

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the timetable generator
scrapy crawl greenbelt_festival_2022_lineup -o artists.csv
```
