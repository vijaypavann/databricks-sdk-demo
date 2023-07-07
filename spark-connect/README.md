1. **Spark Connect is enabled only on Unity Catalog enabled Shared and Single User Clusters.**

2. Only Databricks **Runtime 13.0 ML** and Databricks **Runtime 13.0** are supported.

3. Configure `.databrickscfg` [on Local machine] by setting the profile:
   ```sh
      cat ~/.databrickscfg

      [DEFAULT]
      host = https://<WS_URL>
      token = <PAT>

      [DEV]
      host = https://<WS_URL>
      token = <PAT>
      cluster_id = XXXX-XXXXX-XXXXXXXX             
   ```
   
4. Once the set up is done we can use  `DatabricksSession` from `databricks.connect` module to run spark code
         
5. [Sample Code](./demo.py) to test Spark Connect

6. [Reference link](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect)

