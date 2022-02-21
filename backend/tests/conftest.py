import pytest
import os, sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from onboard_computer_api import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app



@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def create_valid_compute_odds_request():
    """
    Helper function for creating a correctly-structured
    json request
    """
    def _create_valid_compute_odds_request(compute_odds="fixture"):
        return {
            "compute_odds": compute_odds
        }
    return _create_valid_compute_odds_request