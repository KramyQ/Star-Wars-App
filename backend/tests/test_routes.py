def test_compute_odds_integration(client):
    response = client.post("/api/compute_odds", json={
  "countdown": 10,
  "bounty_hunters": [
    {"planet": "Hoth", "day": 6 },
    {"planet": "Hoth", "day": 7 },
    {"planet": "Hoth", "day": 8 }
  ]
})
    assert response.status_code == 200
    assert response is not None
    assert response.data == b'100'

def test_compute_odds_integration_wrong_format(client):
    response = client.post("/api/compute_odds", json={
  "countdown": 10,
  "bounty_hunters": [
    {"planet": "Hoth", "day": 6 },
    {"planet": "Hoth"},
    {"planet": "Hoth"}
  ]
})
    assert response.status_code == 400
    assert response is not None
    assert response.data == b'{\n  "message": [\n    "\'day\' is a required property"\n  ]\n}\n'

def test_compute_odds_integration_wrong_types(client):
    response = client.post("/api/compute_odds", json={
  "countdown": 10,
  "bounty_hunters": [
    {"planet": "Hoth", "day": 6 },
    {"planet": "Hoth", "day": "test" },
    {"planet": "Hoth", "day": 8 }
  ]
})
    assert response.status_code == 400
    assert response is not None
    assert response.data == b'{\n  "message": [\n    "\'test\' is not of type \'integer\'"\n  ]\n}\n'

def test_compute_odds_integration_empty_content(client):
    response = client.post("/api/compute_odds")
    assert response.status_code == 400
    assert response is not None
    assert response.data == b'{\n  "message": [\n    "None is not of type \'object\'"\n  ]\n}\n'

