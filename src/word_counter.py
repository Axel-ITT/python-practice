def lambda_handler(event, context):
    try:
        with open("results.txt", "r") as textfile:
            word_array = textfile.read().split()
        return len(word_array)
    except FileExistsError as e:
        print(e)
    return {
        'statusCode': 200,
        'body': 'File read successfully.'
    }