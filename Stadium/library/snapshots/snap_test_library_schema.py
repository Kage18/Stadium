# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['LibraryTestCase::test_list_games 1'] = {
    'data': {
        'games': [
            {
                'description': 'DummyDes.',
                'gameOwnedSet': [
                    {
                        'customer': {
                            'Customer': {
                                'username': 'dummy_user'
                            }
                        },
                        'id': '1'
                    }
                ],
                'id': '1',
                'name': 'Dummy',
                'price': 85.0,
                'tags': [
                    {
                        'tName': 'Dummy_tag'
                    }
                ]
            }
        ]
    }
}

snapshots['LibraryTestCase::test_list_tags 1'] = {
    'data': {
        'tags': [
            {
                'gameSet': [
                    {
                        'id': '1',
                        'name': 'Dummy'
                    }
                ],
                'id': '1',
                'tName': 'Dummy_tag'
            }
        ]
    }
}

snapshots['LibraryTestCase::test_gameowed 1'] = {
    'data': {
        'gameOwned': [
            {
                'customer': {
                    'Customer': {
                        'id': '1',
                        'username': 'dummy_user'
                    },
                    'id': '1'
                },
                'game': {
                    'id': '1',
                    'images': [
                    ],
                    'name': 'Dummy'
                },
                'hoursPlayed': 0,
                'rating': 0
            }
        ]
    }
}
