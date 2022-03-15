"""Tests standard target features using the built-in SDK tests library."""

import datetime
import os
from typing import Dict, Any

from singer_sdk.testing import get_standard_target_tests

from target_oracle import OracleConnector, TargetOracle


SAMPLE_CONFIG: Dict[str, Any] = {
    'username': os.environ.get('ORACLE_TARGET_USERNAME'),
    'password': os.environ.get('ORACLE_TARGET_PASSWORD'),
    'drivername': os.environ.get('ORACLE_TARGET_DRIVERNAME'),
    'host': os.environ.get('ORACLE_TARGET_HOST'),
    'port': os.environ.get('ORACLE_TARGET_PORT'),
    'database': os.environ.get('ORACLE_TARGET_DATABASE'),
}


# Run standard built-in target tests from the SDK:
def test_standard_target_tests():
    """Run standard target tests from the SDK."""
    tests = get_standard_target_tests(
        TargetOracle,
        config=SAMPLE_CONFIG,
    )
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your target.

def test_connection():
    cnxn = OracleConnector(config=SAMPLE_CONFIG)
    result = cnxn.connection.execute('SELECT 1 from dual')
    assert result.one()[0] == 1