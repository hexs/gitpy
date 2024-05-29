from git import Repo
import os

repo = Repo()

log = repo.git.log('--oneline')
print(log)
print('- -' * 30)

status = repo.git.status()
print(status)
print('- -' * 30)

add = repo.git.add('.')
print(add)
print('- -' * 30)

commit = repo.git.commit('-am "update"')
print(commit)
print('- -' * 30)

push = repo.git.push('origin main')
print(push)
print('- -' * 30)

