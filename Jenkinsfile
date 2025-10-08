pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/akhilballa/Scientific-Calculator.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && python -m pip install --upgrade pip'
                sh '. venv/bin/activate && python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest discover calculator'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t akhilballa112/scientific-calculator:latest ./'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-password', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u akhilballa112 --password-stdin'
                    sh 'docker push akhilballa112/scientific-calculator:latest'
                }
            }
        }

        // stage('Deploy with Ansible') {
        //     steps {
        //         sh 'ansible-playbook ansible/deploy.yml -i ansible/inventory.ini'
        //     }
        // }
    }
}
