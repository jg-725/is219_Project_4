"""This test's if user successfully logged in """


def test_successful_login(new_user):
    assert new_user.email == 'jeff@email.com'
    assert new_user.password == 'Jeffrey'
    response = new_user.get("/dashboard")
    assert response.status_code == 302