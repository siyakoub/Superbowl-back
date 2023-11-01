import secrets
import string


def generate_reset_token():
    # Définissez la longueur du jeton
    token_length = 32  # Vous pouvez ajuster la longueur selon vos besoins

    # Générez un jeton aléatoire sécurisé
    token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(token_length))

    return token

def generate_reset_password_url(token):
    base_url = "https://localhost:3000/reset-password"  # Remplacez par l'URL de votre site
    reset_url = f"{base_url}?token={token}"
    return reset_url

if __name__ == "__main__":
    print(generate_reset_password_url(generate_reset_token()))