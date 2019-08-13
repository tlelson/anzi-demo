# Basic Deployment Demo

This project deploys a lambda to AWS that runs arbitary code.  The function of the repo is to demonstrate the team Git workflow that will be used in future with those working on the Edith predictive analytics team.

## Contribution

1. Discuss an issue for work in the [issues](https://github.com/yanliu2/anzi-demo) tab of the repository
2. Start work on the issue by performing the following steps:
- clone the repository
- create a branch in the form `issues/<#-shortname>`
- commit your changes to that branch
3. When complete - Start a [Pull Request (PR)](https://github.com/yanliu2/anzi-demo/pulls)
this is a request to merge your branch into the `master`.
4. Review the PR with the team.  Review and comment in Github
5. When satified that the issue is suitably addressed, merge the PR.


## Build Pipeline
The act of updating the `master` branch will trigger the build process.  In this case the lambda will be deployed.  We can observe this process in [AWS Codebuild](https://incomplete)

ARTIFACT_BUCKET=teal-ml-lambda-bucket
aws cloudformation package \
    --template-file template.yaml \
    --s3-bucket ${ARTIFACT_BUCKET} \
    --s3-prefix anzi-demo  \
    --output-template /tmp/packaged.yaml
aws cloudformation deploy \
    --capabilities CAPABILITY_IAM \
    --template-file /tmp/packaged.yaml \
    --stack-name anzi-demo-stack

