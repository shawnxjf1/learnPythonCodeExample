## Mark as source root.
If a folder is marked as a source root, it will be added to PYTHONPATH, and resolve will be performed against it.

## python 2.7和3.4
1.引用包的方式不一样:
  python2.7  方式为:from lib import DBStore.
  python3.4  方式为:from .lib import DBStore (带有.号)
  