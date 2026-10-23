from app import get_status

def test_application_status():
    assert get_status() == "Application is ready"
