import os
from typing import Annotated, Literal

from fastmcp import FastMCP
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

if __name__ == "__main__":
    mcp.run()