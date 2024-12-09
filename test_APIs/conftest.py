import pytest
import requests

@pytest.fixture
def get_session():      #session/會話
    session = requests.session()
    yield session
    session.close() 