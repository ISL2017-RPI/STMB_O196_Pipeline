FROM keyi/python2-mcr2017a-rpi-isl


COPY STMB_O196/ ./STMB_O196
COPY O196_STMB_wrapper.py ./
COPY setup.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./

