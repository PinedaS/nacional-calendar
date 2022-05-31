from statistics import harmonic_mean
import requests
import lxml.html as html

HOME_URL = "https://www.atlnacional.com.co/"

XPATH_LINK_TO_FOOTBALL_MATCH = "//div[@class='contenedor-partido']/ul/li[2]/a/@href"
XPATH_DATE_FOOTBALL_MATCH = "//div[@class='info-partido-actual inline-elements']/p[3]"
XPATH_TEAM1 = "//div[@class='equipo-left']/div[1]/p[1]/text()"
XPATH_TEAM2 = "//div[@class='equipo-right']/div[1]/p[1]/text()"


def parse_home():
    try:
        response = requests.get(HOME_URL)

        if response.status_code == 200:
            home = response.content.decode("utf-8")
            parsed = html.fromstring(home)
            link_to_football_match = parsed.xpath(
                XPATH_LINK_TO_FOOTBALL_MATCH)[0]

            return link_to_football_match
        else:
            raise ValueError("Error: " + response.status_code)

    except ValueError as ve:
        print(ve)


def parse_info(link_to_football_match):
    try:
        response = requests.get(link_to_football_match)

        if response.status_code == 200:
            info = response.content.decode("utf-8")
            parsed = html.fromstring(info)

            date_football_match = parsed.xpath(
                XPATH_DATE_FOOTBALL_MATCH)[0].text
            team1 = parsed.xpath(XPATH_TEAM1)[0]
            team2 = parsed.xpath(XPATH_TEAM2)[0]

            return [date_football_match, team1, team2]

        else:
            raise ValueError("Error: " + response.status_code)

    except ValueError as ve:
        print(ve)


def run():
    link_to_football_match = parse_home()

    return parse_info(link_to_football_match)


if __name__ == '__main__':
    run()
