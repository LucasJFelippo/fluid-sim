# fluid-sim

> Coding Adventure / Challenge 1 . Version 1

 This is a little 2D Fluid Simulator using Python. This is a personal project, and the frist instance of a Cading Adventure series that I plan to do. The motivation behind it is mainly to motivate myself to learn new things, forcing me to get out of my comfort zone and get my hands dirty. All this Coding Adventure thing is inspired by Sebastian Lague's [Coding Adventure](https://www.youtube.com/watch?v=SO83KQuuZvg&list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK) videos, check it out, it's worth it.

 # Getting Started

 This project uses [Python](https://www.python.org/) language, any version above 3.8 should work well, previous versions could result in some problems.

## Prerequisites

* [Python >=3.8](https://www.python.org/downloads/)

## Installation
1. **Clone the repository**
    ```bash
    git clone https://github.com/LucasJFelippo/fluid-sim
    ```

2. **Run the `setup.py` file**
    This file install all packages needed by the project. The list of all packages will be listed below, you could install then meanully if you prefer.

    ```bash
    python setup.py
    ```

    * [Pygame](https://www.pygame.org)
    * [Pygame Widgets](https://pygamewidgets.readthedocs.io/en/stable/)
    * [NumPy](https://numpy.org/)

3. **Run the project**

    ```bash
    python run.py
    ```

# What I learn

I would like to dedicate this section to tell to you all the new things I learned with this project so far.

* I gained a deeper knowledge on project structure and modularization, mainly the idea of Package by Feature;
* I have learned more about `design patterns` like: Decorator, State and Observer. A good source to quick understand and revision of `Design Patterns` is [Refactoring Guru](https://refactoring.guru/design-patterns);
* I gained a deeper understanding of `multithreading`, and the problems that it bring, like race condition. Beside the fact that Python's GIL makes the thread system kind of ignore that kind of problem, you can read more about in [PEP 703](https://peps.python.org/pep-0703/).

* Still learning about `signal events` and events structure in general, how to implement it on Python and how to struct and create coherent events.
* Still learning about `buffers` and how to transmit information between threads. Mainly using Python's [Queue](https://docs.python.org/3/library/queue.html).

* I'm still on the graphics, and thread synchronization part of the project. But I'll learn a ton of physics concepts when I get to the physic part.

# License

And last but not least, the legal jibber jabber. This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details
