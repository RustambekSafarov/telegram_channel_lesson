from read_data import fromJson
import datetime


def get_post_weekday(data: dict) -> dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    # Initialize a counter
    count = {}
    messages = data['messages']
    wd = {}

    # Loop through the dictionary
    for day in range(0, 7):
        count[day] = 0
        for m in messages:
            d = m['date']
            format_str = '%Y-%m-%dT%H:%M:%S'
            date = datetime.datetime.strptime(d, format_str)
            if m['type'] == 'message':
                count[day] += date.weekday() == day

    return count


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_weekday(data)
print(count)

# Example:
# >>> get_post_weekday(data)

# Output:
# {
#     'monday': 10,
#     'tuesday': 14,
#     'wednesday': 7,
#     'thursday': 0,
#     'friday': 0,
#     'saturday': 0,
#     'sunday': 0
# }
