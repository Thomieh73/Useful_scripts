# How to install checkm in a virtual environment

We want to install checkm in a virtual environment so that we have no trouble running checkm due to issues with other python installations that might need different versions of python or python packages.
This will set-up checkm in user friendly way.

## Commands for abel (you can skip this for normal linux machines)

#### on the abel cluster, remove loaded modules from memory
```
 module purge    # remove all loaded modules
```
#### loading the python2 module (version 2.7.10)
```
module load python2 hmmer/3.1b2 prodigal pplacer
```

## Commands to install checkm on a linux machine
#### check if the python package virtualenv is available
```
virtualenv —help
```
#### setting up the virtual environment where we will install checkm
```
 virtualenv checkm_env
```
#### active virtual environment
```
 source checkm_env/bin/activate
```

## installing dependencies
Install Hmmer 3.1b2 according to instructions
[Hmmer 3.1b2](http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-macosx-intel.tar.gz)

Install prodigal by downloading the archive from [here](https://github.com/hyattpd/Prodigal) and follow the instructions

Install the [latest release](http://matsen.fhcrc.org/pplacer/) from pplacer 

When this is properly set-up then continue.


#### Now we remove everything from the python path
```
unset PYTHONPATH
```

#### Check python path is empty
```
echo $PYTHONPATH
```

#### Next we install all checkm dependencies with pip
```
pip install numpy
pip install scipy
pip install matplotlib
pip install pysam
pip install dendropy
```
#### and finally we run the checkm installer
```
pip install checkm-genome
```

#### test if checkm can be called
type:
```
checkm
```

#### on abel load a small qlogin to start testing the pipeline

```
qlogin --account=cees --mem-per-cpu=3800M --cpus-per-task=4 --time=2:0:0
```

source that job
```
source /cluster/bin/jobsetup
```

#### downloading the reference dataset to a folder of your choice. on abel do this on work or in a folder in your local area:

**on work:**

```
mkdir /work/users/thhaverk/checkm_db

cd /work/users/thhaverk/checkm_db
```
**on your local area**

```
mkdir ~/nobackup/checkm_db

cd ~/nobackup/checkm_db
```

download the dataset with wget

```
wget https://data.ace.uq.edu.au/public/CheckM_databases/checkm_data_2015_01_16.tar.gz
```
unpacking the archive

```
tar -xzvf checkm_data_2015_01_16.tar.gz
```

#### setting the directory with the reference data

```
checkm data setRoot YOURDIRECTORY_NAME
```
e.g. on the abel work area

```
checkm data setRoot /work/users/thhaverk/checkm_db/
```

#### Now we run the test command

```
checkm test ~/checkm_test_results
```

When this finished without any error messages. than checkm is correctlt installed.
