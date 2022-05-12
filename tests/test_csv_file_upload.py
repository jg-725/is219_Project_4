""" Tests csv upload form """

def test_csv_form(upload_csv_file):
    assert upload_csv_file.filename == 'sample.csv'
    assert upload_csv_file.filepath == 'UPLOAD_FOLDER'
    response = new_user.get("/dashboard")
    assert response.status_code == 302