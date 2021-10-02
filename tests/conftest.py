import pytest
from manage import app
from app.models import User, Role


@pytest.fixture(scope="module")
def new_user():
    role = Role.query.filter_by(permissions=0x1).first()
    user = User(
        email="test@flask.com",
        username="tester",
        password="hello, world",
        role=role,
        confirmed=True,
    )
    return user


@pytest.fixture(scope="module")
def test_client():
    app.testing = True
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
