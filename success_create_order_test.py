import sender_stand_requests

# Ирина Полеводина, 23-я когорта — Финальный проект. Инженер по тестированию плюс
def test_success_create_order():
    track = sender_stand_requests.create_order_and_get_track()

    assert track != ""

    order_response = sender_stand_requests.get_order_by_id(track)

    assert order_response.status_code == 200