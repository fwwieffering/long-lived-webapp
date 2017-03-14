from hypothesis import given, example
import hypothesis.strategies as st
import requests
import pep8
import os


def test_universe():
    assert True


def test_pep8_compliance():
    assert len(pep8.StyleGuide()
               .check_files(filter(lambda x: x.endswith('.py'),
                            os.listdir('.')))
               .get_statistics()) == 0


@given(x=st.integers())
@example(-1)
def test_abs(x: int) -> None:
    assert abs(x) >= 0


def test_up():
    assert requests.get('http://localhost:5050/up').json() == \
        {'status': 'happy'}
