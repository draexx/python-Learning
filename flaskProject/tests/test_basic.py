import pytest

def test_index_route_get(client):
    """
    Test that the index route ('/') returns a 200 OK status code for a GET request.
    """
    response = client.get('/')
    assert response.status_code == 200
    # You can also check for content in the response
    # assert b"Welcome" in response.data # Example: if your index page has "Welcome"

def test_login_route_get(client):
    """
    Test that the login route ('/login') returns a 200 OK status code for a GET request.
    """
    response = client.get('/login') # Assuming you have a /login route
    assert response.status_code == 200
    # assert b"Login Page" in response.data # Example content check

# Add more basic tests here, for example:
# - Test that other important GET routes load correctly.
# - Test redirection if applicable (e.g., accessing a protected page without login).

# Example for a route that might not exist, to show how a 404 might be tested
# def test_non_existent_route(client):
#     response = client.get('/this-route-does-not-exist')
#     assert response.status_code == 404
