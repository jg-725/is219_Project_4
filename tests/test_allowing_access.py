"""This tests allowing access to logged in users """

def test_access(new_user):
    assert new_user.email == 'jeff@email.com'
    assert new_user.password == 'Jeffrey'
    response = new_user.get("/dashboard")
    assert response.status_code == 302