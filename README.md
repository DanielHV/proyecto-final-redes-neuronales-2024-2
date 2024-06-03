# proyecto-final-redes-neuronales-2024-2
Clasificación de URLs maliciosas mediante red neuronal multicapa.

Alumno: Hernández Vela Daniel

Clase: Redes neuronales 2024-2

Profesor: Verónica Esther Arriola Ríos

En el [notebook](proyecto_final_rn.ipynb) se encuentra desarrollado el proyecto y se describe de manera resumida, véase el reporte para una descripción más completa.
[Reporte de proyecto final](reporte_proyecto_rn.pdf)

Librerías necesarias para el proyecto (todas disponibles mediante pip install):
- numpy
- pandas
- matplotlib
- pytorch
- sklearn
- ipywidgets
- IPython
- urllib

El [dataset](malicious_phish_updated.csv) se encuentra en el repositorio listo para usarse por lo que no es necesario descargarlo, si lo considera necesario, este puede ser descargado desde Kaggle en el siguiente url:
https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

Para realizar la corrección mencionada en el reporte es necesario desgargar el siguiente dataset:
https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset

Una vez descargados, en la carpeta /correccion_dataset se deberá ejecutar el script correccion_datos.py, el cual generará el archivo malicious_phish_updated.csv, este deberá ser movido al directorio base, o bien, ajustado el directorio en el notebook.