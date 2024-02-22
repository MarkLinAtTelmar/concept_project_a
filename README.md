# concept_project_a


use git subtree to sync module repo

https://www.atlassian.com/git/tutorials/git-subtree#:~:text=git%20subtree%20lets%20you%20nest,projects%20can%20manage%20project%20dependencies.&text=Management%20of%20a%20simple%20workflow,supported%20(even%20older%20than%20v1.

init fetch
```
git subtree add --prefix share_module_x https://github.com/MarkLinAtTelmar/share_module_x.git main --squash
```

pull
```
git subtree pull --prefix share_module_x https://github.com/MarkLinAtTelmar/share_module_x.git main --squash

git push origin HEAD:main
```

push
```
git commit -a -m "<message>"
git push origin HEAD:main
git subtree push --prefix=share_module_x/ https://github.com/MarkLinAtTelmar/share_module_x.git main
```