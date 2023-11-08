pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/gregerchen99/JenkinsTest.git'
            }
        }

        stage('Execute Python Script') {
            steps {
                script {
                    sh '/var/jenkins_home/workspace/JenkinsTest/source/test.py'
                }
            }
        }
    }
}
