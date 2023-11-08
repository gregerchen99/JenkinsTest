pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/gregerchen99/JenkinsTest.git'
            }
        }

        stage('OWASP DependencyCheck') {
            steps {
                dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
            }
        }

        stage('build'){
            steps {
                sh 'python3 /var/jenkins_home/workspace/JenkinsTest/source/test.py'
            }
        }
    }   
    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}