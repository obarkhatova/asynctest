import pytest

from src.script import check_params, str_to_sha256

template = {'name': 'test_name',
            'vacancy': 'vacancy_val',
            'salary': 10,
            'delay': 0.1,
            'count': 5,
            }


@pytest.mark.parametrize('data, key_missing',
                         [
                             (
                                {'vacancy': 'vacancy_val',
                                 'salary': 10,
                                 'delay': 0.1,
                                 'count': 5,
                                 },
                                'name',
                             ),
                             (
                                {'name': 'test_name',
                                 'salary': 10,
                                 'delay': 0.1,
                                 'count': 5,
                                 },
                                'vacancy',
                             ),
                             (
                                {'name': 'test_name',
                                 'vacancy': 'vacancy_val',
                                 'delay': 0.1,
                                 'count': 5,
                                 },
                                'salary',
                             ),
                             (
                                {'name': 'test_name',
                                 'vacancy': 'vacancy_val',
                                 'salary': 10,
                                 'count': 5,
                                 },
                                'delay',
                             ),
                             (
                                {'name': 'test_name',
                                 'vacancy': 'vacancy_val',
                                 'salary': 10,
                                 'delay': 0.1,
                                 },
                                'count',
                             )]
                         )
def test_check_params_missing(data, key_missing):
    with pytest.raises(ValueError) as excinfo:
        check_params(**data)
    assert f'{key_missing} is missing' in str(excinfo.value)


@pytest.mark.parametrize('data',
                         [{'name': 'test_name',
                           'vacancy': 'vacancy_val',
                           'salary': 10,
                           'delay': 0.1,
                           'count': 51,
                           }]
                         )
def test_check_params_count_overflow(data):
    with pytest.raises(ValueError) as excinfo:
        check_params(**data)
    assert f'Count greater than 50' in str(excinfo.value)


@pytest.mark.parametrize('data',
                         [(
                            {'name': 'test_name',
                             'vacancy': 'vacancy_val',
                             'salary': 10,
                             'delay': 10.01,
                             'count': 50,
                             }
                         )]
                         )
def test_check_params_delay_overflow(data):
    with pytest.raises(ValueError) as excinfo:
        check_params(**data)
    assert f'Delay greater than 10' in str(excinfo.value)


@pytest.mark.parametrize('data',
                         [
                            {'name': 'test_name',
                             'vacancy': 'vacancy_val',
                             'salary': 10,
                             'delay': 10,
                             'count': 50,
                             },
                            {'name': '',
                             'vacancy': '',
                             'salary': 0,
                             'delay': 9.99,
                             'count': 50,
                            }
                         ]
                         )
def test_check_params_positive(data):
    assert check_params(**data) is None


@pytest.mark.parametrize('data, expected',
                         [
                             ('', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca'
                                  '495991b7852b855'),
                             ('123qwert!#$', '45656e0e9a6440e624e4f98aec10d6a7137f2d2'
                                             '95b0d6d6ce3d9e4db7d423902'),
                         ]
                         )
def test_str_to_sha256(data, expected):
    assert str_to_sha256(data) == expected

