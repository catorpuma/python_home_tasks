# task_3_7
import shutil
from builder import make_dir, make_file

# buid structure
# make paths
make_dir('my_project/settings')
make_dir('my_project/mainapp/templates/mainapp')
make_dir('my_project/authapp/templates/authapp')
# make files
make_file('my_project/settings/__init__.py')
make_file('my_project/settings/dev.py')
make_file('my_project/settings/prod.py')
# make files
make_file('my_project/mainapp/__init__.py')
make_file('my_project/mainapp/models.py')
make_file('my_project/mainapp/views.py')
make_file('my_project/mainapp/templates/mainapp/base.html')
make_file('my_project/mainapp/templates/mainapp/index.html')
# make files
make_file('my_project/authapp/__init__.py')
make_file('my_project/authapp/models.py')
make_file('my_project/authapp/views.py')
make_file('my_project/authapp/templates/authapp/base.html')
make_file('my_project/authapp/templates/authapp/index.html')

# copy tree
d = ('my_project/templates')
s2 = r'my_project/mainapp/templates'
shutil.copytree(s2, d)

d = ('my_project/templates')
s3 = r'my_project/authapp/templates'
shutil.copytree(s3, d, dirs_exist_ok=True)
