"""
In this module we are fetching the data from xkcd.com for each comic
In this module we also can fetch data for any 10 comics random resource urls by default
User will also use this as a CLI
"""

import argparse
from pprint import pprint
# pydantic model
from datamodel.comic_datamodel import Comics
# resources model
from resources.r_comics import ResourceComics
from utils.timing import timeit
from utils.fetch_data import hit_url
from utils.randgen import ProduceNumbers
from task_one import get_url


def comic():
    """

    :return: comic_data, comic_url, comic_title of passed comic_id
    """

    comic_obj = ResourceComics()
    comic_title = comic_obj.get_title()
    print("Comic title is::", comic_title)

    comic_data = comic_obj.get_sample_data()
    comic_data = Comics(**comic_data)
    print("Comic data is ::", comic_data)

    image_url = comic_obj.get_image_url()
    print("Comic image url::", image_url)


def random_data():
    """
        Generates the data of any 10 comic_id's by default.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end",type=int, default=100)
    parser.add_argument("-l", "--limit", type=int, default=10)
    argument = parser.parse_args()
    print(f"Passed argument :: {argument}")
    obj = ProduceNumbers(argument.start, argument.end, argument.limit)
    comics = [element for element in obj]
    print(f"Generating the data for `comic_id`::\n {comics}")

    for comic_id in comics:
        print(f"[INFO] Generating the data of comic_id:-{comic_id}")
        url = get_url(comic_id)
        response = hit_url(url)
        data = response.json()
        pprint(data)


if __name__ == "__main__":
    comic()
    random_data()



