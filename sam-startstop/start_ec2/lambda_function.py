import boto3 

region = 'eu-west-2'
instances = []


def lambda_handler(event,context):
    describeInstances = boto3.resource('ec2')
    for instance in describeInstances.instances.all():
        instances.append(instance.id)
        
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    
    #start rds scienta-test-rdscluster01
    testcluster = "scienta-test-rdscluster01"
    rds = boto3.client('rds', region_name=region)
    rds.start_db_cluster(DBClusterIdentifier=testcluster)
    print('started instances: ' + str(instances))
    print('started  rds cluster: ' + testcluster)