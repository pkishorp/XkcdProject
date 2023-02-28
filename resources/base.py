"""
    This module dedicates for the resources which we implement in other module]
"""


class ResourceBase(object):
    """
        Base class representing required method to be implemented
        all the resource classes
    """


    def __init__(self) -> None:
        self.home_url = "https://xkcd.com"

    def get_title(self, comic_id):
        raise NotImplementedError

    def get_sample_data(self):
        raise NotImplementedError

    def get_image_url(self):
        raise NotImplementedError




