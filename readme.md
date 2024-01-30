# PyGB (Python Game Builder)

PyGB (Python Game Builder) is a program designed to facilitate game development in Python, utilizing the Pygame-CE library. This tool assists in the creation of game projects by generating an easy folder structure, scripts, and a straight foward way to the building process.

## Features

- **Game Project Generation**: PyGB automates the creation of a game project folder structure, including essential scripts and assets.
- **Pygame-CE Integration**: Built on top of Pygame-CE, PyGB seamlessly integrates with this library, providing additional functionality and ease of use for game development.
- **Build Process Assistance**: PyGB assists in the process of building game projects, providing tools and utilities to streamline the deployment process.

## Requirements

Before using PyGB, ensure you have necessary dependencies installed running:

```bash
python -m pip install -r requirements.txt
```

## Usage

To use PyGB, follow these steps:

1. Clone this repository or download the latest release.
2. Navigate to the PyGB directory.
3. Follow the prompts to create a new game project.

```bash
python main.py create *TheNameOFYourProyect
```

4. Once the project is created, navigate to the project directory and start developing your game using the provided scripts and assets.
5. When you are ready to test it, you can use the next promp to build it

```bash
python main.py build *TheNameOFYourProyect
```

6. Or this to directly run it

```bash
python main.py run *TheNameOFYourProyect
```

## Build Versions

This repository includes a folder for build versions of the PyGB program. You can find pre-built versions of PyGB in the "builds" directory.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/NotsumeChan/sdkPyGB).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
