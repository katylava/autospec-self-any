from unittest import mock
from play import get_dog, play


@mock.patch('play.Dog.add_trick', autospec=True)
def test_play(mock_trick):
    dog = get_dog()
    play(dog)

    assert mock_trick.call_args == mock.call(mock.ANY, 'sit')
    mock_trick.assert_has_calls([mock.call(mock.ANY, 'sit')])


test_play()
