from passlib.context import CryptContext


crypto_hash = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
	return crypto_hash.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
	return crypto_hash.verify(password, password_hash)
