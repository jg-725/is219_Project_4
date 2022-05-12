""" Tests bad csv upload file """

def test_bad_csv_filename(bad_upload_csv_file):
    assert bad_upload_csv_file.filename == 'sample1.csv'
    assert bad_upload_csv_file.filepath == 'UPLOAD_FOLDER'
    response = bad_upload_csv_file.get("/home")
    assert response.status_code == 302