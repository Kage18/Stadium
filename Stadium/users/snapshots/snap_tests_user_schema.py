# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['LinkTestCase::test_create_link_user_anonymous 1'] = {
    'data': {
        'users': [
            {
                'email': '',
                'id': '1',
                'username': 'dummy_user'
            }
        ]
    }
}
