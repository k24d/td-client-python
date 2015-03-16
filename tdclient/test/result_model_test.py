#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

try:
    from unittest import mock
except ImportError:
    import mock

from tdclient import model
from tdclient.test.test_helper import *

def setup_function(function):
    unset_environ()

def test_result():
    client = mock.MagicMock()
    result = model.Result(client, "name", "url", "org_name")
    assert result.name == "name"
    assert result.url == "url"
    assert result.org_name == "org_name"
