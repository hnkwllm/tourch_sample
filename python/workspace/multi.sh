cat $SGE_JOB_HOSTLIST > ./hostfile
HOST=${HOSTNAME:0:5}
mpirun --hostfile ./hostfile -np $NHOSTS python main.py 