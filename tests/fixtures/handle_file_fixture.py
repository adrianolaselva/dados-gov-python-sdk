import json

from tests import ROOT_DIR_TESTS


class HandleFileFixture(object):

    @staticmethod
    def load_raw_contents(path: str) -> str:
        with open(f"{ROOT_DIR_TESTS}/{path}") as content:
            return content.read()

    @staticmethod
    def load_json_contents(path: str) -> dict:
        return json.loads(HandleFileFixture.load_raw_contents(path))
