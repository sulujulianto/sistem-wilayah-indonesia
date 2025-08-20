import pytest
from app.services.wilayah_service import WilayahService

@pytest.fixture
def wilayah_service():
    return WilayahService()

def test_cari_provinsi_valid(wilayah_service):
    result = wilayah_service.cari_provinsi("Jawa Barat")
    assert result is not None
    assert result["nama"] == "Jawa Barat"
    assert result["ibu_kota"] == "Bandung"

def test_cari_provinsi_invalid(wilayah_service):
    result = wilayah_service.cari_provinsi("Provinsi Tidak Ada")
    assert result is None

def test_cari_provinsi_alias(wilayah_service):
    result = wilayah_service.cari_provinsi("jabar")
    assert result is not None
    assert result["nama"] == "Jawa Barat"

def test_cari_kabupaten_kota_valid(wilayah_service):
    result = wilayah_service.cari_kabupaten_kota("bandung")
    assert result is not None
    assert len(result) > 0

def test_cari_kabupaten_kota_invalid(wilayah_service):
    result = wilayah_service.cari_kabupaten_kota("xyz123")
    # Bisa jadi None atau list kosong
    assert result is None or len(result) == 0

def test_dapatkan_statistik(wilayah_service):
    stats = wilayah_service.dapatkan_statistik()
    assert "total_provinsi" in stats
    assert "total_kabupaten" in stats
    assert "total_kota" in stats
    assert "total_wilayah" in stats
    assert stats["total_provinsi"] > 0

def test_dapatkan_provinsi_acak(wilayah_service):
    result = wilayah_service.dapatkan_provinsi_acak()
    assert result is not None
    assert "nama" in result
    assert "ibu_kota" in result

def test_dapatkan_semua_provinsi(wilayah_service):
    result = wilayah_service.dapatkan_semua_provinsi()
    assert isinstance(result, list)
    assert len(result) > 0