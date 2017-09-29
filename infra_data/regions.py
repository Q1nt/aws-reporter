from boto3.session import Session

session = Session()


def region_list():
    return session.get_available_regions('ec2')
