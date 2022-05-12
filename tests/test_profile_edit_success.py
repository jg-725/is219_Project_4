''' Tests the profile edit form success'''


def test_profile_edit_form(profile_edit):
    assert profile_edit.about == 'Hello, this is my profile!'
    response = profile_edit.get("/browse_users")
    assert response.status_code == 302
    assert b'Please add information about yourself' in response.data