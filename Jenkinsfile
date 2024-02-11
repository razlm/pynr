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

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com "sudo docker build -t counter-service /home/centos/counter-app/."
                    '''
                }
            }
        }

        stage('Run Docker Container for Testing') {
            when {
                expression { params.BRANCH != 'main' }
            }
            steps {
                script {
                    sh '''
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com 'sudo docker run -d -p 90:80 --name counter-service-${params.BRANCH} counter-service'
                        sleep 10
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com 'sudo docker stop counter-service-${params.BRANCH} && sudo docker rm counter-service-${params.BRANCH}'
                    '''
                }
            }
        }

        stage('Deploy Docker Image for Production') {
            when {
                expression { params.BRANCH == 'main' }
            }
            steps {
                script {
                    sh '''
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com "sudo docker stop counter-service && sudo docker rm counter-service"
                        ssh -i /var/jenkins_home/devops-exam.pem centos@ec2-3-120-148-111.eu-central-1.compute.amazonaws.com "sudo docker run -d -p 80:80 --name counter-service counter-service"
                    '''
                }
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
