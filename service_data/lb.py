import boto3

from infra_data import profiles, regions


def lb_report(pth):
    for account in profiles.profile_list():
        print ('Current account: ' + account)
        for region in regions.region_list():
            print ('Current region: ' + region)
            session = boto3.Session(profile_name=account)
            client = session.client('elb',
                                    region_name=region
                                    )
            response = client.describe_load_balancers()
            # print(str(response))
            for r in response['LoadBalancerDescriptions']:
                try:
                    with open(pth, "a") as myfile:
                        myfile.write(account + ',' + region + ',' + r['CanonicalHostedZoneName'] + '\n')
                except Exception, msg:
                    print (msg)
