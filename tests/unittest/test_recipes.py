def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"One look is worth a thousand words." in response.data


def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/auth/login")
    assert response.status_code == 200
    assert b"Email" in response.data
    assert b"Password" in response.data
    assert b"Keep me logged in" in response.data


def test_valid_page(test_client):
    response = test_client.get("/post/5/Git")
    assert response.status_code == 200
    assert b"About InsideCode" in response.data
    assert b"Written by" in response.data


def test_valid_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post(
        "/auth/login",
        data=dict(email="test@flask.com", password="hello, world"),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Successfully logged in." in response.data
