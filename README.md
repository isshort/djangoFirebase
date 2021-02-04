Database Postgresql database loging to postgresql

    $sudo -u postgres psql
    
    create new database 
    #CREATE DATABASE skynance;
    
    create new user
    #CREATE USER admin1234 WITH PASSWORD 'yourpassword';
    
    Role for users
    #ALTER ROLE admin1234 SET client_encoding TO 'utf8';
    # ALTER ROLE admin1234 SET default_transaction_isolation TO 'read committed';
    # ALTER ROLE admin1234 SET timezone TO 'UTC';
    
    new user access to your database
    # GRANT ALL PRIVILEGES ON DATABASE skynance TO admin1234;
    
    Login with other users
    $sudo psql -U admin1234 -h 127.0.0.1  skynance
    
    change the database permision
    show all database with users
    # \du
    # alter database skynance2 owner to admin1234;

to create hstore extension.

      $ sudo su - postgres

      $ psql

      $ \c data_base_name

      $ CREATE EXTENSION hstore;
 

pipenv

    Installing packages for your project
    $ pipenv install request 
    Pipenv will install the excellent Requests library and create a Pipfile 
    
    To activate this project's virtualenv, run the following:
    $ pipenv shell

    Generate a lockfile:
    $pipenv lock
       Create a new project using Python 3.7, specifically:
   
    $ pipenv --python 3.7

       Remove project virtualenv (inferred from current directory):
       $ pipenv --rm
    
       Install all dependencies for a project (including dev):
       $ pipenv install --dev
    
       Create a lockfile containing pre-releases:
       $ pipenv lock --pre
    
       Show a graph of your installed dependencies:
       $ pipenv graph
    
       Check your installed dependencies for security vulnerabilities:
       $ pipenv check
    
       Install a local setup.py into your virtual environment/Pipfile:
       $ pipenv install -e .
    
       Use a lower-level pip command:
       $ pipenv run pip freeze
    
    Commands:
      check      Checks for PyUp Safety security vulnerabilities and against PEP
                 508 markers provided in Pipfile.
    
      clean      Uninstalls all packages not specified in Pipfile.lock.
      graph      Displays currently-installed dependency graph information.
      install    Installs provided packages and adds them to Pipfile, or (if no
                 packages are given), installs all packages from Pipfile.
    
      lock       Generates Pipfile.lock.
      open       View a given module in your editor.
      run        Spawns a command installed into the virtualenv.
      scripts    Lists scripts in current environment config.
      shell      Spawns a shell within the virtualenv.
      sync       Installs all packages specified in Pipfile.lock.
      uninstall  Uninstalls a provided package and removes it from Pipfile.
      update     Runs lock, then sync.


FireBase 
        
    $ pip install pyrebase

Add Pyrebase to your application
    
For use with only user based authentication we can create the following configuration:
    
    import pyrebase
    
    config = {
      "apiKey": "apiKey",
      "authDomain": "projectId.firebaseapp.com",
      "databaseURL": "https://databaseName.firebaseio.com",
      "storageBucket": "projectId.appspot.com"
    }
    
    firebase = pyrebase.initialize_app(config)


Insert four million rows of test “blog posts” into a database using:
    
    model will be
    
    class BlogPost(models.Model):
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=60)

    INSERT INTO blogpost_blogpost (title, author) SELECT md5(random()::text), md5(random()::text)
    FROM (SELECT generate_series(0, 4000000)) as t;