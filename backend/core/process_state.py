"""
Module to manage the state of a long-running process, such as training or validation.
"""

from threading import Lock
from typing import Optional

class ProcessState:
    def __init__(self):
        self._lock = Lock()
        self._in_progress = False
        self._error: Optional[str] = None
        self._chunks: Optional[list] = None

    def start(self) -> bool:
        with self._lock:
            if self._in_progress:
                return False
            self._in_progress = True
            self._error = None
            self._chunks = None
            return True

    def finish(self, error: Optional[str] = None, chunks: Optional[list] = None):
        with self._lock:
            self._in_progress = False
            self._error = error
            self._chunks = chunks

    def reset(self):
        with self._lock:
            self._in_progress = False
            self._error = None
            self._chunks = None

    def get_status(self) -> dict:
        with self._lock:
            return {
                "in_progress": self._in_progress,
                "error": self._error,
                "chunks": self._chunks,
            }

    def is_busy(self) -> bool:
        with self._lock:
            return self._in_progress