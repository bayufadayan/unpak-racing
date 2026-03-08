#!/usr/bin/env bash
# Wrapper to activate project's .venv (POSIX shells)
if [ -f ".venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  . ".venv/bin/activate"
elif [ -f ".venv/Scripts/activate" ]; then
  . ".venv/Scripts/activate"
else
  echo "Virtual environment not found: .venv"
  return 1 2>/dev/null || exit 1
fi
