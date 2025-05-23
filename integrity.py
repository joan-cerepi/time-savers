#!/usr/bin/python3

import argparse
import hashlib
import os.path


def set_arguments(parser: argparse.ArgumentParser) -> None:
    """Set script arguments."""
    parser.add_argument('-p', '--path', help='Specify the path to the file whose integrity you are checking.', required=True)
    parser.add_argument('--hash', help="Specify the hash that the file digest needs to match.", required=True)
    parser.add_argument('-a', '--algorithm', help='Choose which hashing algorithm you want to use. Default is sha256', choices=['sha3_512', 'sha1', 'sha256', 'sha224', 'sha512', 'sha3_256', 'blake2b', 'shake_128', 'sha384', 'sha3_384', 'blake2s', 'shake_256', 'sha3_224', 'md5'], default='sha256')


def verify_integrity(args: argparse.Namespace) -> None:
    """Verify file integrity by comparing hash digests."""
    if os.path.exists(args.path):
        # Terminal color codes.
        GREEN = '\u001b[32m'
        RED = '\u001b[31m'
        RESET = '\u001b[0m'

        # Hashing.
        hasher = hashlib.new(args.algorithm)
        file_digest = None

        with open(args.path, 'rb') as file:
            while chunk := file.read(4096):
                hasher.update(chunk)
            file_digest = hasher.hexdigest()

        if file_digest == args.hash:
            print(f'{GREEN}The hashes match. Your file\'s integrity is intact.{RESET}')
        else:
            print(f'{RED}The hashes did not match. Your file is either corrupt or has been tampered with.{RESET}')
    else:
        print('Invalid path. Check your file path and try again.')

        

def main() -> None:
    """The main entry point of the script."""
    parser = argparse.ArgumentParser(prog='Integrity')
    set_arguments(parser)

    args = parser.parse_args()
    verify_integrity(args)


if __name__ == '__main__':
    main()