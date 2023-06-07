from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("vasco", 25) == "ocsav"
    assert encrypt_message("vasco", 2) == "ocs_av"
    assert encrypt_message("vasco", 3) == "sav_oc"

    with pytest.raises(TypeError):
        encrypt_message("vasco", "gigante")