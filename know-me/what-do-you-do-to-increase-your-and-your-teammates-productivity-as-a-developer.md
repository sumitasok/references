[Index](index.md)

---
## What do you do to increase your and your teammate's productivity as a developer?

- I set up git commit hooks in every new repo we start. It enables the developers to catch the Linting and many other issue notifications provided by the hooks before committing. So repo has clean code.
- Peer review of architecture before implementation and Peer review of code after coding. (In case of long running projects, we have a WIP PR process, where the PR actively added with code, will be reviewed intermittently to find issues at early stage.
- Having a hosted CI pipeline, can allow the engineer to commit the code and let the server run the long running tests. This allows faster development. But errors will be commited to repo and then resolutions have to be done. Off-loading slow running integrations tests to CI server is fine. I would recommend running the Lint, Vet, Memory check, and related tests to be run in the local before committing.
Currently what we follow is feature branch to development branch to master branch Git work flow. Where CI ensures code runs fine with passing tests. We use Jenkins. And once we are ready for deployment after manual QA gives a go ahead. We deploy using Jenkins trigger.
- Lately Gitlab's CI along with https://medium.com/pantomath/go-tools-gitlab-how-to-do-continuous-integration-like-a-boss-941a3a9ad0b6 is interesting me. I am working on setting it up for my fuiture projects.
