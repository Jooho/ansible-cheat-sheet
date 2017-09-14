#!/usr/bin/env python

import click
import os
import sys


@click.command()
@click.option('--deploy_type',
              default='cluster',
              type=click.Choice(['cluster', 'infra', 'app', 'logging', 'metrics', 'teardown', 'stop', 'start']),
              help='This option specifies whether you are deploying a new cluster, scaling up nodes, installing cluster \
                    components, tearing everything down, or something else',
              show_default=True)
@click.option('--az',
              type=click.Choice(['us-east-1a', 'us-east-1b', 'us-east-1c', 'us-west-2a', 'us-west-2b', 'us-west-2c']),
              help='The availability zone in which you wish to deploy the OpenShift cluster')
@click.option('--vpc_stack_name',
              help='The name of the CloudFormation stack used to stand up the VPC this cluster will be deployed to')
@click.option('--ec2_keypair',
              default='ose-devops-admin',
              help='The EC2 keypair you wish to use to connect to cluster hosts')
@click.option('--clear_known_hosts',
              is_flag=True,
              help='Adding this flag will delete the known hosts file at ~/.ssh/known_hosts')
@click.option('-f', '--force',
              help='Continue, even if CloudFormation template for cluster infrastructure with same name already exists',
              is_flag=True)
@click.help_option('--help', '-h')
@click.option('-v', '--verbose', count=True)
def launch(deploy_type=None,
           az=None,
           vpc_stack_name=None,
           ec2_keypair=None,
           clear_known_hosts=None,
           force=None,
           verbose=0):

    # Ensure az gets set
    if az is None:
        print "You must specify a value for --az"
        sys.exit(1)

    # Ensure vpc_stack_name is set in appropriate contexts
    if vpc_stack_name is None:
        print "You must specify a value for --vpc_stack_name"
        sys.exit(1)

    # Ensure ec2_keypair is set in appropriate contexts
    if deploy_type in ['cluster', 'infra', 'app'] and ec2_keypair is None:
        print "You must specify a value for --ec2_keypair with --deploy_type in ['cluster', 'infra', 'appp']"
        sys.exit(1)

    # Infer aws region
    region = az[:-1]

    # Ensure EC2 keypair is present
    if deploy_type == 'cluster' and ec2_keypair is None:
        print "You must specify a value for '--ec2_keypair' with '--deploy_type=cluster'"
        sys.exit(1)

    # Clear known_hosts file between cluster deployments
    if clear_known_hosts is True:
        known_hosts_path = os.path.expanduser('~/.ssh/known_hosts')
        if os.path.isfile(known_hosts_path):
            print "Clearing known_hosts file at ~/.ssh/known_hosts"
            os.system("rm -rf " + known_hosts_path)
        else:
            print "No known_hosts file found, skipping"

    # Remove cached ansible facts
    if os.path.isdir('.ansible'):
        print "Removing cached ansible facts"
        os.system('rm -rf .ansible')

    # Refresh dynamic inventory cache
    print "Refreshing dynamic inventory cache"
    os.system('playbooks/inventory/aws/hosts/ec2.py --refresh-cache > /dev/null')

    # Set ansible verbosity flag appropriately. This works based on click's count=True flag.
    if verbose > 0:
        verbosity = '-' + 'v' * verbose
    else:
        verbosity = ''

    # Construct ansible command
    status = os.system(
        'ansible-playbook %s playbooks/deploy.yaml \
        -e "force=%s deploy_type=%s region=%s az=%s vpc_stack_name=%s ec2_keypair=%s" \
        --extra-vars "@playbooks/vars/main.yaml"'
        % (verbosity, force, deploy_type, region, az, vpc_stack_name, ec2_keypair)
    )

    # Exit appropriately
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) != 0:
        sys.exit(os.WEXITSTATUS(status))

if __name__ == '__main__':
    # Ensure AWS environment variables have been set
    if os.getenv('AWS_ACCESS_KEY_ID') is None or os.getenv('AWS_SECRET_ACCESS_KEY') is None:
        print 'AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY must be exported as environment variables.'
        sys.exit(1)

    # Do all the stuff
    launch()
