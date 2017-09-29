from boto3.session import Session

session = Session()

exceptions_creds = {'vpc-prod', 'jimmy', 'default', 'my'}


def profile_list():
    return [e for e in session.available_profiles if e not in exceptions_creds]
