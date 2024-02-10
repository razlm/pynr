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

        stage('Copy git to host') {
            steps {
                script {
                    sh '''
                        ls -la
                        scp -i /var/jenkins_home/devops-exam.pem -r ./counter-app centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com:/home/centos/.
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com "ls -la"
                    '''
                }
            }
        }

        stage('Build new docker image') {
            steps {
                script {
                    sh '''
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com "sudo docker build -t counter-service /home/centos/counter-app/."
                    '''
                }
            }
        }

        stage('Deploy new docker image') {
            steps {
                script {
                    sh '''
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com 'sudo docker run -d -p 80:80 counter-service'
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    ECHO "Cheking count num:"
                    curl localhost:80
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
