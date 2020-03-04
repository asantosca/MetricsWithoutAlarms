import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')
limit=10
ourmetrics = {""}
# List metrics through the pagination interface
paginator = cloudwatch.get_paginator('list_metrics')
for response in paginator.paginate():
    for metric in response['Metrics']:
        if (not metric['Namespace'].startswith('AWS')):
            target = cloudwatch.describe_alarms_for_metric(
                Dimensions = metric['Dimensions'],
                MetricName = metric['MetricName'],
                Namespace = metric['Namespace'])
                
            # print(target)
            if ('MetricAlarms' in target):
                print(metric['Namespace'] + "->" + metric['MetricName'])
