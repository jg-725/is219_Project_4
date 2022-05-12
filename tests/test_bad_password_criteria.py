"""This test's if password does not meet criteria in registration page """

def test_password_criteria(bad_user):
    assert bad_user.email == 'jeff101@email.com'
    assert bad_user.password != 'Jeffrey'
    response = bad_user.get("/register")
    assert response.status_code == 300
    assert b'This password DOES NOT meet the criteria!' in response.data