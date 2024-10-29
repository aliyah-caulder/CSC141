# Does the same as 9-11 but user class is in one file which is imported into the same file as privileges and admin which is imported
# here

import admin

my_admin = admin.Admin('aliyah', 'caulder', 17, 'theatre', 'reading')
my_admin.privileges.show_privileges()