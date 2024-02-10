pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', description: 'Branch name', defaultValue: 'main')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/razlm/pynr', credentialsId: 'git-pat']]])
            }
        }

        stage('Pull repo to vm') {
            steps {
                withCredentials([file(credentialsId: 'ssh-to-vm', variable: 'SSH_KEY')]) {
                    sh '''
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com "echo 'IM INSIDE'"
                    '''
                }
            }
        }

        stage('Build new docker image') {
            steps {
                withCredentials([file(credentialsId: 'ssh-to-vm', variable: 'SSH_KEY')]) {
                    sh '''
                        ls -a ./counter-app/
                        ssh -i $SSH_KEY centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com 'sudo docker build -t counter-service /home/ubuntu/jenkins_compose/jenkins_configuration/pynr/counter-app/Dockerfile'
                    '''
                }
            }
        }

        stage('Deploy new docker image') {
            steps {
                withCredentials([file(credentialsId: 'ssh-to-vm', variable: 'SSH_KEY')]) {
                    sh '''
                        ssh -i $SSH_KEY centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com 'sudo docker run -d -p 80:80 counter-service'
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    ECHO "Cheking count num:"
                    curl -X GET http://ec2-3-120-148-111.eu-central-1.compute.amazonaws.com
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded. Service is ready for production.'
        }

        failure {
            echo 'Pipeline failed. Take necessary actions.'
        }
    }
}
