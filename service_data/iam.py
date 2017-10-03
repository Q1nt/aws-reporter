import boto3

from infra_data import profiles


def iam_report(pth):
    for account in profiles.profile_list():
        print ('Current account: ' + account)
        session = boto3.Session(profile_name=account)
        client = session.client('iam')
        response = client.list_users()

        for r in response['Users']:
            try:
                with open(pth, "a") as myfile:
                    myfile.write(account + ',' + r['UserName'] + ',' +
                                 str(r['CreateDate'].date()) + '\n')
            except Exception, msg:
                print (str(msg))
