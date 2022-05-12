""" Tests the security form password failure """


def test_security_edit_success(security_user):
    assert security_user.email == 'john@email.com'
    assert security_user.password == 'Lennon'
    assert security_user.confirm != 'Harrison'
    response = security_user.get("/browse_users")
    assert response.status_code == 302
    assert b'Passwords must match' in response.data