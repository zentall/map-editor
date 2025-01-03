# MapEditor
This application is a Django-based system for managing and hosting map configurations for [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js). The configurations can be edited using the [django-admin-json-editor](https://pypi.org/project/django-admin-json-editor/) available in the Django admin site.

## Getting started

1. **Clone this repository**  
   ```bash
   git clone https://github.com/zentall/map-editor.git
   ```

1. **Install required modules**  
   ```bash
   pipenv install
   ```

1. **Activate the virtual environment**  
   ```bash
   pipenv shell
   ```

1.  **Import example datasets**  
    ```bash
    python manage.py load_example
    ```

1.  **Run the development server**  
    ```bash
    python manage.py runserver
    ```

1.  **Open example map**  
    Open the map URL displayed in step 4 in your browser.


## Configurations

1.  **Create a superuser for the admin site**  
    ```bash
    python manage.py createsuperuser
    ```

1.  **Run the development server**  
    ```bash
    python manage.py runserver
    ```

1.  **Log in to the admin site**  
    Open [http://localhost:8000/admin/](http://localhost:8000/admin/) in your browser and login using the superuser credentials.


## Data flow
```mermaid
graph TD
  datastore[(Datastore)]
  Django(Django)
  Admin[Admin]
  MapLibre(MapLibre GL JS)

  Admin -- map configurations --> Django
  Django -- MapLayer --> datastore
  Django -- MapSource --> datastore
  Django -- MapPage --> datastore
  datastore -- MapOptions object(JSON) --> MapLibre -- Map --> User
```