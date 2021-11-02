from app.models import Permission


def test_new_user(new_user):
    assert new_user.email == "test@flask.com"
    assert new_user.username == "tester"
    assert new_user.can(Permission.COMMENT) == True
    assert new_user.can(Permission.WRITE_ARTICLES) == False
