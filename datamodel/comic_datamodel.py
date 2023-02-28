from pydantic import BaseModel
from pprint import pprint


class Comics(BaseModel):

    month: str
    num: str
    link: str
    year: str
    news: str
    safe_title: str
    transcript: str
    alt: str
    img: str
    title: str
    day: str


if __name__ == "__name__":

    external = {"month": "2",
                "num": 2743, "link": "",
                "year": "2023",
                "news": "",
                "safe_title": "Hand Dryers",
                "transcript": "",
                "alt": "I know hand dryers have their problems, but I think for fun we should keep egging Dyson on "
                       "and see if we can get them to make one where"
                       "the airflow breaks the speed of sound.",
                "img": "https://imgs.xkcd.com/comics/hand_dryers.png",
                "title": "Hand Dryers",
                "day": "27"

    }

    obj = Comics(**external)

    pprint(obj)
