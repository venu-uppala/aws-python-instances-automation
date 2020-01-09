import boto3
import click

session = boto3.Session(profile_name='pythonautomation')
ec2 = session.resource('ec2')

@click.group()
def instances():
    "Operations on Ec2 instances"

@instances.command("list-instances")
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(','.join((
        i.id,
        i.instance_type,
        i.state['Name'],
        i.placement['AvailabilityZone'],
        i.public_dns_name))
        )
    return

if __name__ == '__main__':
    instances()
