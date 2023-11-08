pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/gregerchen99/JenkinsTest.git'
            }
        }
        stage('build'){
            steps {
                sh 'python3 /var/jenkins_home/workspace/JenkinsTest/source/test.py'
            }
        }
    }   
}