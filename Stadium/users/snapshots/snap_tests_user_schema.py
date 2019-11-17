# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['UserTestCase::test_create_user 1'] = {
    'data': {
        'createUser': {
            'user': {
                'username': 'kushal'
            }
        }
    }
}

snapshots['UserTestCase::test_customerprofile 1'] = {
    'data': {
        'customer': [
            {
                'Customer': {
                    'username': 'dummy_user'
                },
                'DOB': '1999-03-18',
                'avatar': None,
                'bio': None,
                'gender': 1,
                'id': '1',
                'joined': '2019-11-17',
                'phoneNo': '9340143387'
            }
        ]
    }
}

snapshots['UserTestCase::test_user 1'] = {
    'data': {
        'users': [
            {
                'cus': {
                    'DOB': '1999-03-18',
                    'gender': 1,
                    'joined': '2019-11-17',
                    'phoneNo': '9340143387'
                },
                'email': '',
                'id': '1',
                'isVerified': False,
                'username': 'dummy_user'
            }
        ]
    }
}
