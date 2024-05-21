import importlib
import os
import pkgutil

def import_plugins(package):
    package_dir = os.path.dirname(package.__file__)
    for _, module_name, _ in pkgutil.iter_modules([package_dir]):
        importlib.import_module(f"{package.__name__}.{module_name}")

if __name__ == '__main__':
    from nandha import app
    from nandha import plugins  # Assuming plugins is a package with __init__.py
    import_plugins(plugins)
    app.run_polling()
