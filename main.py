from ecdsa import SigningKey, NIST256p

if __name__ == "__main__":
    n_pairs = input("Введите количество ключей для генерации: ")

    private_dir = input("Введите адрес директории для private ключей c '/' в конце (или 'defualt' для директории по умолчанию): ")
    if private_dir == "default":
        private_dir = "private_keys/"

    public_dir = input("Введите адрес директории для public ключей c '/' в конце (или 'defualt' для директории по умолчанию): ")
    if public_dir == "default":
        public_dir = "public_keys/"
    try:
        for i in range(int(n_pairs)):
            key_id = 1000 + i

            private = SigningKey.generate(curve=NIST256p)
            private_pem = private.to_pem()

            with open(f"{private_dir}private_key_{str(key_id)}.pem", "wb") as private_file:
                private_file.write(private_pem)

            with open(f"{public_dir}public_key_{str(key_id)}.pem", "wb") as public_file:
                public_file.write(private.get_verifying_key().to_pem())
    except Exception as e:
        print(e)