
from read_data import fromJson
# Define a function get post for given month
def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    args:
        data: a dictionary of posts
        month: as number between 1 and 12

    returns: the number of posts for the given month
    """
    # Initialize a counter
    count = 0
    # Loop through the dictionary
    messages= data['messages']
    for i in messages:
        if i['type']=='message':          
            count+=int(i['date'][5:7])==month
        
  
 
    return count

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_month(data,9)
print(count)