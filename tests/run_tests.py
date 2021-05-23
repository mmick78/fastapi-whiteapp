import os

import pytest

# Either run from a terminal "python -m pytest" or debug here
if __name__ == '__main__':
    os.environ['APP_PORT'] = '4200'
    os.environ['APP_ENV'] = 'development'
    pytest.main()
