import os

get_config().InteractiveShellApp.exec_lines = \
    [
        '%load_ext autoreload',
        '%autoreload 2',
        'import json',
        'import os',
        'import io',
    ] + list(map(lambda x: 'import ' + x.split('.py')[0],
                 filter(lambda x:
                        x.endswith('.py') and x not in ['ipython_config.py'],
                        os.listdir('.'))))

print("--------->>>>>>>> CUSTOM CONFIG LOADED <<<<<<<<<------------")
