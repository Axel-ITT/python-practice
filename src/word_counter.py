import boto3
import os

# Get SNS topic ARN from environment variable or hardcode
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN", "arn:aws:sns:us-east-1:123456789012:MyTopic")

sns = boto3.client('sns')


def lambda_handler(event, context):
    try:
        # Main logic
        file_path = '/opt/python/results.txt'
        try:
            with open(file_path, "r") as textfile:
                word_array = textfile.read().split()
        except FileExistsError as e:
            print(e)

        # Format message
        message = "The word count in the results.txt file is {}.'.format(len(word_array))"
        subject = "Word Count Result"

        # Publish to SNS
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject  # Used only for email subscriptions
        )

        return {
            'statusCode': 200,
            'body': 'Success message sent to SNS.'
        }
    except Exception as e:
        print(e)
        raise 