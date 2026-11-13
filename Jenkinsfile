pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat '"C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                bat '"C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application'
                bat 'start "" "C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline successful!'
        }
        failure {
            echo 'CI Pipeline failed'
        }
    }
}
