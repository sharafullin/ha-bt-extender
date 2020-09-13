#create folder
from pathlib import Path
Path("/opt/ha-bt-extender").mkdir(parents=True, exist_ok=True)

#clone repo
import git
repo = git.Repo.clone_from("https://github.com/sharafullin/ha-bt-extender.git", "/opt/ha-bt-extender", branch='master')
