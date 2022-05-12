""" Testing homepage header textdata"""

def test_request_example(client):
    response = client.get("/home")
    assert b"<h1 class=text-center>Home</h1>" in response.data