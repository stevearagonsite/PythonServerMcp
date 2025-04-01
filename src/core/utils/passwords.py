import random
import string
import pyotp


def generate_password(length: int = 20):
    DIGITS_QTY = length // 3
    digits = "".join((random.choice(string.digits) for _ in range(DIGITS_QTY)))
    letters = "".join((random.choice(string.ascii_letters) for _ in range(length - DIGITS_QTY)))
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    final_string = "".join(sample_list)
    return final_string


def validate_otp(key: str, otp_code: str) -> bool:
    totp = pyotp.TOTP(key)
    return totp.verify(otp_code)
