# User Authentication and Authorization

This Documentation will be useful by providing basic instruction about how User Authentication and Authorization works.

Initially let's start by providing information about Database and Models of <b>accounts</b> app.

# User model
User model includes following fields

1. username
2. full_name
3. is_staff (false by default)
4. is_superuser (false by default)
5. password

Important thing to say!
User model will be created by inheriting and AbstractUserModel from Django's default auth subapp.