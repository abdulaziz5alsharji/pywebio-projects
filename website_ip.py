from pywebio.input import input, TEXT
from pywebio.output import put_text
from socket import gethostbyname


def website_ip():
    host = input("Website Host: ", type=TEXT)
    ip = gethostbyname(host)
    put_text(f"Website Ip Is: {ip}")


if __name__ == '__main__':
    website_ip()