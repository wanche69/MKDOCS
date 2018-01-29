from fabric.api import env, cd, prefix, local, run

env.hosts =["cloud"]

def deploy():
	local("git push")
	with prefix("source ~/.virtualenvs/mkdocs/bin/activate")
		with cd("~/Documentos/MKDOCS/mkdocs"):
			run("git pull")
			run("mkdocs build")
