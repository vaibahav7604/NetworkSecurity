import logging
import os
from datetime import datetime

LOG_File=f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

LOG_PATH=os.path.join(os.getcwd(),"logs",LOG_File)
os.makedirs(LOG_PATH,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_PATH,LOG_File)
# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)