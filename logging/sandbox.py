import logging

# invoke logging.basicConfig to specify which levels to show
logging.basicConfig(level=logging.ERROR) # Can only be called once.

logging.critical('Critical Error will get logged.')
logging.error('Error will get logged.')
logging.warning('Warning will not get logged')


# setting the new logging level, which means everything above
# Debug will get logged./
logging.basicConfig(level=logging.DEBUG)

logging.critical('Critical Error will get logged.')
logging.error('Error will get logged.')
logging.warning('Warning will get logged')
logging.info('Info will get logged')
logging.debug('Debug will get logged')


# Log to file
logging.basicConfig(filename='my_app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s' )

logging.warning("This will get logged to the log file")


# log process id along with level and message:
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

import logging
### Add date and time:
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
