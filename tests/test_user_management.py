"""This test the dashboard page for user management"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_user_mgmt_pages(client):
    """This makes the user mgmt page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/edit_profile")
    assert response.status_code == 302
    response = client.get("/edit_account")
    assert response.status_code == 302
    response = client.get("/browse_users")
    assert response.status_code == 302