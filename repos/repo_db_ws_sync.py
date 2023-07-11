from argparse import ArgumentParser
import sys
    

from databricks.sdk import WorkspaceClient
from repos.literals import GIT_CHECKOUT_PATH, GIT_URL, GIT_PROVIDER, GIT_REMOTE_BRANCH

def create_or_update_repo():
    """ - Creates a `Repo` in `Databricks Workspace` using `Databricks SDK` 
            and `DEV Profile` [if it doesn't exist]
        - Updates the Repo if it's already present
    """
    
    # Create a `WorkspaceClient` using `DEV Profile`
    # Alternatively we can use Azure Active Directory Authenication / Service Principal
    ws = WorkspaceClient(profile = "DEV")

    # Filter the repos list using `path_prefix`
    
    repos_list = ws.repos.list(path_prefix = GIT_CHECKOUT_PATH)

    repos_list = list(repos_list)

    if not repos_list:
        print("Repo is not Present in DB Workspace, \n Creating a new one....")
        repoInfo = ws.repos.create(url = GIT_URL, provider = GIT_PROVIDER, path = GIT_CHECKOUT_PATH)
        print(repoInfo)
        # Ex: RepoInfo(branch='main', head_commit_id='b3e3c827a755aa235f0c884b99d37af220139364', id=2668333326914369, path='/Repos/<USERNAME>@<ORG>.com/develop', provider='gitHub', sparse_checkout=None, url='https://github.com/vijaypavann/databricks-sdk-demo.git')
    else:
        print("Updating an existing Repo in DB Workspace....")
        repoId = None

        for repo in repos_list:
            print(repo.path, repo.id, repo.url) 
            if repo.branch == GIT_REMOTE_BRANCH:
                repoId = repo.id
                break    

        if repoId:
            ws.repos.update(repo_id = repoId, branch = GIT_REMOTE_BRANCH)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--GIT_CHECKOUT_PATH", required = False, type = str)
    parser.add_argument("--pr_branch", required=False, type=str)

    namespace = parser.parse_known_args(sys.argv + [ '', ''])[0]
    branch_name = namespace.branch_name
    print('Branch Name: ', branch_name)

    pr_branch = namespace.pr_branch
    print('PR Branch: ', pr_branch)

    create_or_update_repo()