pipeline {
    agent any
    tools {
        nodejs "nodejs"
    }
    stages {
        /*
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

        stage('UI Test'){
            steps {
                sh 'python3 /var/jenkins_home/workspace/JenkinsTest/source/test.py'
            }
        }
        */
        stage('SonarQube'){
            steps {
                script {
                    def scannerHome = tool 'SonarQube';
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=. -Dsonar.inclusions=source/*.html -Dsonar.inclusions=source/*.php"
                    }
                }   
            }
        }
    }   
    post {
        /*
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }*/
        always {
            script {
                def issues = scanForIssues tool: [$class: 'SonarQube']
                recordIssues tool: [$class: 'SonarQube'], issues: issues
            }
        }
    }
}