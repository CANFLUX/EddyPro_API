# Code to facilitate pre-processing of GHG files for automated flux recalculations
# Created by Dr. June Skeeter

import os
import shutil
from subprocess import run

def Batch(toRun):

    cwd = os.getcwd()
    pid = os.getpid()

    ini = cwd+f'/temp/{pid}/ini/'
    processing = f'{ini}processing.eddypro'
    try:
        os.remove(processing)
    except:
        pass

    shutil.copy(toRun,processing)

    bin = cwd+f'/temp/{pid}/bin/'
    batchFile=f'{bin}runEddyPro.bat'.replace('/',"\\")

    p = run(batchFile, capture_output=True)
    
    log_file = toRun.replace('.eddypro','_log.txt')
    with open(log_file, 'w') as log:
        log.write(p.stdout.decode('utf-8'))

