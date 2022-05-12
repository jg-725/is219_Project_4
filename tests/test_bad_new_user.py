"""This test's bad new user """

def test_successful_register(create_user):
    assert create_user.email != 'bob123@email.com'
    assert create_user.is_admin == '1'
    response = successful_registration.get("/browse_users")
    assert response.status_code == 302
    assert b'THIS USER IS ALREADY REGISTERED' in response.data