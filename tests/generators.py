import random
import string

def generate_email():
    return f"rimma_rendikova_5_{random.randint(100, 999)}@yandex.ru"

def generate_password():
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for _ in range(8))

