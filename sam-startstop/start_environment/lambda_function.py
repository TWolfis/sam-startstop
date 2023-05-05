import boto3 

#start environment on a fixed schedule

region = 'eu-west-2'

#start ec2 instances 
def start_ec2():
    ec2 = boto3.client('ec2', region_name=region)
    ec2_instances = []

    #get a list of stopped ec2 instances
    for instance in ec2.describe_instances()['Reservations']:
        for i in instance['Instances']:
            if i['State']['Name'] == 'stopped':
                ec2_instances.append(i['InstanceId'])
    
    #check if there are instances to start
    if len(ec2_instances) > 0:
        ec2.start_instances(InstanceIds=ec2_instances)
        print('started instances: ' + str(ec2_instances))
    else:
        print('no instances to start')

#start rds clusters
def start_rds():
    rds = boto3.client('rds', region_name=region)

    #get a list of stopped rds clusters
    for cluster in rds.describe_db_clusters()['DBClusters']:
        if cluster['Status'] == 'stopped':
            #start cluster
            rds.start_db_cluster(DBClusterIdentifier=cluster['DBClusterIdentifier'])
            print('started rds cluster: ' + cluster['DBClusterIdentifier'])
        else:
            print('rds cluster already running: ' + cluster['DBClusterIdentifier'])

def lambda_handler(event,context):
    #start ec2 instances
    start_ec2()
        
    #start rds clusters
    start_rds()
