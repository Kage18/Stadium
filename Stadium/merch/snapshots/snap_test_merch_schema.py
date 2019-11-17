# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['MerchTestCase::test_list_merch 1'] = {
    'data': {
        'merchs': [
            {
                'desc': 'Dummy_desc',
                'id': '1',
                'images': [
                ],
                'name': 'Dummy_name'
            }
        ]
    }
}

snapshots['MerchTestCase::test_merchowned 1'] = {
    'data': {
        'merchs': [
            {
                'desc': 'Dummy_desc',
                'id': '1',
                'merchuserSet': [
                    {
                        'id': '1',
                        'user': {
                            'Customer': {
                                'username': 'dummy_user'
                            }
                        }
                    }
                ],
                'name': 'Dummy_name'
            }
        ]
    }
}
