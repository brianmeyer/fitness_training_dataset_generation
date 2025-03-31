"""
Rate limiting utilities for API calls.
"""

import time
import threading
from datetime import datetime, timedelta

# Rate limiting settings
RPM_LIMIT = 30  # requests per minute
RPD_LIMIT = 1000  # requests per day
TPM_LIMIT = 6000  # tokens per minute

class RateLimiter:
    def __init__(self):
        self.rpm_lock = threading.Lock()
        self.rpd_lock = threading.Lock()
        self.tpm_lock = threading.Lock()
        
        self.rpm_timestamps = []
        self.rpd_timestamps = []
        self.tpm_tokens = []
        
        self.last_reset = datetime.now()
    
    def wait_for_rpm(self):
        with self.rpm_lock:
            now = datetime.now()
            # Remove timestamps older than 1 minute
            self.rpm_timestamps = [ts for ts in self.rpm_timestamps if now - ts < timedelta(minutes=1)]
            
            if len(self.rpm_timestamps) >= RPM_LIMIT:
                # Wait until oldest request is more than 1 minute old
                sleep_time = (self.rpm_timestamps[0] + timedelta(minutes=1) - now).total_seconds()
                if sleep_time > 0:
                    time.sleep(sleep_time)
            
            self.rpm_timestamps.append(now)

    def wait_for_rpd(self):
        with self.rpd_lock:
            now = datetime.now()
            # Reset daily counter if it's a new day
            if now.date() > self.last_reset.date():
                self.rpd_timestamps = []
                self.last_reset = now
            
            # Remove timestamps older than 24 hours
            self.rpd_timestamps = [ts for ts in self.rpd_timestamps if now - ts < timedelta(days=1)]
            
            if len(self.rpd_timestamps) >= RPD_LIMIT:
                # Wait until oldest request is more than 24 hours old
                sleep_time = (self.rpd_timestamps[0] + timedelta(days=1) - now).total_seconds()
                if sleep_time > 0:
                    time.sleep(sleep_time)
            
            self.rpd_timestamps.append(now)
    
    def wait_for_tpm(self, tokens: int):
        with self.tpm_lock:
            now = datetime.now()
            # Remove token counts older than 1 minute
            self.tpm_tokens = [(ts, count) for ts, count in self.tpm_tokens if now - ts < timedelta(minutes=1)]
            
            current_tpm = sum(count for _, count in self.tpm_tokens)
            if current_tpm + tokens > TPM_LIMIT:
                # Wait until oldest token count is more than 1 minute old
                sleep_time = (self.tpm_tokens[0][0] + timedelta(minutes=1) - now).total_seconds()
                if sleep_time > 0:
                    time.sleep(sleep_time)
            
            self.tpm_tokens.append((now, tokens))

# Create a global rate limiter
rate_limiter = RateLimiter() 