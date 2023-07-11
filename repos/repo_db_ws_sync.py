from argparse import ArgumentParser
import sys
    
from databricks.sdk import WorkspaceClient
from repos.literals import GIT_URL, GIT_PROVIDER


def create_or_update_repo(git_checkout_path: str, git_remote_branch: str):
    """ - Creates a `Repo` in `Databricks Workspace` [if it doesn't exist]
            using `Databricks SDK` and `DEV Profile` 
        - Updates the Repo if it's already present
    """
    
    # Create a `WorkspaceClient` using `DEV Profile`
    # Alternatively we can use Azure Active Directory Authenication / Service Principal
    ws = WorkspaceClient(profile = "DEV")

    # Filter the repos list using `path_prefix`
    repos_list = ws.repos.list(path_prefix = git_checkout_path)

    repos_list = list(repos_list)

    if not repos_list:
        print("Repo is not Present in DB Workspace, \n Creating a new one....")
        repoInfo = ws.repos.create(url = GIT_URL, provider = GIT_PROVIDER, path = git_checkout_path)
        print(repoInfo)
        # Ex: RepoInfo(branch='main', head_commit_id='b3e3c827a755aa235f0c884b99d37af220139364', id=2668333326914369, path='/Repos/<USERNAME>@<ORG>.com/<DIR>', provider='gitHub', sparse_checkout=None, url='https://github.com/vijaypavann/databricks-sdk-demo.git')
    else: 
        print("Updating an existing Repo in DB Workspace....")
        repoId = None

        for repo in repos_list:
            print(repo.path, repo.id, repo.url) 
            if repo.branch == git_remote_branch:
                repoId = repo.id
                break    

        if repoId:
            ws.repos.update(repo_id = repoId, branch = git_remote_branch)


if __name__ == "__main__":
    
    """
        Parse the Arguments passed to the python file
        python <FILE_NAME>.py --git_checkout_path ${{ secrets.GIT_CHECKOUT_PATH }} 
                       --branch_name ${GITHUB_REF#refs/heads/}
    """
    parser = ArgumentParser()

    parser.add_argument("--branch_name", required = False, type = str)
    parser.add_argument("--git_checkout_path", required = False, type = str)

    namespace = parser.parse_known_args(sys.argv + [ '', ''])[0]

    git_remote_branch_name = namespace.branch_name
    print('Branch Name: ', git_remote_branch_name)

    git_checkout_path = namespace.git_checkout_path
    print('git checkout path: ', git_checkout_path)

    create_or_update_repo(git_checkout_path, git_remote_branch_name)