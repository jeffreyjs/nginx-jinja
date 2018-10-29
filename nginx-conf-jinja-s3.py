import boto3
import botocore
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('nginx.conf.j2')
s3_client = boto3.client('s3')


#Dev Conf
devBucket = 's3dev-bucket'
devProfile = boto3.session.Session(profile_name='dev')
print 'Dev Nginx Config File'
dev_CX_template = template.render(elb = 'web-srv.test.lan', url = 'dev.site.com', dns = '172.0.0.1', level = 'debug')
#print dev_CX_template

with open('outfiles/dev/nginx.conf', 'wb') as dev:
    dev.write(dev_CX_template)

s3_resource.Object(devBucket, dev).upload_file(Filename=nginx.conf)
dev.close()


#ic-Prod Conf
prodBucket = 's3prod-bucket'
prodProfile = boto3.session.Session(profile_name='prod')
print 'Prod Nginx Config File'
prod_CX_template = template.render(elb = 'web-srv.prod.lan', url = 'prod.site.com', dns = '172.10.0.1', level = 'warn')
#print prod_CX_template

with open('outfiles/prod/nginx.conf', 'wb') as prod:
    prod.write(prod_CX_template)

s3_resource.Object(prodBucket, prod).upload_file(Filename=nginx.conf)
prod.close()