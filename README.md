# Smart Device Management System

## Course

**Object-Oriented Programming (Python)**

## Project Title

**Smart Device Management System Using Object-Oriented Programming**



---

# Project Overview

The **Smart Device Management System** is a console-based Python application developed to demonstrate the practical implementation of **Object-Oriented Programming (OOP)** principles. The system simulates the management of smart home devices by allowing users to perform operations such as turning devices on or off, monitoring temperature, adjusting light brightness, and controlling a security camera through an interactive menu.

The project emphasizes software design through the use of classes, inheritance, encapsulation, abstraction, and polymorphism. It illustrates how common attributes and behaviors can be shared among related objects while allowing each device to implement its own specialized functionality.

---

# Objectives

The objectives of this project are to:

* Design a real-world application using Object-Oriented Programming.
* Demonstrate the use of classes and objects.
* Apply inheritance to promote code reuse.
* Implement encapsulation using private attributes and property methods.
* Demonstrate abstraction by exposing only essential operations to users.
* Show polymorphism by allowing different objects to share common behaviors.
* Develop a simple menu-driven application for managing multiple smart devices.

---

# System Description

The system manages three different smart devices:

### 1. SmartDevice (Parent Class)

The `SmartDevice` class serves as the base class from which all other smart devices inherit. It stores common information such as:

* Device name
* Device ID
* Power status

It also provides common methods for:

* Turning devices ON
* Turning devices OFF
* Displaying device information

---

### 2. TemperatureSensor

The `TemperatureSensor` class inherits from `SmartDevice` and adds the ability to:

* Store temperature values
* Display the current temperature

---

### 3. SmartLight

The `SmartLight` class extends the parent class by introducing:

* Adjustable brightness
* Brightness validation
* Brightness increase and decrease operations

---

### 4. SecurityCamera

The `SecurityCamera` class inherits from `SmartDevice` and provides functionality for:

* Starting recording
* Stopping recording

---

# Object-Oriented Programming Concepts Implemented

## Encapsulation

Encapsulation is achieved by declaring important attributes such as:

* Device ID
* Power status
* Brightness

as **private variables**. Access to these variables is controlled using Python property decorators (`@property`) and setter methods, ensuring that only valid data can be assigned.

---

## Inheritance

Inheritance allows the child classes:

* `TemperatureSensor`
* `SmartLight`
* `SecurityCamera`

to inherit common attributes and methods from the `SmartDevice` class. This reduces code duplication and improves maintainability.

---

## Abstraction

The program hides implementation details by providing simple methods such as:

* `turn_on()`
* `turn_off()`
* `display_info()`
* `read_temperature()`
* `increase_brightness()`
* `start_recording()`

Users interact with these methods without needing to understand the internal implementation.

---

## Polymorphism

Polymorphism is demonstrated by creating different device objects that share common behaviors inherited from the parent class. For example, every device object can invoke the `display_info()` method, while each object maintains its own unique state and functionality.

---

# Program Features

The application provides the following features:

* Display information about all registered devices.
* Turn devices ON.
* Turn devices OFF.
* Read temperature from the temperature sensor.
* Adjust the brightness of the smart light.
* Start recording using the security camera.
* Interactive menu-driven interface.
* Input validation for selected properties.



text
Smart Device Management Menu

1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit


 Conclusion

The Smart Device Management System successfully demonstrates the application of fundamental Object-Oriented Programming concepts in Python. Through a well-structured class hierarchy and modular design, the project models real-world smart devices.
