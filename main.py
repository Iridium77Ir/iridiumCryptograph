from lib.crypter import Crypter
import argparse

parser = argparse.ArgumentParser(description='Encode files(ex: passwords). Use arguments: -d decrypt, -e encrypt, -f the filename, -p the password you use')
parser.add_argument('-d', '--decrypt', type=bool, metavar='', required=False, help='\033[93mDecrypt a file\033[0m')
parser.add_argument('-e', '--encrypt', type=bool, metavar='', required=False, help='\033[93mEncrypt a file\033[0m')
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='\033[93mThe name of the file to encode\033[0m')
parser.add_argument('-p', '--password', type=str, metavar='', required=True, help='\033[93mThe password used for decrypt\033[0m')
args = parser.parse_args()

cryptAgent = Crypter(str(args.password))
if args.decrypt is not None:
    cryptAgent.decrypt_file(str(args.file))
elif args.encrypt is not None:
    cryptAgent.encrypt_file(str(args.file))
else:
    print('please have either -d or -e to decrypt or encrypt a file!')
