# sam-startstop
AWS SAM deployment that rolls out 2 python3.10 Lambda functions that start/stop any EC2 instance or RDS
Cluster deployment based on a cron schedule. 

## Needed
- AWS Account: https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html
- AWS SAM CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
- Locally configured AWS credentials: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

## Usage
1. Clone the repository.
2. CD into sam-startstop/sam-startstop.
3. sam build.
4. sam deploy.