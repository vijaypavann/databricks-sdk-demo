def get_secret():
    """ Access Secrets using `Databricks SDK` usind DEV profile
    """
    from databricks.sdk import WorkspaceClient

    ws = WorkspaceClient(profile = "DEV")

    scopes = ws.secrets.list_scopes()
    print(scopes, type(scopes))

get_secret()


def get_secret_cli():
  # Legacy (pip install databricks-cli)
  """ This is the old way of accessing the Secrets using databricks_cli
  """
  from databricks_cli.secrets.api import SecretApi
  from databricks_cli.sdk.api_client import ApiClient
  import os

  api_client = ApiClient(
    host  = os.getenv('DATABRICKS_HOST'),
    token = os.getenv('DATABRICKS_TOKEN')
  )
  a = SecretApi(api_client)
  scopes = a.list_scopes()
  print(scopes, type(scopes))



