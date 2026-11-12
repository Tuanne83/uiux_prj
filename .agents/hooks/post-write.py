#!/usr/bin/env python3
"""Antigravity PostToolUse adapter for BA-Kit documentation lifecycle hooks."""

import json
import os
import subprocess
import sys


def main() -> None:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        payload = {}

    tool_call = payload.get("toolCall") or {}
    args = tool_call.get("args") or {}
    file_path = args.get("Path") or args.get("path") or ""

    default_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    cwd = payload.get("cwd") or default_root

    if file_path:
        env = os.environ.copy()
        env["PROJECT_PATH"] = cwd
        env.setdefault("AUTO_CHANGELOG", "true")

        for hook_name in (
            "auto-changelog.sh",
            "status-transition.sh",
            "post-edit-stale.sh",
            "kg-refresh.sh",
        ):
            hook_path = os.path.join(cwd, ".claude", "hooks", hook_name)
            if os.path.isfile(hook_path):
                subprocess.run(
                    [hook_path, file_path],
                    cwd=cwd,
                    env=env,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False,
                )

    print("{}")


if __name__ == "__main__":
    main()

