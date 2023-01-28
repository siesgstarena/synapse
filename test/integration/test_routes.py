import os
from app import app

# pylint: disable=redefined-outer-name


# testing index route
def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


# testing admin route without login
def test_admin_route():
    client = app.test_client()
    response = client.get("/admin/")
    assert response.status_code == 403


# testing login route
def test_auth_login_route():
    client = app.test_client()
    response = client.get("/auth/login")
    assert response.status_code == 200


# testing logout route
def test_auth_logout_route():
    client = app.test_client()
    response = client.get("/auth/logout")
    assert response.status_code == 302


# testing login post route
def test_auth_login_post_route():
    client = app.test_client()
    response = client.post(
        "/auth/login",
        data=dict(username="admin", password="admin"),
        follow_redirects=True,
    )
    assert response.status_code == 200


# testing admin route with login with wrong credentials
with app.test_client() as client:
    client.post(
        "/auth/login",
        data=dict(username="test", password="test"),
        follow_redirects=True,
    )
    response = client.get("/admin/")
    assert response.status_code == 403

# testing admin route with login with correct credentials
with app.test_client() as client:
    client.post(
        "/auth/login",
        data=dict(
            username=os.environ.get("ADMIN_USERNAME"),
            password=os.environ.get("ADMIN_PASSWORD"),
        ),
        follow_redirects=True,
    )
    response = client.get("/admin/")
    assert response.status_code == 200


# testing /problem/training route POST request with wrong authorization token
def test_problem_training_route():
    client = app.test_client()
    response = client.post(
        "/problem/training",
        headers=dict(
            authorization="wrong_token",
        ),
        follow_redirects=True,
    )
    assert response.status_code == 401


# testing /problem/recommed route GET request with wrong authorization token
def test_problem_recommend_route():
    client = app.test_client()
    response = client.get(
        "/problem/recommend",
        headers=dict(
            authorization="wrong_token",
        ),
        follow_redirects=True,
    )
    assert response.status_code == 401


# testing /problem/training route GET with valid authorization token in header
def test_problem_training_route_valid():
    client = app.test_client()
    response = client.get(
        "/problem/recommend",
        headers={"Authorization": os.environ.get("ACCESS_TOKEN")},
        follow_redirects=True,
    )
    assert response.status_code == 200
