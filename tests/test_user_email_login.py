""" Testing bad user email login """

def test_user_email(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password, authenticated, and role fields are defined correctly
    """
    assert new_user.email != 'jeff1@gmail.com'
    assert new_user.password == 'Jeffrey'