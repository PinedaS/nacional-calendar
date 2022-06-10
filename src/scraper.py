from statistics import harmonic_mean
import requests
import lxml.html as html

HOME_URL = "https://www.atlnacional.com.co/"

XPATH_DATE_AND_TIME_FOOTBALL_MATCH = "//div[@class='jet-listing-dynamic-repeater__item'][1]/div/div/div[2]/span"
XPATH_TEAM1 = "//div[@class='jet-listing-dynamic-repeater__item'][1]/div/div/div[1]/div[1]/h3"
XPATH_TEAM2 = "//div[@class='jet-listing-dynamic-repeater__item'][1]/div/div/div[1]/div[2]/h3"


def parse_info():
    try:
        response = requests.get(HOME_URL)

        if response.status_code == 200:
            info = response.content.decode("utf-8")
            parsed = html.fromstring(info)

            date_football_match = parsed.xpath(
                XPATH_DATE_AND_TIME_FOOTBALL_MATCH)[0].text
            time_football_match = parsed.xpath(
                XPATH_DATE_AND_TIME_FOOTBALL_MATCH)[1].text
            team1 = parsed.xpath(XPATH_TEAM1)[0].text
            team2 = parsed.xpath(XPATH_TEAM2)[0].text

            return [date_football_match, time_football_match, team1, team2]

        else:
            raise ValueError("Error: " + response.status_code)

    except ValueError as ve:
        print(ve)


def run():
    return parse_info()


if __name__ == '__main__':
    run()
