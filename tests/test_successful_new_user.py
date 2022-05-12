"""This test's new user successfully registered """

def test_successful_register(create_user):
    assert create_user.email == 'bob@email.com'
    assert create_user.password == 'Marley'
    assert create_user.confirm == 'Marley'
    assert create_user.is_admin == '1'
    response = successful_registration.get("/dashboard")
    assert response.status_code == 302
    assert b'Congratulations, you just created a user' in response.data