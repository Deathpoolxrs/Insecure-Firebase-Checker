# Insecure-Firebase-Checker
Insecure-Firebase-Checker


Here's a description you can use for your GitHub repository:

Firebase Security Checker

This Python script allows users to check the security configurations of Firebase databases by analyzing read and write access permissions for specified endpoints. It helps identify potential security vulnerabilities such as allowing anonymous read/write access or exposing sensitive data through specific endpoints.

Features:

Insecure Read Access Detection: Checks if the Firebase database allows anonymous read access or only read access to the root endpoint. It detects potential security risks where sensitive data may be exposed.

Insecure Write Access Detection: Tests the ability to write data to specified endpoints within the Firebase database. It identifies potential security vulnerabilities where unauthorized users can modify data.

Vulnerable Endpoints Identification: Identifies specific endpoints within the Firebase database that may be vulnerable to security risks. It focuses on endpoints like Users and Logs where sensitive data might be exposed.
