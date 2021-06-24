import requests
import sys
import pytest

sys.path.insert(1,'')
import worker

def test_get_random_bytes(requests_mock):
    requests_mock.get('http://rng/32', status_code=200, text='data')
    assert worker.get_random_bytes() == requests.get('http://rng/32').content
    
def test_hash_bytes(requests_mock):
    requests_mock.post('http://hasher/', status_code=200, text='data')
    assert worker.hash_bytes('data') == requests.post('http://hasher/').text