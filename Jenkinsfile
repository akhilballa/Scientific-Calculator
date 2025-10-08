pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/akhilballa/Scientific-Calculator.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest discover calculator'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t your-dockerhub-username/scientific-calculator:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-password', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u your-dockerhub-username --password-stdin'
                    sh 'docker push your-dockerhub-username/scientific-calculator:latest'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml -i ansible/inventory.ini'
            }
        }
    }
}
