from argparse import ArgumentParser
import sys

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--git_path", required = False, type = str)
    parser.add_argument("--db_host", required=False, type=str)

    namespace = parser.parse_known_args(sys.argv + [ '', ''])[0]
    git_path = namespace.git_path
    print('GIT_CHECKOUT_PATH Name: ', git_path)

    db_host = namespace.db_host
    print('DATABRICKS_HOST : ', db_host)

