import urllib3

def test_homepage():
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/')
    assert 200  == r.status

def test_activities():
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/Activities')
    assert 200  == r.status

def test_location():
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/Locations')
    assert 200  == r.status

def test_nonpage():
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/About')
    assert 404  == r.status
