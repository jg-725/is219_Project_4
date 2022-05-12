""" Tests the security form success """


def test_security_edit_success(security_user):
    assert security_user.email == 'john@email.com'
    assert security_user.password == 'Lennon'
    assert security_user.confirm == 'Lennon'
    response = security_user.get("/browse_users")
    assert response.status_code == 302
    assert b'You Successfully Updated your Password or Email' in response.data