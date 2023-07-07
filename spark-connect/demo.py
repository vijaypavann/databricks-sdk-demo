# Import DatabricksSession from databricks.connect
from databricks.connect import DatabricksSession
from databricks.sdk.core import Config


def spark_connect_using_environment():
    """
        This  function invokes Databricks Session and run spark code using the remote databricks cluster.
        Need to set up SPARK_REMOTE environment variable before invoking below method
    """
    # export SPARK_REMOTE="sc://<WS_URL>:443/;token=<PAT>;x-databricks-cluster-id=<CLUSTER_ID>" 
    spark = DatabricksSession.builder.getOrCreate()
    spark.sql("show tables").show()

def spark_connect_using_remote_url():
    """
        This  function invokes Databricks Session and run spark code using the remote databricks cluster.
        Here cluster configuration can be given in the code itself inside remote() method
    """
    REMOTE_URL = "sc://<WS_URL>:443/;token=<PAT>;x-databricks-cluster-id=<CLUSTER_ID>" 
    spark = DatabricksSession.builder.remote(REMOTE_URL).getOrCreate()
    spark.sql("show databases").show()

def spark_connect_using_config():
    config = Config(profile = "DEV")
    spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

    query = "show tables from default1" 
   #  query = "show databases"
   #  query = "create database if not exists demo"

    # query = "USE default1" 
    df = spark.sql(query)
    df.show()

if __name__ == "__main__":

    # spark_connect_using_environment()
    # spark_connect_using_remote_url()

    spark_connect_using_config()