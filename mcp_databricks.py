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

if __name__ == "__main__":
    mcp.run()