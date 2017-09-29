import os
import time
from service_data import ec2, s3, rds, lb, iam

fname = '-' + time.strftime("%d-%m-%Y") + '.csv'
report_path = os.path.dirname(os.path.abspath(__file__))

# get S3 bucket list
# s3.bucket_report(report_path + '/s3_report' + fname)

# get RDS list
# rds.rds_report(report_path + '/rds_report' + fname)

# get ec2 instances list
# ec2.ec2_report(report_path + '/ec2_report' + fname)

# get lb list
# lb.lb_report(report_path + '/lb_report' + fname)

# get iam list
# iam.iam_report(report_path + '/iam_report' + fname)
