# 💻 MundoPC - Sistema de Gestión de Computadoras

![POO](https://img.shields.io/badge/Programación-Orientada%20a%20Objetos-blueviolet)
![Herencia](https://img.shields.io/badge/Patrones-Herencia-success)
![Modular](https://img.shields.io/badge/Arquitectura-Modular-9cf)
![License](https://img.shields.io/badge/Licencia-MIT-green)

> *"Sistema educativo para gestión de componentes de computadoras demostrando principios fundamentales de POO"*

## 🌟 Características Principales
- 🧩 **Programación modular** bien estructurada
- 🏗️ **Orientación a Objetos** pura (Abstracción, Encapsulamiento)
- 👨‍👦 **Herencia** entre clases (`DispositivoEntrada` → `Raton`, `Teclado`)
- 📦 **Relaciones de agregación** (`Computadora` contiene `Monitor`, `Raton`, etc.)
- 📊 **Sobrecarga de métodos** para flexibilidad

## 🔄 Flujo de Relaciones entre Clases
```mermaid
graph LR
    DispositivoEntrada -->|hereda| Raton
    DispositivoEntrada -->|hereda| Teclado
    Computadora -->|contiene| Monitor
    Computadora -->|usa| Raton
    Computadora -->|usa| Teclado
```
## 🛠️ Metodologías de Desarrollo
```mermaid
pie title Enfoques Utilizados
    "POO Pura" : 45
    "Programación Modular" : 30
    "Herencia" : 10
```
