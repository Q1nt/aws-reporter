import os
import time
import click
from service_data.ec2 import ec2_report
from service_data.s3 import bucket_report
from service_data.rds import rds_report
from service_data.lb import lb_report
from service_data.iam import iam_report

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


@click.group()
def reporter():
    """Generates different reports"""
    pass


@reporter.command()
def ec2():
    """Generates ec2 report"""
    click.echo("Going to generate ec2 report")
    ec2_report(report_path + '/rds_report' + fname)