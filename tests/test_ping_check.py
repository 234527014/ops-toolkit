import subprocess
import sys

import ping_check


def set_argv(monkeypatch, hosts_file, log_file):
    monkeypatch.setattr(
        sys, "argv",
        ["ping_check.py", "--file", str(hosts_file), "--log", str(log_file)],
    )


def test_read_hosts_skips_blank_lines_and_strips(tmp_path):
    f = tmp_path / "hosts.txt"
    f.write_text("  8.8.8.8  \n\n127.0.0.1\n   \n")
    assert ping_check.read_hosts(f) == ["8.8.8.8", "127.0.0.1"]


def test_check_host_returns_true_when_ping_succeeds(monkeypatch):
    monkeypatch.setattr(
        subprocess, "run", lambda cmd, **kw: subprocess.CompletedProcess(cmd, 0)
    )
    assert ping_check.check_host("127.0.0.1", 1, 1) is True


def test_check_host_returns_false_when_ping_fails(monkeypatch):
    monkeypatch.setattr(
        subprocess, "run", lambda cmd, **kw: subprocess.CompletedProcess(cmd, 1)
    )
    assert ping_check.check_host("10.255.255.1", 1, 1) is False


def test_check_host_builds_expected_command(monkeypatch):
    seen = {}

    def fake_run(cmd, **kw):
        seen["cmd"] = cmd
        return subprocess.CompletedProcess(cmd, 0)

    monkeypatch.setattr(subprocess, "run", fake_run)
    ping_check.check_host("1.2.3.4", 3, 5)
    assert seen["cmd"] == ["ping", "-c", "3", "-W", "5", "1.2.3.4"]


def test_main_returns_2_when_hosts_file_missing(monkeypatch, tmp_path):
    set_argv(monkeypatch, tmp_path / "nope.txt", tmp_path / "t.log")
    assert ping_check.main() == 2


def test_main_returns_0_when_all_hosts_up(monkeypatch, tmp_path):
    hosts = tmp_path / "hosts.txt"
    hosts.write_text("a\nb\n")
    monkeypatch.setattr(ping_check, "check_host", lambda h, c, t: True)
    set_argv(monkeypatch, hosts, tmp_path / "t.log")
    assert ping_check.main() == 0


def test_main_returns_1_when_some_host_down(monkeypatch, tmp_path):
    hosts = tmp_path / "hosts.txt"
    hosts.write_text("a\nb\n")
    monkeypatch.setattr(ping_check, "check_host", lambda h, c, t: h != "b")
    set_argv(monkeypatch, hosts, tmp_path / "t.log")
    assert ping_check.main() == 1