from mlproject.distance import haversine

def test_distance():
    assert haversine(lon1, lat1, lon2, lat2).dtype == "int"
    
