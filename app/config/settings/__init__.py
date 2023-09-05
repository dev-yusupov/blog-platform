from .apps import *
from .base import *
from .database import *

ENV_STATUS = "Dev"

if ENV_STATUS == "Dev":
    from .local import *

else:
    from .production import *