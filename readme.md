# PyGB (Python Game Builder)

PyGB (Python Game Builder) is a program designed to facilitate game development in Python, utilizing the Pygame-CE library. This tool assists in the creation of game projects by generating an easy folder structure, scripts, and a straight foward way to the building process.

## Features

- **Game Project Generation**: PyGB automates the creation of a game project folder structure, including essential scripts.
- **Pygame-CE Integration**: Built on top of Pygame-CE, PyGB seamlessly integrates with this library, providing additional abstraction and ease of use for game development.
- **Build Process Assistance**: PyGB assists in the process of building game projects, providing tools and utilities to streamline the deployment process.

## Requirements

Before using PyGB, ensure you have necessary dependencies installed running:

> [!WARNING]
> I higly recomend using pypy for this kind of use,
> But you can easily use python (just spect worst performance)

```bash
pypy -m pip install -r requirements.txt
```

## Usage

To use PyGB, follow these steps:

1. Clone this repository or download the [latest release](https://github.com/NotsumeChan/sdkPyGB?tab=readme-ov-file#build-versions).
2. Navigate to the PyGB directory.
3. Follow the prompts to create a new game project.

> [!NOTE]
> Proyect = The name of your game proyect


```bash
pypy main.py create Proyect
```

4. Once the project is created, navigate to the project directory (it will be inside of the games folder) and start developing your game!!
5. When you are ready to test it, you can use the next promp to build it

```bash
pypy main.py build Proyect
```

> [!NOTE]
> Your game will be inside the games directory

6. Or this to directly run it

```bash
pypy main.py run Proyect
```

## Build Versions

This repository includes a [folder for build versions of the PyGB program](https://github.com/NotsumeChan/sdkPyGB/tree/main/builds). You can find pre-built versions of PyGB in the "builds" directory.

The builds version will work the same as the python files, but is cleaner to work with

> [!WARNING]
> The first build version will come out when is stable enough 

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/NotsumeChan/sdkPyGB/issues).
