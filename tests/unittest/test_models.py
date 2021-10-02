from app.models import Permission


def test_new_user(new_user):
    assert new_user.email == "test@flask.com"
    assert new_user.username == "tester"
    assert new_user.can(Permission.COMMENT) == True
    assert new_user.can(Permission.WRITE_ARTICLES) == False


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"One look is worth a thousand words." in response.data
