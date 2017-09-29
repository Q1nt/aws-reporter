import boto3

from infra_data import profiles, regions


def rds_report(pth):
    for account in profiles.profile_list():
        print ('Current account: ' + account)
        for region in regions.region_list():
            print ('Current region: ' + region)
            session = boto3.Session(profile_name=account)
            client = session.client('rds',
                                    region_name=region
                                    )
            response = client.describe_db_instances()

            # print str(response)

            for r in response['DBInstances']:
                try:
                    with open(pth, "a") as myfile:
                        myfile.write(
                            account + ',' + region + ',' + r['Endpoint']['Address'] + ',' + r['LicenseModel'] + '\n')
                except Exception, msg:
                    print (str(msg))
