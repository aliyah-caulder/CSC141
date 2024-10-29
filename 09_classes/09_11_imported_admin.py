# Put the user, privileges, and admin class in a separate module and imported them here.

import users

my_user = users.Admin('aliyah', 'caulder', 17, 'theatre', 'reading')
my_user.privileges.show_privileges()