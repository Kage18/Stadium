# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['UserTestCase::test_customerprofile 1'] = {
    'data': {
        'customer': [
            {
                'Customer': {
                    'username': 'dummy_user'
                },
                'DOB': '1999-03-18',
                'avatar': [
                ],
                'bio': None,
                'gender': 1,
                'id': '1',
                'joined': '2019-12-21',
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
                    'joined': '2019-12-21',
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
