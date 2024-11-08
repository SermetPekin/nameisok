from nameisok.core import get_check_url, eval_req, show_status_console, get_status_package_cli


def test_get_url():
    url: str = get_check_url('pandas')
    assert url

    assert url.endswith('/')


def test_eval_req():
    s = eval_req(200, 200)
    assert s.success


def test_show_status_console(capsys):
    with capsys.disabled():
        show_status_console('test', False)


def test_get_status_package_cli(capsys):
    with capsys.disabled():
        r = get_status_package_cli('pandas,example', lambda x: print(x))
        assert r is None
