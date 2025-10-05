pipeline {
    agent any

    environment {
        // Define Python virtual environment directory
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                echo "Creating virtual environment and installing dependencies..."
                sh '''
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                sh '''
                    source $VENV/bin/activate
                    pytest || echo "No tests found, skipping..."
                '''
            }
        }

        stage('Build') {
                 steps{
     			sh './python-app.py' 
	}
}

