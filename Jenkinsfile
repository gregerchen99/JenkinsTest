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
                script {
                    // Your OWASP DependencyCheck configurations here
                    def dependencyCheckScan = [
                        additionalArguments: '''
                            -o './'
                            -s './'
                            -f 'ALL'
                            --prettyPrint''',
                        odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
                    ]
                    sh 'dependency-check command here' // Perform the DependencyCheck scan
                }
                step([$class: 'DependencyCheckPublisher', pattern: 'dependency-check-report.xml'])
            }
        }

        stage('Integration UI Test') {
            stage('Headless Browser Test') {
                agent {
                    docker {
                        image 'maven:3-alpine' 
                        args '-v /root/.m2:/root/.m2' 
                    }
                }
                steps {
                    sh 'mvn -B -DskipTests clean package'
                    sh 'mvn test'
                }
                post {
                    always {
                        junit 'target/surefire-reports/*.xml'
                    }
                }
            }
        }
    }
}
