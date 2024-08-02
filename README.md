# SaTyR Scheduler
This is a `Python` package for the production of '*revyer*' within the [SaTyR foundation](https://www.satyr.dk/).

This package will be able to load data files (`.csv`) which contain a list of songs or sketches which will need to be practices and from there create a recommended schedule which will include the title of the sketch/song, which people is involved, if there is need for an instructor, what time the practice will commend and what room the practice will happen in.

Furthermore the program will also take people not doing anything and put them in '**Rekvisitten**'. My goal is also to automatically add breaks within the schedule such that people doesn't have to practice all the time.

### Feature list
- [x] PyPi Package for easy install
- [ ] Full documentation of the package and its uses
- [ ] Automatic scheduler with custom timing, breakpoints, room assignment and instructor assignment
  - [ ] Room Assignments
  - [ ] Instructor Assignments
  - [ ] Custom Timing
  - [ ] Breakpoints
  - [ ] Accurately assign people without overlaps
  - [ ] MORE TO COME 

## How to build locally
**NOTE!** To build locally it is recommended to be on a Linux Distro or at least use WSL in windows.

To build locally go into `SatyrScheduler` and run the following command:
```bash
python3 -m build
python3 -m pip install .
```

Remember to also uninstall the package from pip before trying to install. This can be done with the following command:
```bash
pip uninstall SatyrScheduler
```

The script [`clean.sh`](clean.sh) is used to clean the python3 build content. The script [`build.sh`](build.sh) can be used to build the package from scratch without having to clean it.

## How to install
Make sure that `pip` is installed. 

**Install:** To install `SatyrScheduler` run the following command:
```bash
pip install SatyrScheduler
```

**Update:** To update `SatyrScheduler` run the following command:
```bash
pip install --upgrade SatyrScheduler
```


## About SaTyR
SaTyR is a collaboration between the the student revyer at the Natur & Bioscience faculty at Copenhagen university. Its association has eight members (Biology-, Computer- Science-, Physics-, Chemistry-, Mathematics-, Mol.Chem-, Smedie- and GeologyRevy). 

The link for SaTyR can be found [here](https://www.satyr.dk/). 

## About Satyr-Scheduler
### Intended usage
The intended usage of this package is to simply create a schedule, given the data for what need to be trained and where we can. The goal of this package is for now *(31/07-24)* **not** being a formatter. This work will have to be done manually, preferable in $\LaTeX$. 

If the peers of this package deems it a useful tool within revy context, then maybe I will release an update to include a $\LaTeX$ formatter within the package to create a `.pdf` file with the schedule, as defined in our normal way of creating the schedule.

### Manually work which had to be done
#### Data I/O
Pandas is used to read and write data from `.csv` files. But purging and also "fixing" bad data injection from end-user is left up to the developer. For example: `"Hello"` and `" Hello"`. As one can see a space has snug itself within the string. Since we cannot rely on everyone will read the documentation, a more aggressive approach has been made to "*clean*" the inputs. 
 
#### CustomTime
Since dawn of time, everybody has hated `datetime` from python since global formatting is not really an option. This has left me with no options than to create a custom time class. `namedtuple` from `collections` is also used here for "ease-of-us" when dealing with hour+minutes timings.


#### Python version
When I'm sure that both most `GNU+Linux` and Mac's can run `Python 3.12` then I will make this the standard. Not all M3 books can run this version of python and some stable distro releases (*like Debian 12*) is still not supporting `Python 3.12`. 

When we change to version `3.12`, a lot of work can be made "easier" because of [PEP 695](https://peps.python.org/pep-0695/). This would allow us to have custom type syntax, which could reduce the clutter created by the `Schedule` and `CustomTime` classes. Futhermore we would have better f-strings [PEP 701](https://peps.python.org/pep-0701/).

A problem with this update would be that `distutils` has been deprecated [PEP 632](https://peps.python.org/pep-0632/). `setuptools` require this package but from what can be gathered from the internet, `distutils` is still being worked on, but is just only coming from the `setuptools` package, which is not ideal if `setuptools` is needed as an package within `Satyr-Scheduler`. This will be a development problem for later though.