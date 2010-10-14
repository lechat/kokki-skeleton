
from kokki import *

env.include_recipe("ssh")

Package("git-core", action="upgrade")
Package("subversion", action="upgrade")
Package("vim", action="upgrade")
Package("screen", action="upgrade")
Package("htop", action="upgrade")
Package("sysstat", action="upgrade")
Package("python")
Package("python-dev")
