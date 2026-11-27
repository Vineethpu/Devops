from app import add,app

#unit test:checks one small function

def test_add():
    assert add(2,3) == 5 #false if fails
    
#route rest :flask's test client simulates a browser
def test_home_route():
    client = app.test_client() #testing client
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, DevOps Team -CI CD 2026!" in response.data

def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] =="ok"