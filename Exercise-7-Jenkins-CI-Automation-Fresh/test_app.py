from app import welcome

def test_welcome():
    assert welcome("Developer") == "Welcome to Jenkins CI, Developer!"

def test_welcome_with_another_name():
    assert welcome("Srujana") == "Welcome to Jenkins CI, Srujana!"
