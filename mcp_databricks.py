import os
from typing import Annotated, List, Literal, Optional

from fastmcp import FastMCP
from pydantic import BaseModel
import requests

databricks_host = os.environ["DATABRICKS_HOST"]
databricks_token = os.environ["DATABRICKS_TOKEN"]

headers = {"Authorization": f"Bearer {databricks_token}"}

mcp = FastMCP("databricks")

@mcp.tool(tags=["workspace", "databricks_workspace", "git_credentials"])
def list_git_credentials() -> str:
    """List the Git credentials"""
    url = "/api/2.0/git-credentials"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "git_credentials"])
def create_git_credentials(
    git_provider: Literal["gitHub", "bitbucketCloud", "gitLab", "azureDevOpsServices", "gitHubEnterprise", "bitbucketServer", "gitLabEnterpriseEdition", "awsCodeCommit"],
    git_email: Annotated[str | None, "Optional, The authenticating email associated with your Git provider user account. Used for authentication with the remote repository and also sets the author & committer identity for commits. Required for most Git providers except AWS CodeCommit"] = None,
    git_username: Annotated[str | None, "Optional. The Git username associated with the credential. Required for AWS CodeCommit"] = None,
    is_default_for_provider: Annotated[bool | None, "Optional"] = None,
    name: Annotated[str | None, "Optional"] = None,
    personal_access_token: Annotated[str | None, "Optional"] = None,    
    ) -> str:
    """Create Git credentials"""
    url = "/api/2.0/git-credentials"
    data = {
        "git_provider": git_provider,
        "git_email": git_email,
        "git_username": git_username,
        "is_default_for_provider": is_default_for_provider,
        "name": name,
        "personal_access_token": personal_access_token,
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "git_credentials"])
def get_git_credential(credential_id: int) -> str:
    """Get a Git credential"""
    url = f"/api/2.0/git-credentials/{credential_id}"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "git_credentials"])
def update_git_credential(
    credential_id: int,
    git_provider: Literal["gitHub", "bitbucketCloud", "gitLab", "azureDevOpsServices", "gitHubEnterprise", "bitbucketServer", "gitLabEnterpriseEdition", "awsCodeCommit"],
    git_email: Annotated[str | None, "Optional. The authenticating email associated with your Git provider user account. Used for authentication with the remote repository and also sets the author & committer identity for commits. Required for most Git providers except AWS CodeCommit"] = None,
    git_username: Annotated[str | None, "Optional. The Git username associated with the credential. Required for AWS CodeCommit"] = None,
    is_default_for_provider: Annotated[bool | None, "Optional"] = None,
    name: Annotated[str | None, "Optional"] = None,
    personal_access_token: Annotated[str | None, "Optional"] = None,    
    ) -> str:
    """Update a Git credential"""
    url = f"/api/2.0/git-credentials/{credential_id}"
    data = {
        "git_provider": git_provider,
        "git_email": git_email,
        "git_username": git_username,
        "is_default_for_provider": is_default_for_provider,
        "name": name,
        "personal_access_token": personal_access_token,
    }
    response = requests.patch(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "git_credentials"])
