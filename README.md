# Proyecto de ejemplo - Python TDD (Desarrollo guiado por test)
- Proyecto base para crear ejercicios de Python para los alumnos.
- Incluye la configuración de GitHub Actions para ejecutar los tests automáticamente al subir los cambios a GitHub.
- Se utilizan módulos de Python para separar los tests de los ejercicios.
- El método de trabajo consiste en crear tests junto con el esqueleto de las funciones de código. El alumno deberá crear el código para que la función pase el test.

## Instrucciones para trabajar
1. Clonar repositorio
2. Instalar dependencias (utilizar [entornos virtuales de Python](https://docs.python.org/3/tutorial/venv.html) si se desea)
```bash
pip install -r requirements.txt
```
3. Ejecutar tests
```bash
pytest
```

## Integración continua
- El repositorio cuenta con una acción de GitHub Actions para ejecutar los tests
- Los tests deben crearse en la carpeta `tests` y empezar con el nombre de archivo `test_`
- Se pueden crear tantos archivos de test como se deseen

## Referencias
- [Documentación oficial Python y GitHub Actions](https://docs.github.com/en/actions/guides/building-and-testing-python)
- [Integración continua con Python en GitHub](https://mattsegal.dev/pytest-on-github-actions.html)
- [Documentación sobre PyTest](https://docs.pytest.org/en/6.2.x/goodpractices.html#test-discovery)
