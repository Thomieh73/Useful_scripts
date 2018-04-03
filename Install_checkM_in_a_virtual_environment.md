# How to install Checkm in a virtual environment
We want to install [checkM](https://github.com/Ecogenomics/CheckM/wiki) in a virtual environment so that we have no trouble running checkm due to issues with other python installations that might need different versions of python or python packages. This is convenient when working on a high computing cluster, since it allows us to use different kinds of software packages without intereference due to differences in the set-up of these packages.

The best way, in my opinion, is to create a virtual environment using Anaconda or Miniconda, since it creates a virtual environment without any links to other variables in your normal environment. Anaconda is a much larger package than miniconda, but both can set-up the same packages. 

If you have not yet installed Anaconda or miniconda you can do that using the instructions found here:
[Conda download page](https://conda.io/docs/user-guide/install/download.html). Note that when you install Anaconda it will add a line to your `.bashrc` file. That however, does not work well with the slurm set-up on a high computing cluster such as abel.

You should add to to your .bashrc file the following line, so that it points to the conda.sh file in your anaconda installation. Replace the text in capitals in the line below. You can use `nano` to modify your .bashrc file.
```
. /ABSOLUTE-PATH-TO-DIRECTORY/anaconda3/etc/profile.d/conda.sh
```
After changing your .bashrc file you should logout and login into the compute node, or start a new terminal window.

## Commands for Abel (you can skip this for normal linux machines)

#### on the abel cluster, remove loaded modules from memory.
```
 module purge    # remove all loaded modules
```

## Commands to install checkm on a linux machine
after installation and restarting your terminal window, check if conda is available, type:
```
conda
```
When it is present than continue below. If not, make sure that you have your `.bashrc` file correctly set-up.

#### Create a python 2.7 virtual environment with conda. 
We give this environment the name of the software we want to install. Here I use: `checkm_env`.

```
conda create -n checkm_env python=2.7
```
When the installation is finished we need to activate the virtual environment so that we can install the checkm software and all its dependencies.
##### active virtual environment
```
conda activate checkm_env
```
That should give a commandline prompt looking like this:

```
(checkm_env) bash-4.1$
```
Now we are ready to install checkm in this environment using the conda package created for checkM.
[bioconda checkM packages](https://anaconda.org/bioconda/checkm-genome). Install checkm with:

```
conda install -c bioconda checkm-genome 
```
This command installs all the dependencies in the checkm environment we created. After the installation finished you can test the installation by typing:

```
checkm
```
This should start complaining about your database directory. Give it a directory you find suitable and then let is run. It will finish with giving you an overview of the commands.

A better test is to run a test job. You can do that the following way:

```
checkm test ~/checkm_test_results
```
That should finish without any problems. Note that when checkm crashes with a error, it is usually in the pplacer step, and is usually caused by to little memory. I need in this test step more than 4Gb of memory and for a large job checkM can use up to 35 Gb easily.

When the test job is finished we need to deactivate the virtual environment.

```
conda deactivate
```


