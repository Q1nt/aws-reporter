import boto3

from infra_data import profiles, regions


# TODO
# fix issue with exception on tags
def ec2_report(pth):
    for account in profiles.profile_list():
        print ('Current account: ' + account)
        for region in regions.region_list():
            print ('Current region: ' + region)
            session = boto3.Session(profile_name=account)
            client = session.client('ec2',
                                    region_name=region
                                    )
            response = client.describe_instances()
            #
            for r in response['Reservations']:

                for i in r['Instances']:
                    try:
                        for tag in i['Tags']:

                            if tag['Key'] == 'Name':
                                instance_name = tag['Value']
                            else:
                                instance_name = 'None'
                            if tag['Key'] == 'Site':
                                instance_site = tag['Value']
                            else:
                                instance_site = 'None'

                        with open(pth, "a") as myfile:
                            myfile.write(account + ',' + region + ',' + i[
                                'InstanceId'] + ',' + instance_name + ',' + instance_site + ',' + str(
                                i.get('PublicIpAddress')) + ',' + str(i.get('PrivateIpAddress')) + '\n')
                    except Exception, msg:
                        print (msg)
