import boto3 

#stop environment on a fixed schedule

region = 'eu-west-2'

#stop ec2 instances 
def stop_ec2():
    ec2 = boto3.client('ec2', region_name=region)
    ec2_instances = []

    #get a list of stopped ec2 instances
    for instance in ec2.describe_instances()['Reservations']:
        for i in instance['Instances']:
            if i['State']['Name'] == 'running':
                ec2_instances.append(i['InstanceId'])

    #check if there are any instances to stop
    if len(ec2_instances) > 0:
        #stop instances
        ec2.stop_instances(InstanceIds=ec2_instances)
        print('stoped instances: ' + str(ec2_instances))          
    else:
        print('no instances to stop')

#stop rds clusters
def stop_rds():
    rds = boto3.client('rds', region_name=region)
    rds_clusters = []

    #get a list of stopped rds clusters
    for cluster in rds.describe_db_clusters()['DBClusters']:
        if cluster['Status'] == 'running':
            #stop cluster
            rds.stop_db_cluster(DBClusterIdentifier=cluster['DBClusterIdentifier'])
            print('stoped cluster: ' + cluster['DBClusterIdentifier'])
        else:
            print('cluster is not running: ' + cluster['DBClusterIdentifier'])

def lambda_handler(event,context):
    #stop ec2 instances
    stop_ec2()
        
    #stop rds clusters
    stop_rds()
