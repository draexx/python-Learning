# Python

Este repositorio es para pruebas de python  tanto en programacion de sintaxis como prueba de framework

## Getting Started

PySample contiene codigo de python para prueba
flaskProject Prueba de un proyecto pequeño con flask framework

### Prerequisites

pySample requiere pyTesseract an openCV para la lectura de imagenes
flaskProject tiene el archivo requeriments donde estan las dependencias que se necesitan

### Installing

flaskProject para instalar las dependencias

```
pip install -r requeriments.txt
```

And repeat

```
until finished
```

### Variables de entorno

Para que el flaskProject funcione debes crear las siguientes variables de entorno:

#### Linux/Mac

    export FLASK_APP="entrypoint"
    export FLASK_ENV="development"
    export APP_SETTINGS_MODULE="config.local"

#### Windows

    set "FLASK_APP=entrypoint"
    set "FLASK_ENV=development"
    set "APP_SETTINGS_MODULE=config.local"
    
> Mi recomendación para las pruebas es que añadas esas variables en el fichero "activate" o "activate.bat"
> si estás usando virtualenv

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

## Built With

* [Flask](https://www.palletsprojects.com/p/flask/) - The web framework used
* [pyTesseract](https://pypi.org/project/pytesseract/) - OCR tool for python

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/draexx/946513c6cb2ee2adffca97b2999dc4d2) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Pedro Carranza** - *Initial work* - [Draexx](https://github.com/draexx)

See also the list of [contributors](https://github.com/draexx/python-Learning/contributors) who participated in this project.

## License

This project is licensed under the ??? License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration


