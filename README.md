# 2016-11-03-nsbe-workshop
Materials for the nsbe workshop

The workshop website: https://chendaniely.github.io/2016-11-03-nsbe/

The etherpad URL: http://pad.software-carpentry.org/NSBE-bootcamp.
Note the contents of the etherpad are also saved in `etherpad.txt`


`python_1` contains the data and notebook Jennifer covered in the first part of the first day

`python_2_visualization` contains the data and notebooks covered in the second part of the first day

the git repository covered in the second day is located here: https://github.com/chendaniely/2016-11-03-nsbe-git

## Additional challenge question

Notice that the `python_1` and `python_2_visualization` folders contain duplicate data.
the [Git lesson](https://github.com/chendaniely/2016-11-03-nsbe-git) showed that repositories should have a separate `src` folder for code, and a `data` folder for data.

1. download this repository either with `git clone` or download zip (the `git clone` url can be found by clicking the green `clone or download` link above)
2. create a data folder
3. move the data from `python_1` and `python_2_visualization` into the data folder.  Note: the inflammation and small datasets are both the same
4. create a `src` folder
5. move the `*.ipynb` files from `python_1` and `python_2_visualization` inmto the `src` folder
6. run the code in the notebooks, and you should get the same exact output as before
  1. You will notice that the data loading steps will fail with a file not found error
  2. prepend the data with `../data/`, that is, `inflammation-01.csv` will now become `../data/inflammation-01.csv`
  3. the `../data/` tells python to look for the data one directory above, and then in the `data` folder
  4. after you make this change to the code, the notebooks should run
