# mcp-databricks
The Databricks MCP (Model Context Protocol).

## Features
Current implementation support all "Databricks Workspace" endpoints from the Databricks API.

## Usage

### Using pip

1. Install Python from your preferred distribution like [python.org](https://www.python.org/downloads/) or [anaconda.com](https://www.anaconda.com/download) or other
2. Clone the repository `git clone https://github.com/jaymeanchante/mcp-databricks`
3. (Optional) Create a Python virtual environment from your preferred tool and activate it
3. Install requirements `pip install fastmcp==2.12.5`
4. Add the server configuration in your MCP client:
```json
"servers": {
  "databricks": {
    "command": "/path/to/python",
    "args": ["/path/to/mcp-databricks/mcp_databricks.py"],
    "env": {
      "DATABRICKS_HOST": "",
      "DATABRICKS_TOKEN": "",
    },
  }
}
```

### Using uv
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repository `git clone https://github.com/jaymeanchante/mcp-databricks`
3. Add the server configuration in your MCP client:
```json
"servers": {
  "databricks": {
    "command": "uvx",
    "args": ["--with", "fastmcp==2.12.5", "python", "/path/to/mcp-databricks/mcp_databricks.py"],
    "env": {
      "DATABRICKS_HOST": "",
      "DATABRICKS_TOKEN": "",
    },
  }
}
```

## Support
The MCP Databricks API currently support the following endpoints:

| Support | Type | Category | Subcategory |
|---------|------|----------|-------------|
|   ✅   | workspace | databricks_workspace | git_credentials |
|   ✅   | workspace | databricks_workspace | repos |
|   ✅   | workspace | databricks_workspace | secret |
|   ✅   | workspace | databricks_workspace | workspace |
|   ✅   | workspace | compute | cluster_policies |
|   ❌   | workspace | compute | clusters |
|   ❌   | workspace | compute | command_execution |
|   ❌   | workspace | compute | global_init_scripts |
|   ❌   | workspace | compute | instance_pools |
|   ❌   | workspace | compute | instance_profiles |
|   ❌   | workspace | compute | managed_libraries |
|   ❌   | workspace | compute | policy_compliance_for_clusters |
|   ❌   | workspace | compute | policy_families |
|   ❌   | workspace | workflows | jobs |
|   ❌   | workspace | workflows | jobs_legacy |
|   ❌   | workspace | workflows | policy_compliance_for_jobs |
|   ❌   | workspace | delta_live_tables | pipelines |
|   ❌   | workspace | file_management | dbfs |
|   ❌   | workspace | file_management | files |
|   ❌   | workspace | machine_learning | experiments |
|   ❌   | workspace | machine_learning | experiments_tracing |
|   ❌   | workspace | machine_learning | model_registry |
|   ❌   | workspace | real_time_serving | serving_endpoints |
|   ❌   | workspace | apps | apps |
|   ❌   | workspace | vector_search | endpoints |
|   ❌   | workspace | vector_search | indexes |
|   ❌   | workspace | identity_and_access_management | account_access_control_proxy |
|   ❌   | workspace | identity_and_access_management | current_user |
|   ❌   | workspace | identity_and_access_management | groups |
|   ❌   | workspace | identity_and_access_management | permissions |
|   ❌   | workspace | identity_and_access_management | service_principals |
|   ❌   | workspace | identity_and_access_management | users |
|   ❌   | workspace | identity_and_access_management | iam_v2 |
|   ❌   | workspace | databricks_sql | alerts |
|   ❌   | workspace | databricks_sql | alerts_legacy |
|   ❌   | workspace | databricks_sql | alerts_v2 |
|   ❌   | workspace | databricks_sql | dashboards_legacy |
|   ❌   | workspace | databricks_sql | data_sources_legacy |
|   ❌   | workspace | databricks_sql | acl_permissions |
|   ❌   | workspace | databricks_sql | queries |
|   ❌   | workspace | databricks_sql | queries_legacy |
|   ❌   | workspace | databricks_sql | query_history |
|   ❌   | workspace | databricks_sql | statement_execution |
|   ❌   | workspace | databricks_sql | sql_warehouses |
|   ❌   | workspace | ai_bi | genie |
|   ❌   | workspace | ai_bi | lakeview |
|   ❌   | workspace | ai_bi | lakeview_embedded |
|   ❌   | workspace | unity_catalog | artifact_allowlists |
|   ❌   | workspace | unity_catalog | catalogs |
|   ❌   | workspace | unity_catalog | connections |
|   ❌   | workspace | unity_catalog | credentials |
|   ❌   | workspace | unity_catalog | entity_tag_assignments |
|   ❌   | workspace | unity_catalog | external_lineage |
|   ❌   | workspace | unity_catalog | external_locations |
|   ❌   | workspace | unity_catalog | external_metadata |
|   ❌   | workspace | unity_catalog | functions |
|   ❌   | workspace | unity_catalog | grants |
|   ❌   | workspace | unity_catalog | metastores |
|   ❌   | workspace | unity_catalog | model_versions |
|   ❌   | workspace | unity_catalog | online_tables |
|   ❌   | workspace | unity_catalog | abac_policies |
|   ❌   | workspace | unity_catalog | quality_monitors |
|   ❌   | workspace | unity_catalog | registered_models |
|   ❌   | workspace | unity_catalog | resource_quotas |
|   ❌   | workspace | unity_catalog | request_for_access |
|   ❌   | workspace | unity_catalog | schemas |
|   ❌   | workspace | unity_catalog | storage_credentials |
|   ❌   | workspace | unity_catalog | system_schemas |
|   ❌   | workspace | unity_catalog | table_constraints |
|   ❌   | workspace | unity_catalog | tables |
|   ❌   | workspace | unity_catalog | temporary_path_credentials |
|   ❌   | workspace | unity_catalog | temporary_table_credentials |
|   ❌   | workspace | unity_catalog | volumes |
|   ❌   | workspace | unity_catalog | workspace_bindings |
|   ❌   | workspace | delta_sharing | providers |
|   ❌   | workspace | delta_sharing | recipient_activation |
|   ❌   | workspace | delta_sharing | recipient_fedaration_policies |
|   ❌   | workspace | delta_sharing | recipients |
|   ❌   | workspace | delta_sharing | shares |
|   ❌   | workspace | settings | settings |
|   ❌   | workspace | settings | ip_access_lists |
|   ❌   | workspace | settings | notification_destionations |
|   ❌   | workspace | settings | settings_api_v2 |
|   ❌   | workspace | settings | token_management |
|   ❌   | workspace | settings | token |
|   ❌   | workspace | settings | workspace_conf |
|   ❌   | workspace | oath | service_principal_secrets_proxy |
|   ❌   | workspace | marketplace | consumer_fulfillments |
|   ❌   | workspace | marketplace | consumer_installations |
|   ❌   | workspace | marketplace | consumer_listings |
|   ❌   | workspace | marketplace | consumer_personalization_requests |
|   ❌   | workspace | marketplace | consumer_providers |
|   ❌   | workspace | marketplace | provider_exchange_filters |
|   ❌   | workspace | marketplace | provider_exchanges |
|   ❌   | workspace | marketplace | provider_files |
|   ❌   | workspace | marketplace | provider_listings |
|   ❌   | workspace | marketplace | provider_personalization_requests |
|   ❌   | workspace | marketplace | provider_providers_analytics_dashboards |
|   ❌   | workspace | marketplace | provider_providers |
|   ❌   | workspace | clean_rooms | asset_revisions |
|   ❌   | workspace | clean_rooms | assets |
|   ❌   | workspace | clean_rooms | auto_approval_rules |
|   ❌   | workspace | clean_rooms | task_runs |
|   ❌   | workspace | clean_rooms | clean_rooms |
|   ❌   | workspace | quality_monitor | quality_monitor_v2 |
|   ❌   | workspace | data_quality_monitoring | data_quality_monitors |
|   ❌   | workspace | database_instances | database_instances |
|   ❌   | workspace | tags | tag_policies |