"""
    Самым частовызываемым вызывом оказался openat,
    проверял при помощи strace -c <option> <args>.
    Самым "горячим участком" кода оказалась функция dir_handler,
    проверял при помощи cProfile
    Наиболее потребляемым по времени вызовом оказался openat,
    проверял аналагично первому пункту.
    P.S. в logs.txt файле прикладываю один из выводов cProfile и strace.
"""
import os
import hashlib
import cProfile


def hash_comparer(content: list, hash: str) -> None:
    for roots, dirs, files in content:
        for filename in files:
            try:
                with open(filename, "rb") as f:
                    data = f.read()
                    if not data:
                        break
                    file_hash = hashlib.sha256(data).hexdigest()
                    if hash == file_hash:
                        print(os.path.abspath(filename))
            except FileNotFoundError:
                continue


def dir_handler():
    content = []
    for root, dirs, files in os.walk(path):
        content.append((root, dirs, files))
    return content


def main():
    content = dir_handler()
    hash_comparer(content, hash_sha)


if __name__ == '__main__':
    path = input('Enter the path to dir:')
    hash_sha = input('Enter sha256:')
    cProfile.run('main()')