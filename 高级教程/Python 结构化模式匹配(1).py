import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['push', 'pull', 'commit'])
    args = parser.parse_args()

    match args.command:
        case 'push':
            print('pushing')
        case 'pull':
            print('pulling')
        case _:
            parser.error(f'{args.command!r} not yet implemented')