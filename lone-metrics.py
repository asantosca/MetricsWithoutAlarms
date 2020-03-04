import boto3

# Lists metrics that have no alarms

cloudwatch = boto3.client('cloudwatch')
limit=10

paginator = cloudwatch.get_paginator('list_metrics')
for response in paginator.paginate():
    for metric in response['Metrics']:
        if (not metric['Namespace'].startswith('AWS')):
            target = cloudwatch.describe_alarms_for_metric(
                Dimensions = metric['Dimensions'],
                MetricName = metric['MetricName'],
                Namespace = metric['Namespace'])
                
            if (('MetricAlarms' in target) and len(target['MetricAlarms']) == 0):
                print(metric['Namespace'] + "->" + metric['MetricName'])
