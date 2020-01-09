import boto3
import click

session = boto3.Session(profile_name='pythonautomation')
ec2 = session.resource('ec2')

def filter_instances(project):
    filters = [{'Name':'tag:Project', 'Values':[project]}]
    return ec2.instances.filter(Filters=filters)

@click.group()
def instances():
    "Operations on Ec2 instances"

@instances.command("list-instances")
@click.option('--project', required=True)
def list_instances(project):
    "List EC2 instances"

    instances = filter_instances(project);
    for i in instances:

        print(','.join((
        i.id,
        i.instance_type,
        i.state['Name'],
        i.placement['AvailabilityZone'],
        i.public_dns_name))
        )

    return

@instances.command("stop")
@click.option('--project', required=True)
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project);
    for i in instances:

        print("Stopping {0} instance".format(i.id))
        i.stop()

    return

@instances.command("start")
@click.option('--project', required=True)
def start_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project);
    for i in instances:

        print("Starting {0} instance".format(i.id))
        i.start()

    return

if __name__ == '__main__':
    instances()
