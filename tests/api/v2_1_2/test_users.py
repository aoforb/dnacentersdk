# -*- coding: utf-8 -*-
"""DNACenterAPI users API fixtures and tests.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pytest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.2', reason='version does not match')


def is_valid_get_user_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_d7a6392845e8969d_v2_1_2').validate(obj)
    return True


def get_user_enrichment_details(api):
    endpoint_result = api.users.get_user_enrichment_details(

    )
    return endpoint_result


@pytest.mark.users
def test_get_user_enrichment_details(api, validator):
    assert is_valid_get_user_enrichment_details(
        validator,
        get_user_enrichment_details(api)
    )


def get_user_enrichment_details_default(api):
    endpoint_result = api.users.get_user_enrichment_details(

    )
    return endpoint_result


@pytest.mark.users
def test_get_user_enrichment_details_default(api, validator):
    try:
        assert is_valid_get_user_enrichment_details(
            validator,
            get_user_enrichment_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e
