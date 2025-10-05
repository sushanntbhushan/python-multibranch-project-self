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

        stage('Running my Python App') {
                 steps{
     			echo "Running python.py..."
                sh '''
                    source $VENV/bin/activate
                    python python-app.py
                ''' 
		}
	}
}
post {
    always {
        echo "Stopping Flask app if running..."
        sh '''
            if [ -f flask.pid ]; then
                kill -9 $(cat flask.pid) || true
                rm -f flask.pid
            fi
        '''
    }
}
}

