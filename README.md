# VtScanner
# 🛡️ Mini VirusTotal Scanner (Python)

A lightweight desktop application built with **Python** and **Tkinter** that allows users to scan files using the **VirusTotal API** through a simple drag-and-drop interface.

## 🚀 Features

* Drag and drop file scanning
* Integration with the VirusTotal v3 API
* Real-time scan status monitoring
* Displays scan statistics:

  * Malicious
  * Suspicious
  * Harmless
  * Undetected
* Simple and user-friendly GUI using Tkinter

## 🛠️ Technologies Used

* Python 3
* Tkinter
* TkinterDnD2
* Requests Library
* VirusTotal API v3

## 📌 How It Works

1. Launch the application.
2. Drag and drop any file into the drop area.
3. The application uploads the file to VirusTotal.
4. It waits for the analysis to complete.
5. Scan results are displayed in the application window.

## ⚠️ Note

This project requires a valid **VirusTotal API Key**. For security reasons, never expose your personal API key in public repositories. Store it as an environment variable or in a configuration file excluded by `.gitignore`.

## 🎯 Purpose

This project was developed as a learning exercise to understand API integration, desktop GUI development, file handling, and cybersecurity concepts using Python.
