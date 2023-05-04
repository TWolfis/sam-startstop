import boto3 

region = 'eu-west-2'
instances = []


def lambda_handler(event,context):
    describeInstances = boto3.resource('ec2')
    for instance in describeInstances.instances.all():
        instances.append(instance.id)
        
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    
    #start rds scienta-test-rdscluster01
    testcluster = "scienta-test-rdscluster01"
    rds = boto3.client('rds', region_name=region)
    rds.stop_db_cluster(DBClusterIdentifier=testcluster)
    
    print('stopped your instances: ' + str(instances))
    print('stopped  rds cluster: ' + testcluster)
    