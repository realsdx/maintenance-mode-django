# Maintenance mode django apps

*Under development*
<br>
=====
Maintenance Mode    
=====

A app to show maintenance mode error page(503) to normal users.

Quick start
-----------

1. Add "maintenance" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'maintenance',
    ]

2. Include the maintenance URLconf in your project urls.py like this::

    path('maintenance/', include('maintenance.urls')),

3. Run `python manage.py migrate` to create the maintenance models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to set the boolean value of maintenance mode state (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to check if it's working as expected.