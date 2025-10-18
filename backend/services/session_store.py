"""
Session store service using Redis.
"""

from core.redis_client import redis_client
import json


def store_session(session_id: str, summary_data: dict, ttl_seconds=1800):
    redis_client.setex(f"session:{session_id}", ttl_seconds, json.dumps(summary_data))

def load_session(session_id: str):
    data = redis_client.get(f"session:{session_id}")
    return json.loads(data) if data else None