from read_data import fromJson


def get_post_per_month(data: dict) -> dict:
    """
    Return the number of posts for each month

    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each month
    """
    # Initialize a counter
    count = {}
    # Loop through the dictionary
    messages = data['messages']
    for i in range(1, 13):
        count[i] = 0
        for m in messages:
            if m['type'] == 'message':
                count[i] += int(m['date'][5:7]) == i

    return count


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)

# Example:
# >>> get_post_per_month(data)
# {1: 0, 2: 20, 3: 14, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
