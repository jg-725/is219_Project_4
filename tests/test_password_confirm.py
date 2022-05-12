"""This test's password confirmation in the registration page """

def test_successful_register(successful_registration):
    assert successful_registration.email == 'jeff@email.com'
    assert successful_registration.password == 'Jeffrey'
    assert successful_registration.confirm == 'Jeffrey'
    response = successful_registration.get("/dashboard")
    assert response.status_code == 302
    assert b'Password is Confirmed' in response.data