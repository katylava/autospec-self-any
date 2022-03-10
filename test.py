from unittest import mock
from play import play


@mock.patch('play.Dog.add_trick', autospec=True)
def test_play(mock_trick):
    play()

    assert mock_trick.call_args == mock.call(mock.ANY, 'sit')
    mock_trick.assert_has_calls([mock.call(mock.ANY, 'sit')])


test_play()
