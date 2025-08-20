from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_all_provinsi():
    response = client.get("/api/v1/provinsi")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_provinsi_valid():
    response = client.get("/api/v1/provinsi/Jawa%20Barat")
    assert response.status_code == 200
    data = response.json()
    assert data["nama"] == "Jawa Barat"
    assert data["ibu_kota"] == "Bandung"

def test_get_provinsi_invalid():
    response = client.get("/api/v1/provinsi/Provinsi%20Tidak%20Ada")
    assert response.status_code == 404

def test_search_wilayah_valid():
    response = client.get("/api/v1/search?q=bandung")
    assert response.status_code == 200
    data = response.json()
    assert "query" in data
    assert "results" in data

def test_search_wilayah_empty():
    response = client.get("/api/v1/search?q=")
    assert response.status_code == 400

def test_get_statistics():
    response = client.get("/api/v1/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_provinsi" in data
    assert "total_kabupaten" in data
    assert "total_kota" in data
    assert "total_wilayah" in data

def test_get_random_provinsi():
    response = client.get("/api/v1/random")
    assert response.status_code == 200
    data = response.json()
    assert "nama" in data
    assert "ibu_kota" in data