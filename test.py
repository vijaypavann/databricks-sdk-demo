from argparse import ArgumentParser
import sys

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--git_path", required = False, type = str)
    parser.add_argument("--db_host", required=False, type=str)
    parser.add_argument("--db_token", required=False, type=str)

    namespace = parser.parse_known_args(sys.argv + [ '', '', ''])[0]
    git_path = namespace.git_path
    print('GIT_CHECKOUT_PATH Name: ', git_path)

    db_host = namespace.db_host
    print('DATABRICKS_HOST : ', db_host)

    db_token = namespace.db_token
    print('db_token : ', db_token)

    from databricks.sdk import WorkspaceClient

    ws = WorkspaceClient(host= db_host, token=db_token)

    scopes = ws.secrets.list_scopes()
    print(scopes, type(scopes))


