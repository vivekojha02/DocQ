import random
import time
from config import OTP_VALIDITY_MINUTES, MAX_OTP_REQUESTS, OTP_COOLDOWN_SECONDS

otp_store = {}
otp_request_tracker = {}

class OTPTracker:
    def __init__(self):
        self.requests = {}

    def allow(self, email):
        now = time.time()
        self.cleanup(email)

        if email not in self.requests:
            self.requests[email] = []

        # Too frequent?
        if self.requests[email] and (now - self.requests[email][-1]) < OTP_COOLDOWN_SECONDS:
            return False

        if len(self.requests[email]) >= MAX_OTP_REQUESTS:
            return False

        self.requests[email].append(now)
        return True

    def cleanup(self, email):
        now = time.time()
        self.requests[email] = [t for t in self.requests.get(email, []) if now - t < 600]

otp_request_tracker = OTPTracker()

def generate_otp(email):
    otp = str(random.randint(100000, 999999))
    otp_store[email] = {
        'otp': otp,
        'timestamp': time.time()
    }
    return otp

def validate_otp(email, otp_input):
    record = otp_store.get(email)
    if not record:
        return False

    valid_duration = OTP_VALIDITY_MINUTES * 60
    if time.time() - record['timestamp'] > valid_duration:
        otp_store.pop(email, None)
        return False

    if record['otp'] == otp_input:
        otp_store.pop(email, None)
        return True

    return False
