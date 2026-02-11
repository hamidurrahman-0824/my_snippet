import logging
#create the logger (department manager)
logger = logging.getLogger('First Logger')#best practice __name__ get directly file name
logger.setLevel(logging.DEBUG)

#create a handler (inspector/destination)
console_handler = logging.StreamHandler()#inspector who prints message to console
console_handler.setLevel(logging.WARNING)#this inspector only reposts warnings

#create a formatter (how mesage looks)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

#attach the handler to the logger
logger.addHandler(console_handler)

#send messages through the logger 
logger.debug("Cmaera lens aligned")#debug> manager cares,inspector ignores
logger.info("Camera started filming")#info > manager cares, ins ignores
logger.warning("Camera battery low")#warning> manager cares, inspector reports
logger.error("Camera mafunnction!")#manger cares, inspecotr reports
logger.critical("Camera exploaded!")#manager cares,inspector reports
logging.basicConfig(level=logging.DEBUG,filename="log.log",filemode="a",\
                    format="%(asctime)s - %(levelname)s - %(message)s ")
logger = logging.getLogger(__name__)

exit()
x=2
logging.info(f"the value of x is {x}")
try:
    1/0
except ZeroDivisionError as e:
    logging.error("Zero division error",exc_info=True)
    logging.exception("zero division error")


exit()
logging.debug('deb')
logging.info('inf')
logging.warning('war')#below warning everything will be printed as level set to warining
logging.error('err')
logging.critical('cri')