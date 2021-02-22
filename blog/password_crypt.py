from cryptography.fernet import Fernet


def encrypt_p(password):
    f = Fernet('Ow2Qd11KeZS_ahNOMicpWUr3nu3RjOUYa0_GEuMDlOc=')
    try:
        p1 = password.encode()
        token=f.encrypt(p1)
        p2=token.decode()
        return p2
    except Exception as e:
        print("error ",e)
        return None

def decrypt_p(password):
    f = Fernet('Ow2Qd11KeZS_ahNOMicpWUr3nu3RjOUYa0_GEuMDlOc=')
    try:
        p1=password.encode()
        token=f.decrypt(p1)
        p2=token.decode()
        return p2
    except Exception as e:
        print("error ",e)
        return None



if __name__ == '__main__':
    a = encrypt_p('Namatullah')
    print(a)
    b = decrypt_p(
        'gAAAAABgM9CkQfe0vKCVnvmUtm03RupF4HIbaxemUithbafMpcuAvxyPXaO1oh9SHUw-RaanZeSKFPjkJVas_kxaKO2OTMmT3g==')
    print(b)
