"""
Module to create and manage a Redis client for the application.
"""

import redis
import os
from dotenv import load_dotenv
from pathlib import Path

# Load the .env file from the project root
env_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path=env_path)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Create a Redis client once
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),  # use "redis" when in Docker
    port=6379,
    decode_responses=True  # get strings instead of bytes
)