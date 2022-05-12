"""This test's if user successfully registered """

def test_successful_register(successful_registration):
    assert successful_registration.email == 'jeff@email.com'
    assert successful_registration.password == 'Jeffrey'
    assert successful_registration.confirm == 'Jeffrey'
    response = successful_registration.get("/dashboard")
    assert response.status_code == 302
    assert b'Congrats, registration success' in response.data