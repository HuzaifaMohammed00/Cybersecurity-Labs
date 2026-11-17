# test parse_log_single
# test is_suspicious_request
# test count_segment_recursive
# test sanitize_log

from project1_log_sanitizer import (
    parse_log_single,
    is_suspicious_request,
    count_segments_recursive,
    sanitize_log,
)
import pytest


def test_parse_log():
    assert parse_log_single(" 192.168.1.10 | get | /home/index.html | 200 ") == {
        "ip": "192.168.1.10",
        "method": "GET",
        "endpoint": "/home/index.html",
        "status": 200,
    }


def test_is_suspicious_request():
    assert (
        is_suspicious_request(
            {
                "ip": "192.168.1.10",
                "method": "GET",
                "endpoint": "/home/index.html",
                "status": 200,
            }
        )
        == False
    )


def test_count_segments_recursive():
    assert count_segments_recursive(["api", "v1", "users", "profile"]) == 4
    assert count_segments_recursive([]) == 0


def test_sanitize_log():
    assert sanitize_log(
        {
            "ip": "192.168.1.10",
            "method": "GET",
            "endpoint": "/home/index.html/<script>",
            "status": 200,
        }
    ) == {
        "ip": "192.168.1.10",
        "method": "GET",
        "endpoint": "/home/index.html/[REDACTED]script[REDACTED]",
        "status": 200,
    }
