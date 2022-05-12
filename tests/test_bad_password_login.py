"""This tests bad password in Login page """

def test_login_password(bad_user):
    assert bad_user.email == 'jeff101@email.com'
    assert bad_user.password != 'Jeffrey'
    response = bad_user.get("/login")
    assert response.status_code == 300
    assert b'INVALID LOGIN PASSWORD!' in response.data