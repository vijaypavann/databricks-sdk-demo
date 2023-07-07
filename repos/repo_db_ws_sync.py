from databricks.sdk import WorkspaceClient
from repos.literals import GIT_CHECKOUT_PATH, GIT_URL, GIT_PROVIDER, GIT_REMOTE_BRANCH

def create_or_update_repo():
    """ - Creates a `Repo` in `Databricks Workspace` using `Databricks SDK` 
            and `EE-DEMO Profile` [if it doesn't exist]
        - Updates the Repo if it's already present
    """
    
    # Create a `WorkspaceClient` using `EE-DEMO Profile`
    ws = WorkspaceClient(profile = "EE-DEMO")

    # Filter the repos list using `path_prefix`
    
    repos_list = ws.repos.list(path_prefix = GIT_CHECKOUT_PATH)

    repos_list = list(repos_list)

    if not repos_list:
        print("Repo is not Present in DB Workspace, \n Creating a new one....")
        repoInfo = ws.repos.create(url = GIT_URL, provider = GIT_PROVIDER, path = GIT_CHECKOUT_PATH)
        print(repoInfo)
        # RepoInfo(branch='main', head_commit_id='b3e3c827a755aa235f0c884b99d37af220139364', id=2668333326914369, path='/Repos/<USERNAME>@databricks.com/develop', provider='gitHub', sparse_checkout=None, url='https://github.com/vijaypavann/databricks-sdk-demo.git')
    else:
        print("Updating a existing Repo in DB Workspace....")
        repoId = None

        for repo in repos_list:
            print(repo.path, repo.id, repo.url) 
            if repo.branch == GIT_REMOTE_BRANCH:
                repoId = repo.id
                break    

        if repoId:
            ws.repos.update(repo_id = repoId, branch = GIT_REMOTE_BRANCH)


create_or_update_repo()