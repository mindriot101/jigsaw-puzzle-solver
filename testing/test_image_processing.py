import pytest
import sys
import cv2

sys.path.append(".")
from side_extractor import process_piece


@pytest.fixture(scope="session")
def filename():
    return "testing/fixtures/IMG_20180415_211104234.jpg"


def test_process_image(snapshot, filename):
    img = cv2.imread(filename)
    out = process_piece(img)

    snapshot.assert_match(out)
