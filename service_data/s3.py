import boto3

from infra_data import profiles, regions


def bucket_report(pth):
    for account in profiles.profile_list():
        print ('Current account: ' + account)
        for region in regions.region_list():
            print ('Current region: ' + region)
            session = boto3.Session(profile_name=account)
            client = session.client('s3',
                                    region_name=region
                                    )
            response = client.list_buckets()

            # print (str(response))

            for r in response['Buckets']:
                try:
                    with open(pth, "a") as myfile:
                        myfile.write(account + ',' + region + ',' +
                                     r['Name'] + '\n')
                except Exception, msg:
                    print (str(msg))
