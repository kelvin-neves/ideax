# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestDimensionForm.test_max_ptbr 1'] = {
    'description': [
        'Certifique-se de que o valor tenha no máximo 500 caracteres (ele possui 501).'
    ],
    'title': [
        'Certifique-se de que o valor tenha no máximo 200 caracteres (ele possui 201).'
    ]
}

snapshots['TestDimensionForm.test_invalid 1'] = {
    'description': [
        'This field is required.'
    ],
    'init_date': [
        'This field is required.'
    ],
    'title': [
        'This field is required.'
    ],
    'weight': [
        'This field is required.'
    ]
}

snapshots['TestDimensionForm.test_max 1'] = {
    'description': [
        'Ensure this value has at most 500 characters (it has 501).'
    ],
    'title': [
        'Ensure this value has at most 200 characters (it has 201).'
    ]
}
