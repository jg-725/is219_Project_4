"""This test's if user is already registered """

def test_duplicate_register(new_user):
    assert new_user.email == 'jeff@email.com'
    assert new_user.password == 'Jeffrey'
    response = new_user.get("/login")
    assert response.status_code == 300
    assert b'This User is ALREADY registered!' in response.data