import os
import time

# In-memory store of request timestamps per user
USER_LIMIT = {}

# Configurable limits via environment variables
# Defaults: 10 requests per 60 seconds
MAX_REQUESTS = int(os.getenv("RATE_LIMIT_MAX_REQUESTS", "10"))
WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", "60"))

def check_limit(user: str) -> bool:
    """Return True if the request is allowed; False if rate limit reached.

    - Keeps only timestamps within the current WINDOW
    - Allows request if count < MAX_REQUESTS and records the timestamp
    - Denies request if count >= MAX_REQUESTS
    """
    now = time.time()
    timestamps = USER_LIMIT.setdefault(user, [])

    # Keep only timestamps within the window
    timestamps = [t for t in timestamps if now - t < WINDOW]
    USER_LIMIT[user] = timestamps

    # If under limit, allow and record
    if len(timestamps) < MAX_REQUESTS:
        timestamps.append(now)
        USER_LIMIT[user] = timestamps
        return True

    # Limit reached
    return False