def delete_git_credential(credential_id: int) -> str:
    """Delete a Git credential"""
    url = f"/api/2.0/git-credentials/{credential_id}"
    response = requests.delete(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def get_repo_permissions(repo_id: str) -> str:
    """Get repository permissions"""
    url = f"/api/2.0/permissions/repos/{repo_id}"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

class AccessControlEntry(BaseModel):
    group_name: Optional[str] = None
    permission_level: Optional[Literal["CAN_MANAGE", "CAN_EDIT", "CAN_RUN", "CAN_READ"]] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def set_repo_permissions(
    repo_id: str,
    access_control_list: Annotated[Optional[List[AccessControlEntry]] | None, "Optional. List of access control entries"] = None,
    ) -> str:
    """Set repository permissions"""
    url = f"/api/2.0/permissions/repos/{repo_id}"
    data = {"access_control_list": access_control_list}
    response = requests.put(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def update_repo_permissions(
    repo_id: str,
    access_control_list: Annotated[Optional[List[AccessControlEntry]] | None, "Optional. List of access control entries"] = None,
    ) -> str:
    """Update repository permissions"""
    url = f"/api/2.0/permissions/repos/{repo_id}"
    data = {"access_control_list": access_control_list}
    response = requests.patch(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def get_repo_permission_levels(repo_id: str,) -> str:
    """Get repository permission levels"""
    url = f"/api/2.0/permissions/repos/{repo_id}/permissionLevels"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def get_repos() -> str:
    """Get all repositories"""
    url = "/api/2.0/repos"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

class SparseCheckoutEntry(BaseModel):
    patterns: List[str]

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def create_repo(
    url: str,
    provider: Literal["gitHub", "bitbucketCloud", "gitLab", "azureDevOpsServices", "gitHubEnterprise", "bitbucketServer", "gitLabEnterpriseEdition", "awsCodeCommit"],
    path: Annotated[Optional[str] | None, "Optional. Desired path for the repo in the workspace"] = None,
    sparse_checkout: Annotated[Optional[SparseCheckoutEntry] | None, "Optional. Whether to enable sparse checkout for the repo"] = None,
) -> str:
    """Create a new repository"""
    url = "/api/2.0/repos"
    data = {
        "url": url,
        "provider": provider,
        "path": path,
        "sparse_checkout": sparse_checkout,
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def get_repo(repo_id: str) -> str:
    """Get a repository"""
    url = f"/api/2.0/repos/{repo_id}"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def update_repo(
    repo_id: str,
    branch: Annotated[Optional[str] | None, "Optional. Desired branch for the repo"] = None,
    sparse_checkout: Annotated[Optional[SparseCheckoutEntry] | None, "Optional. Whether to enable sparse checkout for the repo"] = None,
    tag: Annotated[Optional[str] | None, "Optional. Desired tag for the repo"] = None,
) -> str:
    """Update a repository"""
    url = f"/api/2.0/repos/{repo_id}"
    data = {
        "url": url,
        "branch": branch,
        "sparse_checkout": sparse_checkout,
        "tag": tag,
    }
    response = requests.patch(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "repos"])
def delete_repo(repo_id: int) -> str:
    """Delete a repository"""
    url = f"/api/2.0/repos/{repo_id}"
    response = requests.delete(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def delete_acl(principal: str, scope: str) -> str:
    """Delete the access control list (ACL) for a principal on a secret scope."""
    url = "/api/2.0/secrets/acls/delete"
    data = {
        "principal": principal,
        "scope": scope
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def get_acl(principal: str, scope: str) -> str:
    """Get the access control list (ACL) for a principal on a secret scope."""
    url = "/api/2.0/secrets/acls/get"
    data = {
        "principal": principal,
        "scope": scope
    }
    response = requests.get(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def list_acls(scope: str) -> str:
    """List the access control lists (ACLs) for a secret scope."""
    url = "/api/2.0/secrets/acls/list"
    data = {
        "scope": scope
    }
    response = requests.get(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def create_update_acl(
    principal: str,
    scope: str,
    permission: Literal["READ", "WRITE", "MANAGE"]
    ) -> str:
    """Create or update the access control list (ACL) for a principal on a secret scope."""
    url = "/api/2.0/secrets/acls/set"
    data = {
        "principal": principal,
        "scope": scope,
        "permission": permission,
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def delete_secret(scope: str, key: str) -> str:
    """Delete a secret from a secret scope."""
    url = "/api/2.0/secrets/delete"
    data = {
        "scope": scope,
        "key": key
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def get_secret(scope: str, key: str) -> str:
    """Get a secret from a secret scope."""
    url = "/api/2.0/secrets/get"
    data = {
        "scope": scope,
        "key": key
    }
    response = requests.get(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def list_secrets(scope: str) -> str:
    """List secrets in a secret scope."""
    url = "/api/2.0/secrets/list"
    data = {
        "scope": scope
    }
    response = requests.get(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def create_secret(
    scope: str,
    key: str,
    string_value: Annotated[Optional[str] | None, "Optional. The string value of the secret. Either string_value or bytes_value must be provided."] = None,
    bytes_value: Annotated[Optional[bytes] | None, "Optional. The byte value of the secret. Either string_value or bytes_value must be provided."] = None,
    ) -> str:
    """Create a secret in a secret scope."""
    url = "/api/2.0/secrets/put"
    data = {
        "scope": scope,
        "key": key,
        "string_value": string_value,
        "bytes_value": bytes_value,
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def create_scope(
    scope: str,
    initial_manage_principal: Annotated[Optional[str] | None, "Optional. The principal (user or group) that is granted the MANAGE permission on the created secret scope. If not specified, the caller is granted the MANAGE permission."] = None,
    scope_backend_type: Annotated[Optional[Literal["DATABRICKS", "AZURE_KEYVAULT"]] | None, "Optional. If not specified, will default to DATABRICKS."] = None
    ) -> str:
    """Create a secret scope."""
    url = "/api/2.0/secrets/scopes/create"
    data = {
        "scope": scope,
        "initial_manage_principal": initial_manage_principal,
        "scope_backend_type": scope_backend_type,
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def delete_scope(scope: str) -> str:
    """Delete a secret scope."""
    url = "/api/2.0/secrets/scopes/delete"
    data = {
        "scope": scope
    }
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "secret"])
def list_scopes() -> str:
    """List secret scopes."""
    url = "/api/2.0/secrets/scopes/list"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def get_workspace_object_permission(
    workspace_object_type: str,
    workspace_object_id: str,
    ) -> str:
    """Get workspace object permissions"""
    url = f"/api/2.0/permissions/{workspace_object_type}/{workspace_object_id}"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def set_workspace_object_permission(
    workspace_object_type: str,
    workspace_object_id: str,
    access_control_list: Annotated[Optional[List[AccessControlEntry]] | None, "Optional. List of access control entries"] = None,
    ) -> str:
    """Set workspace object permissions"""
    url = f"/api/2.0/permissions/{workspace_object_type}/{workspace_object_id}"
    data = {"access_control_list": access_control_list}
    response = requests.put(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def update_workspace_object_permission(
    workspace_object_type: str,
    workspace_object_id: str,
    access_control_list: Annotated[Optional[List[AccessControlEntry]] | None, "Optional. List of access control entries"] = None,
    ) -> str:
    """Update workspace object permissions"""
    url = f"/api/2.0/permissions/{workspace_object_type}/{workspace_object_id}"
    data = {"access_control_list": access_control_list}
    response = requests.patch(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def get_workspace_object_permission_levels(
    workspace_object_type: str,
    workspace_object_id: str,
    ) -> str:
    """Get workspace object permission levels"""
    url = f"/api/2.0/permissions/{workspace_object_type}/{workspace_object_id}/permissionLevels"
    response = requests.get(databricks_host + url, headers=headers)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def delete_workspace_object(path: str, recursive: bool | None = False) -> str:
    """Delete a workspace object"""
    url = "/api/2.0/workspace/delete"
    data = {"path": path, "recursive": recursive}
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def export_workspace_object(
    path: str,
    format: Literal["SOURCE", "HTML", "JUPYTER", "DBC", "R_MARKDOWN", "AUTO", "RAW"] = "SOURCE",
    direct_download: bool | None = False,
    ) -> str:
    """Export a workspace object"""
    url = "/api/2.0/workspace/export"
    params = {"path": path, "format": format, "direct_download": direct_download}
    response = requests.get(databricks_host + url, headers=headers, params=params)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def get_object_status(path: str) -> str:
    """Get the status of a workspace object"""
    url = "/api/2.0/workspace/get-status"
    params = {"path": path}
    response = requests.get(databricks_host + url, headers=headers, params=params)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def import_workspace_object(
    path: str,
    content: Annotated[Optional[str] | None, "Optional. Base64-encoded content of the object to be imported. Required if overwrite is true or if the object does not already exist at the specified path."] = None,
    format: Literal["SOURCE", "HTML", "JUPYTER", "DBC", "R_MARKDOWN", "AUTO", "RAW"] = "SOURCE",
    language: Annotated[Optional[Literal["SCALA", "PYTHON", "SQL", "R"]] | None, "Optional. This value is set only if the object type is NOTEBOOK."] = None,
    overwrite: bool | None = False,
    ) -> str:
    """Import a workspace object"""
    url = "/api/2.0/workspace/import"
    data = {"path": path, "content": content, "format": format, "language": language, "overwrite": overwrite}
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def list_workspace_objects(path: str, notebooks_modified_after: Annotated[int | None, "Optional. UTC timestamp in milliseconds"] = None) -> str:
    """List workspace objects"""
    url = "/api/2.0/workspace/list"
    params = {"path": path}
    if notebooks_modified_after:
        params["notebooks_modified_after"] = notebooks_modified_after
    response = requests.get(databricks_host + url, headers=headers, params=params)
    return response.text

@mcp.tool(tags=["workspace", "databricks_workspace", "workspace"])
def create_directory(path: str) -> str:
    """Create a directory in the workspace"""
    url = "/api/2.0/workspace/mkdirs"
    data = {"path": path}
    response = requests.post(databricks_host + url, headers=headers, json=data)
    return response.text

if __name__ == "__main__":
    mcp.run()