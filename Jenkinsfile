pipeline {
    agent any  // You can specify a specific agent label or node if needed

    stages {

        stage('Checkout SCM') {
            steps {
                git 'https://github.com/gregerchen99/JenkinsTest.git'
            }
        }

        stage('Execute Python Script') {
            steps {
                script {
                    // Replace 'python3' with your Python interpreter command if needed
                    sh '/var/jenkins_home/workspace/JenkinsTest/source/test.py'  // Replace with your Python script filename
                }
            }
        }
    }
}
