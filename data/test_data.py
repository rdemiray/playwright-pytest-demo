from dataclasses import dataclass
from utils.utils import generate_random_email, generate_password

@dataclass
class SignupTestData:
    email: str
    password: str
    country: str

test_data_for_tc3 = SignupTestData(
    email=generate_random_email(), 
    password=generate_password(),
    country="Canada"
)