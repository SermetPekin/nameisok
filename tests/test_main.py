from nameisok.core import get_check_url, eval_req, get_status_package_cli, show_status_console_available, \
    show_status_console_taken


def test_get_url():
    url: str = get_check_url('pandas')
    assert url

    assert url.endswith('/')


def test_eval_req():
    s = eval_req(200, 200)
    assert s.exists


def test_show_status_console(capsys):
    with capsys.disabled():
        show_status_console_available('test')
        show_status_console_taken('test')


def test_get_status_package_cli(capsys):
    with capsys.disabled():
        r = get_status_package_cli('pandas,example', lambda x: print(x))
        assert tuple(r ) == ( None , None )


def test_real_get_status_package_cli(capsys):
    with capsys.disabled():
        r = get_status_package_cli('pandas')
        assert r is False
        r = get_status_package_cli('pandas_12345678')
        assert r is True
