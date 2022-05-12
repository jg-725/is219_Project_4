"""This tests denying access to users NOT logged in """

def test_deny_access(bad_user):
    assert bad_user.email == 'jeff101@email.com'
    assert bad_user.password != 'Jeffrey'
    response = bad_user.get("/")
    assert response.status_code == 302