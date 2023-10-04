import hashlib
import os


def hash_password(password):
    """
    Hashes a password using SHA-256.

    :param password: Le mot à hasher.
    :return: The hashed password.
    """
    password = password.encode('utf-8')  # Encode the password as bytes
    # Combine the password and salt, then hash the result using SHA-256
    hashed_password = hashlib.sha256(password).hexdigest()

    # Return the hashed password and salt as a tuple
    return hashed_password
