import logging 
logger = logging.getLogger('logg')#manager
logger.setLevel(logging.DEBUG)#cares


console_handler = logging.StreamHandler()#inspector
console_handler.setLevel(logging.ERROR)#cares

formatter = logging.Formatter("%(asctime)s - %(message)s - %(levelname)s")#format
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logging.critical('this is emergency')
import logging

# 1️⃣ Create the logger (department manager)
logger = logging.getLogger("CameraDept")
logger.setLevel(logging.DEBUG)  # what severity messages this manager cares about

# 2️⃣ Create a handler (inspector / destination)
console_handler = logging.StreamHandler()  # inspector who prints messages to console
console_handler.setLevel(logging.WARNING)  # this inspector only reports warnings and above

# 3️⃣ Create a formatter (how the message looks)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 4️⃣ Attach the handler to the logger
logger.addHandler(console_handler)

# 5️⃣ Send messages through the logger
logger.debug("Camera lens aligned")       # DEBUG → manager cares, inspector ignores
logger.info("Camera started filming")     # INFO → manager cares, inspector ignores
logger.warning("Camera battery low")      # WARNING → manager cares, inspector reports
logger.error("Camera malfunction!")       # ERROR → manager cares, inspector reports
logger.critical("Camera exploded!")       # CRITICAL → manager cares, inspector reports
