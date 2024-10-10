# defines a function with an arbitrary keyword argument to build a user profile.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('aliyah', 'caulder', location='reading', field='theatre', college='albright')

print(user_profile)