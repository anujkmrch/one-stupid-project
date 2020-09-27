from fabric import Connection
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--length', dest='length', action='store_const',
                    const=sum, default=10,
                    help='sum the integers (default: find the max)')

result = Connection('xyz.com').run('uname -s')
msg = "Ran {.command!r} on {.connection.host}, got stdout:\n{.stdout}"
print(msg.format(result))
